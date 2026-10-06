// =============================================================================
//  cfu.v  --  Fused pixel-wise  Expansion -> Depthwise -> Projection  CFU
//             (MobileNetV2 inverted-residual block, INT8, TFLite-exact requant)
//
//  Single-file design: copy this file over proj/<your_proj>/cfu.v
//
//  Architecture (follows Yildirim & Ozturk, "RISC-V Based TinyML Accelerator
//  for Depthwise Separable Convolutions in Edge AI"):
//    * 9 Expansion engines, each an 8-way INT8 MAC tree  (3x3 window in parallel)
//    * 1 Depthwise engine, 9-way MAC
//    * NPE Projection engines (output-stationary accumulators)
//    * 9-bank IFMAP buffer (bank = (row%3)*3 + col%3) -> 3x3 window in 1 cycle
//    * on-the-fly padding (no padded tensor, no F1/F2 feature-map buffer)
//    * fully pipelined: one (channel, 8-input-chunk) is issued per clock
//
//  Deliberate deviation from the paper (a correctness fix):
//    the paper pads the *input* of the expansion with the zero-point.  TFLite
//    pads the *expansion output (F1)* of the depthwise layer, so out-of-bound
//    taps here are masked in the depthwise stage (contribution = 0), which is
//    bit-exact with TFLite/TFLM.
//
//  Instruction set  (cfu_op0(funct7, rs1, rs2)):
//    0 PING    -> 0xD5C00001
//    1 CFG     rs1 = cfg register index, rs2 = value
//    2 MEMW    rs1 = {mem_id[4:0], addr[26:0]}, rs2 = 32-bit data
//    3 START
//    4 STATUS  -> {31'b0, busy}
//    5 OUTRD   rs1 = output word index -> 32-bit word (4 int8, NHWC order)
//    6 WAIT    blocks until the accelerator is idle
//    7 CYCLES  -> hardware busy-cycle counter of the last job
// =============================================================================
`timescale 1ns/1ps

// ---------------------------------------------------------------- RAM helpers
module dsc_ram32 #(parameter AW = 8) (
    input              clk,
    input              we,
    input  [AW-1:0]    waddr,
    input  [31:0]      wdata,
    input  [AW-1:0]    raddr,
    output reg [31:0]  rdata
);
    reg [31:0] mem [0:(1<<AW)-1];
    integer i;
    initial begin
        for (i = 0; i < (1<<AW); i = i + 1) mem[i] = 32'd0;
        rdata = 32'd0;
    end
    always @(posedge clk) begin
        if (we) mem[waddr] <= wdata;
        rdata <= mem[raddr];
    end
endmodule

// 64-bit wide read, 32-bit wide write (w32addr = 32-bit word index)
module dsc_ram64 #(parameter AW = 10) (
    input              clk,
    input              we,
    input  [AW:0]      w32addr,
    input  [31:0]      wdata,
    input  [AW-1:0]    raddr,
    output [63:0]      rdata
);
    wire we_lo = we & ~w32addr[0];
    wire we_hi = we &  w32addr[0];
    dsc_ram32 #(AW) lo (.clk(clk), .we(we_lo), .waddr(w32addr[AW:1]), .wdata(wdata),
                        .raddr(raddr), .rdata(rdata[31:0]));
    dsc_ram32 #(AW) hi (.clk(clk), .we(we_hi), .waddr(w32addr[AW:1]), .wdata(wdata),
                        .raddr(raddr), .rdata(rdata[63:32]));
endmodule

// ------------------------------------------------- TFLite-exact requantiser
//  q = clamp( MultiplyByQuantizedMultiplier(acc+bias, mult, shift) + zp )
//  Latency: v_out appears 6 cycles after v_in (inputs sampled in the v_in cycle)
module dsc_requant (
    input                     clk,
    input                     v_in,
    input  signed [31:0]      acc,
    input  signed [31:0]      bias,
    input  signed [31:0]      mult,
    input  signed [31:0]      shift,
    input  signed [31:0]      zp,
    input  signed [31:0]      amin,
    input  signed [31:0]      amax,
    output reg                v_out,
    output reg signed [7:0]   q_out
);
    reg v0, v1, v2, v3, v4;
    // stage 0 : bias add
    reg signed [31:0] x0, m0;  reg signed [31:0] s0;
    // stage 1 : left shift
    reg signed [31:0] x1, m1;  reg [4:0] r1;
    // stage 2/3 : 32x32 multiply (two registers so Vivado can use DSP pipeline regs)
    reg signed [63:0] p2, p3;  reg [4:0] r2, r3; reg o2, o3;
    // stage 4 : saturating rounding doubling high mul
    reg signed [31:0] h4;      reg [4:0] r4;

    wire [4:0] lsh = (s0 > 0) ? s0[4:0] : 5'd0;
    wire signed [31:0] negs = -s0;
    wire [4:0] rsh = (s0 > 0) ? 5'd0 : negs[4:0];

    // stage 4 helpers
    wire signed [63:0] nudge = p3[63] ? (64'sd1 - 64'sd1073741824) : 64'sd1073741824;
    wire signed [63:0] t4    = p3 + nudge;
    wire signed [63:0] t4n   = t4 + 64'sd2147483647;      // trunc-toward-zero for negatives
    wire signed [63:0] q4    = t4[63] ? (t4n >>> 31) : (t4 >>> 31);

    // stage 5 helpers
    wire [31:0] mask  = (32'd1 << r4) - 32'd1;
    wire [31:0] rem   = h4 & mask;
    wire [31:0] thr   = (mask >> 1) + (h4[31] ? 32'd1 : 32'd0);
    wire signed [31:0] sh5 = h4 >>> r4;
    wire signed [31:0] rd5 = sh5 + ((rem > thr) ? 32'sd1 : 32'sd0);
    wire signed [31:0] zz  = rd5 + zp;
    wire signed [31:0] cl  = (zz < amin) ? amin : ((zz > amax) ? amax : zz);

    initial begin v0=0; v1=0; v2=0; v3=0; v4=0; v_out=0; q_out=0; end

    always @(posedge clk) begin
        // 0
        v0 <= v_in;  x0 <= acc + bias;  m0 <= mult;  s0 <= shift;
        // 1
        v1 <= v0;    x1 <= x0 << lsh;   m1 <= m0;    r1 <= rsh;
        // 2
        v2 <= v1;    p2 <= x1 * m1;     r2 <= r1;
        o2 <= (x1 == 32'sh80000000) && (m1 == 32'sh80000000);
        // 3
        v3 <= v2;    p3 <= p2;          r3 <= r2;    o3 <= o2;
        // 4
        v4 <= v3;    h4 <= o3 ? 32'sh7fffffff : q4[31:0];  r4 <= r3;
        // 5
        v_out <= v4; q_out <= cl[7:0];
    end
endmodule

// ============================================================ accelerator core
module dsc_core #(
    parameter NPE     = 56,   // projection engines (max output channels P)
    parameter MAXM_AW = 10,   // expanded-channel index width  (M <= 1024)
    parameter PAW     = 7,    // output-channel index width    (P <= 128)
    parameter IF_AW   = 10,   // IFMAP bank depth (64-bit words)
    parameter EXW_AW  = 12,   // expansion-weight depth (64-bit words)
    parameter OUT_AW  = 12    // output buffer depth (32-bit words)
)(
    input                  clk,
    input                  reset,
    input  [1023:0]        cfg_bus,
    input                  start,
    output reg             busy,
    output reg [31:0]      cycle_cnt,
    input                  mw_en,
    input  [4:0]           mw_id,
    input  [26:0]          mw_addr,
    input  [31:0]          mw_data,
    input  [OUT_AW-1:0]    out_rd_addr,
    output [31:0]          out_rd_data
);
    // ------------------------------------------------------------- config regs
    wire [31:0] c_H      = cfg_bus[ 0*32 +: 32];
    wire [31:0] c_W      = cfg_bus[ 1*32 +: 32];
    wire [31:0] c_M      = cfg_bus[ 3*32 +: 32];
    wire [31:0] c_P      = cfg_bus[ 4*32 +: 32];
    wire [31:0] c_STRIDE = cfg_bus[ 5*32 +: 32];
    wire [31:0] c_OUT_H  = cfg_bus[ 6*32 +: 32];
    wire [31:0] c_OUT_W  = cfg_bus[ 7*32 +: 32];
    wire [31:0] c_ROWOFF = cfg_bus[ 8*32 +: 32];
    wire [31:0] c_COLOFF = cfg_bus[ 9*32 +: 32];
    wire [31:0] c_EXINOFF= cfg_bus[10*32 +: 32];
    wire [31:0] c_EXZP   = cfg_bus[11*32 +: 32];
    wire [31:0] c_EXMIN  = cfg_bus[12*32 +: 32];
    wire [31:0] c_EXMAX  = cfg_bus[13*32 +: 32];
    wire [31:0] c_DWINOFF= cfg_bus[14*32 +: 32];
    wire [31:0] c_DWZP   = cfg_bus[15*32 +: 32];
    wire [31:0] c_DWMIN  = cfg_bus[16*32 +: 32];
    wire [31:0] c_DWMAX  = cfg_bus[17*32 +: 32];
    wire [31:0] c_PRINOFF= cfg_bus[18*32 +: 32];
    wire [31:0] c_PRZP   = cfg_bus[19*32 +: 32];
    wire [31:0] c_PRMIN  = cfg_bus[20*32 +: 32];
    wire [31:0] c_PRMAX  = cfg_bus[21*32 +: 32];
    wire [31:0] c_WQN    = cfg_bus[22*32 +: 32];   // ceil(W/3) * (N/8)
    wire [31:0] c_NC     = cfg_bus[23*32 +: 32];   // N/8

    // ---------------------------------------------------------- tag pipeline
    localparam TW = 27;   // [9:0] m  [10] first_m [11] last_m [12] first_c [13] last_c
                          // [22:14] vmask  [24:23] rm  [26:25] cm
    reg  [TW-1:0] tp  [0:19];
    reg           tvp [0:19];
    integer ti;
    initial for (ti = 0; ti < 20; ti = ti + 1) begin tp[ti] = 0; tvp[ti] = 0; end

    // -------------------------------------------------------- issue-side state
    localparam S_IDLE=3'd0, S_INIT1=3'd1, S_INIT2=3'd2, S_PREP0=3'd3,
               S_PREP1=3'd4, S_ISSUE=3'd5, S_GAP=3'd6, S_DRAIN=3'd7;
    reg [2:0]  state;
    reg [9:0]  oy, ox;
    reg signed [11:0] r0, c0;
    reg [9:0]  m_cnt;
    reg [4:0]  chunk;
    reg [EXW_AW-1:0] exw_cnt, exw_addr;
    reg [15:0] mnc, gap_len, gap_cnt;
    reg [19:0] pix_total;
    reg [31:0] out_total;

    // output-side state (declared early: used by the FSM drain condition)
    reg [1:0]  byte_idx;
    reg [7:0]  ob0, ob1, ob2;
    reg        out_we;
    reg [OUT_AW-1:0] out_waddr;
    reg [31:0] out_wdata;
    reg [31:0] out_wcnt;

    // window parameters (per output pixel)
    reg [2:0]  rv_r, cv_r;
    reg [1:0]  rm_r, cm_r;
    reg [6:0]  qr0, qr1, qr2, qc0, qc1, qc2;
    reg [IF_AW-1:0] base_r [0:8];
    reg [8:0]  vmask_r;
    reg [IF_AW-1:0] ifm_addr [0:8];

    initial begin
        state = S_IDLE; busy = 0; cycle_cnt = 0; gap_cnt = 0;
        byte_idx = 0; out_we = 0; out_wcnt = 0;
    end

    // integer divide-by-3 for 0..1023 (verified exhaustively in scripts/)
    function [9:0] div3; input [9:0] x; reg [19:0] t; begin
        t = x * 10'd683; div3 = t[19:11]; end endfunction

    wire signed [12:0] Hs = {1'b0, c_H[11:0]};
    wire signed [12:0] Ws = {1'b0, c_W[11:0]};

    // PREP0 combinational helpers
    wire signed [11:0] r0p1 = r0 + 12'sd1, r0p2 = r0 + 12'sd2;
    wire signed [11:0] c0p1 = c0 + 12'sd1, c0p2 = c0 + 12'sd2;
    wire [9:0] xr0 = r0   + 12'sd258, xr1 = r0p1 + 12'sd258, xr2 = r0p2 + 12'sd258;
    wire [9:0] xc0 = c0   + 12'sd258, xc1 = c0p1 + 12'sd258, xc2 = c0p2 + 12'sd258;
    wire [9:0] dr0 = div3(xr0), dr1 = div3(xr1), dr2 = div3(xr2);
    wire [9:0] dc0 = div3(xc0), dc1 = div3(xc1), dc2 = div3(xc2);

    // PREP1 combinational helpers
    wire [IF_AW-1:0] Rt0 = rv_r[0] ? qr0 * c_WQN[IF_AW-1:0] : {IF_AW{1'b0}};
    wire [IF_AW-1:0] Rt1 = rv_r[1] ? qr1 * c_WQN[IF_AW-1:0] : {IF_AW{1'b0}};
    wire [IF_AW-1:0] Rt2 = rv_r[2] ? qr2 * c_WQN[IF_AW-1:0] : {IF_AW{1'b0}};
    wire [IF_AW-1:0] Ct0 = cv_r[0] ? qc0 * c_NC[IF_AW-1:0]  : {IF_AW{1'b0}};
    wire [IF_AW-1:0] Ct1 = cv_r[1] ? qc1 * c_NC[IF_AW-1:0]  : {IF_AW{1'b0}};
    wire [IF_AW-1:0] Ct2 = cv_r[2] ? qc2 * c_NC[IF_AW-1:0]  : {IF_AW{1'b0}};
    wire [3*IF_AW-1:0] Rt = {Rt2, Rt1, Rt0};
    wire [3*IF_AW-1:0] Ct = {Ct2, Ct1, Ct0};

    wire last_pix  = (ox == c_OUT_W[9:0] - 10'd1) && (oy == c_OUT_H[9:0] - 10'd1);
    wire start_acc = start && (state == S_IDLE);

    integer b;
    reg [1:0] dy, dx;

    always @(posedge clk) begin
        if (reset) begin
            state <= S_IDLE; busy <= 1'b0;
        end else begin
            if (busy) cycle_cnt <= cycle_cnt + 32'd1;
            case (state)
            S_IDLE: if (start) begin
                busy <= 1'b1; cycle_cnt <= 32'd0;
                oy <= 0; ox <= 0;
                r0 <= c_ROWOFF[11:0]; c0 <= c_COLOFF[11:0];
                m_cnt <= 0; chunk <= 0; exw_cnt <= 0;
                state <= S_INIT1;
            end
            S_INIT1: begin
                mnc       <= c_M[15:0] * c_NC[15:0];
                pix_total <= c_OUT_H[9:0] * c_OUT_W[9:0];
                state <= S_INIT2;
            end
            S_INIT2: begin
                out_total <= pix_total * c_P[7:2];
                gap_len   <= ((c_P[15:0] + 16'd4) > mnc) ? (c_P[15:0] + 16'd4 - mnc) : 16'd0;
                state <= S_PREP0;
            end
            S_PREP0: begin
                rv_r[0] <= (r0   >= 0) && ($signed({r0[11],   r0})   < Hs);
                rv_r[1] <= (r0p1 >= 0) && ($signed({r0p1[11], r0p1}) < Hs);
                rv_r[2] <= (r0p2 >= 0) && ($signed({r0p2[11], r0p2}) < Hs);
                cv_r[0] <= (c0   >= 0) && ($signed({c0[11],   c0})   < Ws);
                cv_r[1] <= (c0p1 >= 0) && ($signed({c0p1[11], c0p1}) < Ws);
                cv_r[2] <= (c0p2 >= 0) && ($signed({c0p2[11], c0p2}) < Ws);
                rm_r <= xr0 - 3*dr0;
                cm_r <= xc0 - 3*dc0;
                qr0 <= dr0 - 10'd86; qr1 <= dr1 - 10'd86; qr2 <= dr2 - 10'd86;
                qc0 <= dc0 - 10'd86; qc1 <= dc1 - 10'd86; qc2 <= dc2 - 10'd86;
                state <= S_PREP1;
            end
            S_PREP1: begin
                for (b = 0; b < 9; b = b + 1) begin
                    dy = (b/3 + 3 - rm_r) % 3;
                    dx = (b%3 + 3 - cm_r) % 3;
                    base_r[b]  <= Rt[dy*IF_AW +: IF_AW] + Ct[dx*IF_AW +: IF_AW];
                    vmask_r[b] <= rv_r[dy] & cv_r[dx];
                end
                state <= S_ISSUE;
            end
            S_ISSUE: begin
                exw_cnt <= exw_cnt + 1'b1;
                if (chunk == c_NC[4:0] - 5'd1) begin
                    chunk <= 0;
                    if (m_cnt == c_M[9:0] - 10'd1) begin
                        m_cnt <= 0; exw_cnt <= 0;
                        if (last_pix) state <= S_DRAIN;
                        else begin
                            if (ox == c_OUT_W[9:0] - 10'd1) begin
                                ox <= 0; oy <= oy + 10'd1;
                                r0 <= r0 + c_STRIDE[11:0]; c0 <= c_COLOFF[11:0];
                            end else begin
                                ox <= ox + 10'd1; c0 <= c0 + c_STRIDE[11:0];
                            end
                            gap_cnt <= gap_len;
                            state <= (gap_len != 0) ? S_GAP : S_PREP0;
                        end
                    end else m_cnt <= m_cnt + 10'd1;
                end else chunk <= chunk + 5'd1;
            end
            S_GAP: begin
                gap_cnt <= gap_cnt - 16'd1;
                if (gap_cnt == 16'd1) state <= S_PREP0;
            end
            S_DRAIN: if ((out_wcnt == out_total) && !out_we) begin
                busy <= 1'b0; state <= S_IDLE;
            end
            default: state <= S_IDLE;
            endcase
        end
    end

    // --------------------------------------------- issue datapath registers
    wire [TW-1:0] tag_next = {cm_r, rm_r, vmask_r, (chunk == c_NC[4:0]-5'd1), (chunk == 5'd0),
                              (m_cnt == c_M[9:0]-10'd1), (m_cnt == 10'd0), m_cnt};
    integer bq;
    always @(posedge clk) begin
        tp[0]  <= tag_next;
        tvp[0] <= (state == S_ISSUE) && !reset;
        for (ti = 1; ti < 20; ti = ti + 1) begin tp[ti] <= tp[ti-1]; tvp[ti] <= tvp[ti-1]; end
        for (bq = 0; bq < 9; bq = bq + 1) ifm_addr[bq] <= base_r[bq] + chunk;
        exw_addr <= exw_cnt;
    end

    // ----------------------------------------------------------- memory decode
    wire [9*64-1:0] ifm_rd;
    wire [63:0]     exw_rd;
    wire [31:0] exb_rd, exm_rd, exs_rd;
    wire [31:0] dwb_rd, dwm_rd, dws_rd;
    wire [31:0] prb_rd, prm_rd, prs_rd;
    wire [9*32-1:0] dww_rd;
    wire [NPE*32-1:0] prw_rd;

    wire [9:0] m3  = tp[3][9:0];
    wire [9:0] m9  = tp[9][9:0];
    wire [9:0] m11 = tp[11][9:0];
    wire [9:0] m17 = tp[17][9:0];
    reg  [PAW-1:0] post_p;

    // expansion weights (64-bit words, read in streaming order)
    dsc_ram64 #(EXW_AW) u_exw (.clk(clk), .we(mw_en && mw_id == 5'd0), .w32addr(mw_addr[EXW_AW:0]),
                               .wdata(mw_data), .raddr(exw_addr), .rdata(exw_rd));
    // expansion per-channel params
    dsc_ram32 #(MAXM_AW) u_exb (.clk(clk), .we(mw_en && mw_id==5'd1), .waddr(mw_addr[MAXM_AW-1:0]), .wdata(mw_data), .raddr(m3), .rdata(exb_rd));
    dsc_ram32 #(MAXM_AW) u_exm (.clk(clk), .we(mw_en && mw_id==5'd2), .waddr(mw_addr[MAXM_AW-1:0]), .wdata(mw_data), .raddr(m3), .rdata(exm_rd));
    dsc_ram32 #(MAXM_AW) u_exs (.clk(clk), .we(mw_en && mw_id==5'd3), .waddr(mw_addr[MAXM_AW-1:0]), .wdata(mw_data), .raddr(m3), .rdata(exs_rd));
    // depthwise params
    dsc_ram32 #(MAXM_AW) u_dwb (.clk(clk), .we(mw_en && mw_id==5'd13), .waddr(mw_addr[MAXM_AW-1:0]), .wdata(mw_data), .raddr(m11), .rdata(dwb_rd));
    dsc_ram32 #(MAXM_AW) u_dwm (.clk(clk), .we(mw_en && mw_id==5'd14), .waddr(mw_addr[MAXM_AW-1:0]), .wdata(mw_data), .raddr(m11), .rdata(dwm_rd));
    dsc_ram32 #(MAXM_AW) u_dws (.clk(clk), .we(mw_en && mw_id==5'd15), .waddr(mw_addr[MAXM_AW-1:0]), .wdata(mw_data), .raddr(m11), .rdata(dws_rd));
    // projection params
    dsc_ram32 #(PAW) u_prb (.clk(clk), .we(mw_en && mw_id==5'd17), .waddr(mw_addr[PAW-1:0]), .wdata(mw_data), .raddr(post_p), .rdata(prb_rd));
    dsc_ram32 #(PAW) u_prm (.clk(clk), .we(mw_en && mw_id==5'd18), .waddr(mw_addr[PAW-1:0]), .wdata(mw_data), .raddr(post_p), .rdata(prm_rd));
    dsc_ram32 #(PAW) u_prs (.clk(clk), .we(mw_en && mw_id==5'd19), .waddr(mw_addr[PAW-1:0]), .wdata(mw_data), .raddr(post_p), .rdata(prs_rd));

    genvar g;
    generate
        for (g = 0; g < 9; g = g + 1) begin : G_BANK
            // 9-bank IFMAP buffer
            dsc_ram64 #(IF_AW) u_if (.clk(clk), .we(mw_en && mw_id == 5'd20 && mw_addr[26:23] == g),
                                     .w32addr(mw_addr[IF_AW:0]), .wdata(mw_data),
                                     .raddr(ifm_addr[g]), .rdata(ifm_rd[g*64 +: 64]));
            // 9-bank depthwise filter buffer (bank j = tap j, TFLite layout [ky][kx][c])
            dsc_ram32 #(MAXM_AW-2) u_dw (.clk(clk), .we(mw_en && mw_id == (5'd4 + g)),
                                     .waddr(mw_addr[MAXM_AW-3:0]), .wdata(mw_data),
                                     .raddr(m9[MAXM_AW-1:2]), .rdata(dww_rd[g*32 +: 32]));
        end
        for (g = 0; g < NPE; g = g + 1) begin : G_PRW
            // per-engine private projection weight buffer
            dsc_ram32 #(8) u_pw (.clk(clk), .we(mw_en && mw_id == 5'd16 && mw_addr[15:8] == g),
                                 .waddr(mw_addr[7:0]), .wdata(mw_data),
                                 .raddr(m17[9:2]), .rdata(prw_rd[g*32 +: 32]));
        end
    endgenerate

    // =================================================== Expansion (9 engines)
    reg ev4;
    initial ev4 = 0;
    always @(posedge clk) ev4 <= tvp[3] && tp[3][13];

    wire [9*8-1:0] f1q_flat;
    wire [8:0]     f1v_w;

    generate
        for (g = 0; g < 9; g = g + 1) begin : ENG
            reg signed [17:0] prod [0:7];
            reg signed [20:0] sum8;
            reg signed [31:0] acc;
            wire [63:0] d = ifm_rd[g*64 +: 64];
            integer i;
            initial acc = 0;
            always @(posedge clk) begin
                for (i = 0; i < 8; i = i + 1)
                    prod[i] <= ($signed(d[i*8 +: 8]) + $signed(c_EXINOFF[9:0])) * $signed(exw_rd[i*8 +: 8]);
                sum8 <= prod[0] + prod[1] + prod[2] + prod[3] + prod[4] + prod[5] + prod[6] + prod[7];
                if (tvp[3]) acc <= (tp[3][12] ? 32'sd0 : acc) + sum8;
            end
            wire signed [7:0] qo;
            dsc_requant u_rq (.clk(clk), .v_in(ev4), .acc(acc), .bias(exb_rd), .mult(exm_rd),
                              .shift(exs_rd), .zp(c_EXZP), .amin(c_EXMIN), .amax(c_EXMAX),
                              .v_out(f1v_w[g]), .q_out(qo));
            assign f1q_flat[g*8 +: 8] = qo;
        end
    endgenerate

    // ====================================================== Depthwise engine
    function [3:0] tapidx; input integer bb; input [1:0] rm; input [1:0] cm;
        integer ddy, ddx;
        begin ddy = (bb/3 + 3 - rm) % 3; ddx = (bb%3 + 3 - cm) % 3; tapidx = ddy*3 + ddx; end
    endfunction

    wire [8:0] vm10 = tp[10][22:14];
    wire [1:0] rm10 = tp[10][24:23];
    wire [1:0] cm10 = tp[10][26:25];
    wire [1:0] bs10 = tp[10][1:0];

    reg signed [17:0] dprod [0:8];
    reg signed [31:0] dsum;
    reg dv11, dv12;
    initial begin dv11 = 0; dv12 = 0; end
    reg [31:0] wsel; reg [7:0] wbyte; reg signed [9:0] tval;
    integer k;
    always @(posedge clk) begin
        for (k = 0; k < 9; k = k + 1) begin
            wsel  = dww_rd[tapidx(k, rm10, cm10)*32 +: 32];
            wbyte = wsel[bs10*8 +: 8];
            tval  = vm10[k] ? ($signed(f1q_flat[k*8 +: 8]) + $signed(c_DWINOFF[9:0])) : 10'sd0;
            dprod[k] <= tval * $signed(wbyte);
        end
        dsum <= dprod[0] + dprod[1] + dprod[2] + dprod[3] + dprod[4]
              + dprod[5] + dprod[6] + dprod[7] + dprod[8];
        dv11 <= f1v_w[0];
        dv12 <= dv11;
    end

    wire dqv; wire signed [7:0] dq;
    dsc_requant u_rq_dw (.clk(clk), .v_in(dv12), .acc(dsum), .bias(dwb_rd), .mult(dwm_rd),
                         .shift(dws_rd), .zp(c_DWZP), .amin(c_DWMIN), .amax(c_DWMAX),
                         .v_out(dqv), .q_out(dq));

    // ================================================ Projection (NPE engines)
    wire [1:0] bs18 = tp[18][1:0];
    wire signed [9:0] f2off = $signed(dq) + $signed(c_PRINOFF[9:0]);
    reg pv19;
    initial pv19 = 0;
    always @(posedge clk) pv19 <= dqv;

    wire load_snap = pv19 && tp[19][11];
    wire [NPE*32-1:0] newsum_flat;
    reg  [NPE*32-1:0] snap_flat;
    reg  post_v0, post_active;

    generate
        for (g = 0; g < NPE; g = g + 1) begin : PE
            reg signed [17:0] pprod;
            reg signed [31:0] pacc;
            wire [31:0] wword = prw_rd[g*32 +: 32];
            wire [7:0]  wb    = wword[bs18*8 +: 8];
            initial begin pacc = 0; pprod = 0; end
            always @(posedge clk) begin
                pprod <= f2off * $signed(wb);
                if (pv19) pacc <= (tp[19][10] ? 32'sd0 : pacc) + pprod;
            end
            assign newsum_flat[g*32 +: 32] = (tp[19][10] ? 32'sd0 : pacc) + pprod;
        end
    endgenerate

    // snapshot shift register -> serial post-processing (no per-engine requant)
    initial begin post_v0 = 0; post_active = 0; post_p = 0; end
    always @(posedge clk) begin
        post_v0 <= 1'b0;
        if (load_snap) begin
            snap_flat   <= newsum_flat;
            post_active <= 1'b1;
            post_p      <= 0;
        end else begin
            if (post_active) begin
                post_v0 <= 1'b1;
                if (post_p == c_P[PAW-1:0] - 1'b1) post_active <= 1'b0;
                else post_p <= post_p + 1'b1;
            end
            if (post_v0) snap_flat <= {32'd0, snap_flat[NPE*32-1:32]};
        end
    end

    wire pqv; wire signed [7:0] pq;
    dsc_requant u_rq_pr (.clk(clk), .v_in(post_v0), .acc(snap_flat[31:0]), .bias(prb_rd), .mult(prm_rd),
                         .shift(prs_rd), .zp(c_PRZP), .amin(c_PRMIN), .amax(c_PRMAX),
                         .v_out(pqv), .q_out(pq));

    // ------------------------------------------ pack int8 -> 32-bit output words
    always @(posedge clk) begin
        out_we <= 1'b0;
        if (start_acc) begin
            out_wcnt <= 32'd0; byte_idx <= 2'd0;
        end else if (pqv) begin
            byte_idx <= byte_idx + 2'd1;
            case (byte_idx)
                2'd0: ob0 <= pq;
                2'd1: ob1 <= pq;
                2'd2: ob2 <= pq;
                2'd3: begin
                    out_we    <= 1'b1;
                    out_wdata <= {pq, ob2, ob1, ob0};
                    out_waddr <= out_wcnt[OUT_AW-1:0];
                    out_wcnt  <= out_wcnt + 32'd1;
                end
            endcase
        end
    end

    dsc_ram32 #(OUT_AW) u_out (.clk(clk), .we(out_we), .waddr(out_waddr), .wdata(out_wdata),
                               .raddr(out_rd_addr), .rdata(out_rd_data));
endmodule

// ================================================================== CFU top
module Cfu (
    input               cmd_valid,
    output              cmd_ready,
    input      [9:0]    cmd_payload_function_id,
    input      [31:0]   cmd_payload_inputs_0,
    input      [31:0]   cmd_payload_inputs_1,
    output              rsp_valid,
    input               rsp_ready,
    output     [31:0]   rsp_payload_outputs_0,
    input               reset,
    input               clk
);
    localparam F_PING=7'd0, F_CFG=7'd1, F_MEMW=7'd2, F_START=7'd3,
               F_STATUS=7'd4, F_OUTRD=7'd5, F_WAIT=7'd6, F_CYCLES=7'd7;
    localparam ST_IDLE=3'd0, ST_RD1=3'd1, ST_RD2=3'd2, ST_WAIT=3'd3, ST_RSP=3'd4;
    localparam OUT_AW = 12;

    reg [31:0] cfg [0:31];
    wire [1023:0] cfg_bus;
    genvar gi;
    generate for (gi = 0; gi < 32; gi = gi + 1) begin : G_CFG
        assign cfg_bus[gi*32 +: 32] = cfg[gi];
    end endgenerate
    integer ci;
    initial for (ci = 0; ci < 32; ci = ci + 1) cfg[ci] = 32'd0;

    reg [2:0]  st;
    reg [31:0] rsp_data;
    reg        mw_en, start_p;
    reg [4:0]  mw_id;
    reg [26:0] mw_addr;
    reg [31:0] mw_data;
    reg [OUT_AW-1:0] out_rd_addr;
    wire       busy;
    wire [31:0] cycle_cnt, out_rd_data;
    initial begin st = ST_IDLE; mw_en = 0; start_p = 0; out_rd_addr = 0; end

    wire [6:0] f7 = cmd_payload_function_id[9:3];

    assign cmd_ready             = (st == ST_IDLE);
    assign rsp_valid             = (st == ST_RSP);
    assign rsp_payload_outputs_0 = rsp_data;

    always @(posedge clk) begin
        mw_en   <= 1'b0;
        start_p <= 1'b0;
        if (reset) st <= ST_IDLE;
        else case (st)
        ST_IDLE: if (cmd_valid) begin
            rsp_data <= 32'd0;
            st <= ST_RSP;
            case (f7)
            F_PING:   rsp_data <= 32'hD5C00001;
            F_CFG:    cfg[cmd_payload_inputs_0[4:0]] <= cmd_payload_inputs_1;
            F_MEMW:   begin mw_en <= 1'b1; mw_id <= cmd_payload_inputs_0[31:27];
                            mw_addr <= cmd_payload_inputs_0[26:0]; mw_data <= cmd_payload_inputs_1; end
            F_START:  start_p <= 1'b1;
            F_STATUS: rsp_data <= {31'd0, busy | start_p};
            F_CYCLES: rsp_data <= cycle_cnt;
            F_OUTRD:  begin out_rd_addr <= cmd_payload_inputs_0[OUT_AW-1:0]; st <= ST_RD1; end
            F_WAIT:   st <= (busy | start_p) ? ST_WAIT : ST_RSP;
            default:  ;
            endcase
        end
        ST_RD1: st <= ST_RD2;
        ST_RD2: begin rsp_data <= out_rd_data; st <= ST_RSP; end
        ST_WAIT: if (!busy && !start_p) st <= ST_RSP;
        ST_RSP: if (rsp_ready) st <= ST_IDLE;
        default: st <= ST_IDLE;
        endcase
    end

    dsc_core #(.NPE(56), .MAXM_AW(10), .PAW(7), .IF_AW(10), .EXW_AW(12), .OUT_AW(OUT_AW)) u_core (
        .clk(clk), .reset(reset), .cfg_bus(cfg_bus), .start(start_p), .busy(busy),
        .cycle_cnt(cycle_cnt), .mw_en(mw_en), .mw_id(mw_id), .mw_addr(mw_addr), .mw_data(mw_data),
        .out_rd_addr(out_rd_addr), .out_rd_data(out_rd_data));
endmodule
