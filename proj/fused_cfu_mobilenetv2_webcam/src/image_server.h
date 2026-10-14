// image_server.h -- UART image link shared by the board firmware and the PC test harness.
//
// The PC program sends one 224x224x3 RGB image (raw bytes, row-major, R G B) per request:
//
//   PC -> board :  'I' 'M' 'G' '!'   uint32 length (LE, must be 150528)   <length bytes>   uint32 FNV-1a (LE)
//   PC -> board :  'I' 'M' 'G' '?'   (ping)  ->  board answers "@@READY ..."
//   PC -> board :  'B' 'Y' 'E' '!'   (leave the image server)  ->  board answers "@@BYE" and Serve() returns,
//                                    so the firmware falls back to the CFU-Playground menu
//   board -> PC :  "@@ACK ..." (image accepted) | "@@NAK reason=..." (resend)
//                  ... free-form console text (TFLM profile etc.) ...
//                  "@@FUSED blocks=.. hw_cycles=.. cpu_cycles=.."      (optional)
//                  "@@RESULT frame=N top1=I score_e6=S"
//                  "@@TOP5 i:score i:score ..."
//                  "@@LOGITS_E6 v0,v1,...,v999"
//                  "@@END"
// Scores are the FLOAT32 model outputs multiplied by 1e6 and truncated (same convention as the other projects).
// Only getchar()/printf()/putchar() are used, so the same code runs on the VexRiscv console and on a PC pipe.
#pragma once
#include <stdint.h>
#include <stdio.h>

namespace imgsrv {

constexpr int kW = 224, kH = 224, kC = 3;
constexpr uint32_t kBytes = kW * kH * kC;
constexpr int kClasses = 1000;

// Runs the network on one RGB image. Returns the FLOAT32 output tensor (kClasses values) or nullptr on failure.
typedef const float* (*InferFn)(const uint8_t* rgb);

static inline uint32_t Fnv1a(const uint8_t* d, uint32_t n) {
  uint32_t h = 2166136261u;
  for (uint32_t i = 0; i < n; i++) { h ^= d[i]; h *= 16777619u; }
  return h;
}

static inline bool ReadByte(uint8_t* b) {
  int c = getchar();
  if (c < 0) return false;
  *b = (uint8_t)c;
  return true;
}

static inline bool ReadU32(uint32_t* v) {
  uint32_t x = 0;
  for (int i = 0; i < 4; i++) {
    uint8_t b;
    if (!ReadByte(&b)) return false;
    x |= (uint32_t)b << (8 * i);
  }
  *v = x;
  return true;
}

static inline void PrintResult(uint32_t frame, const float* out) {
  int top[5] = {-1, -1, -1, -1, -1};
  for (int k = 0; k < 5; k++) {                      // 5 selection passes (n = 1000, trivial cost)
    int best = -1;
    for (int i = 0; i < kClasses; i++) {
      bool used = false;
      for (int j = 0; j < k; j++) if (top[j] == i) used = true;
      if (!used && (best < 0 || out[i] > out[best])) best = i;
    }
    top[k] = best;
  }
  printf("@@RESULT frame=%lu top1=%d score_e6=%ld\n", (unsigned long)frame, top[0],
         (long)(int32_t)(out[top[0]] * 1000000.0f));
  printf("@@TOP5");
  for (int k = 0; k < 5; k++) printf(" %d:%ld", top[k], (long)(int32_t)(out[top[k]] * 1000000.0f));
  printf("\n@@LOGITS_E6 ");
  for (int i = 0; i < kClasses; i++) printf(i ? ",%ld" : "%ld", (long)(int32_t)(out[i] * 1000000.0f));
  printf("\n@@END\n");
  fflush(stdout);
}

// Returns when the PC sends "BYE!" (the firmware then goes back to its menu) or when the input stream ends
// (PC test harness).
//
// With IMGSRV_MAILBOX (set for the RISC-V firmware, see mnv2_webcam_app.cc) the server also watches a mailbox in RAM:
// a simulator (Renode) can copy a picture straight into the board's memory, so nothing has to travel through the
// simulated UART:
//   board -> PC :  "@@MAILBOX addr=0x........ size=N"     (printed before @@READY)
//   PC writes   :  data  at addr+16 (150528 bytes), uint32 fnv at addr+12, uint32 length at addr+4, and LAST the
//                  uint32 magic 0x494D4721 at addr+0 (= the same "IMG!" frame as over the UART, just in memory)
//   board       :  checks length + FNV-1a exactly like a UART frame, answers @@ACK/@@NAK, runs the network, prints
//                  the usual @@RESULT ... @@END, and clears the magic.
//   PC writes   :  the magic 0x42594521 ("BYE!") instead  ->  the server returns (back to the menu).
// The UART protocol keeps working in parallel (ping, BYE!, and real frames on a real board).
#ifdef IMGSRV_MAILBOX
extern "C" int readchar_nonblock(void);
struct Mailbox {
  volatile uint32_t magic;       // 0x494D4721 when a picture is waiting
  volatile uint32_t length;
  volatile uint32_t seq;         // free for the PC (picture number)
  volatile uint32_t fnv;
  uint8_t data[kBytes];
};
#endif

static inline void Serve(InferFn infer, const char* mode) {
  static uint8_t frame[kBytes];
  uint32_t count = 0;
#ifdef IMGSRV_MAILBOX
  static Mailbox mb __attribute__((aligned(16)));
  mb.magic = 0;
  printf("\n@@MAILBOX addr=0x%08lx size=%lu\n", (unsigned long)(uintptr_t)&mb, (unsigned long)sizeof(Mailbox));
#endif
  printf("\n@@READY mode=%s bytes=%lu\n", mode, (unsigned long)kBytes);
  fflush(stdout);

  // one picture: verify, acknowledge, classify, report.  Returns false only for "connection gone".
  auto handle = [&](const uint8_t* img, uint32_t sent) {
    const uint32_t calc = Fnv1a(img, kBytes);
    if (sent != calc) {
      printf("@@NAK reason=checksum sent=0x%08lx calc=0x%08lx\n", (unsigned long)sent, (unsigned long)calc);
      fflush(stdout);
      return;
    }
    printf("@@ACK len=%lu fnv=0x%08lx\n", (unsigned long)kBytes, (unsigned long)calc);
    fflush(stdout);
    const float* out = infer(img);
    if (!out) { printf("@@NAK reason=inference_failed\n@@END\n"); fflush(stdout); return; }
    PrintResult(++count, out);
  };

  uint32_t win = 0;
  for (;;) {
#ifdef IMGSRV_MAILBOX
    if (mb.magic == 0x42594521u) {                    // "BYE!" placed in the mailbox: leave the server
      mb.magic = 0;
      printf("@@BYE frames=%lu\n", (unsigned long)count);
      fflush(stdout);
      return;
    }
    if (mb.magic == 0x494D4721u) {                    // a picture was placed in the mailbox
      const uint32_t len = mb.length, sent = mb.fnv;
      if (len != kBytes) {
        printf("@@NAK reason=length got=%lu\n", (unsigned long)len); fflush(stdout);
      } else {
        handle(mb.data, sent);
      }
      mb.magic = 0;
      continue;
    }
    if (!readchar_nonblock()) continue;               // nothing on the UART either: keep watching
#endif
    uint8_t c;
    if (!ReadByte(&c)) return;
    win = (win << 8) | c;
    if (win == 0x494D473Fu) {                         // "IMG?"
      printf("@@READY mode=%s bytes=%lu\n", mode, (unsigned long)kBytes);
      fflush(stdout);
      win = 0;
    } else if (win == 0x42594521u) {                  // "BYE!"  -> leave the server
      printf("@@BYE frames=%lu\n", (unsigned long)count);
      fflush(stdout);
      return;
    } else if (win == 0x494D4721u) {                  // "IMG!"  -> a frame over the UART
      win = 0;
      uint32_t len;
      if (!ReadU32(&len)) return;
      if (len != kBytes) { printf("@@NAK reason=length got=%lu\n", (unsigned long)len); fflush(stdout); continue; }
      for (uint32_t i = 0; i < len; i++) if (!ReadByte(&frame[i])) return;
      uint32_t sent;
      if (!ReadU32(&sent)) return;
      handle(frame, sent);
    }
  }
}

}  // namespace imgsrv
