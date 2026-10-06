`timescale 1ns/1ps
// Replays build/cmds.txt (the exact custom-instruction stream produced by the C driver)
// through the CFU command/response interface, and checks every OUTRD response against
// build/expected.hex (Python golden model).
module tb_cfu;
    reg clk = 0, reset = 1;
    always #5 clk = ~clk;                       // 100 MHz

    reg         cmd_valid = 0;
    reg  [9:0]  fid = 0;
    reg  [31:0] in0 = 0, in1 = 0;
    wire        cmd_ready, rsp_valid;
    reg         rsp_ready = 1;
    wire [31:0] rsp;

    Cfu dut (.cmd_valid(cmd_valid), .cmd_ready(cmd_ready), .cmd_payload_function_id(fid),
             .cmd_payload_inputs_0(in0), .cmd_payload_inputs_1(in1),
             .rsp_valid(rsp_valid), .rsp_ready(rsp_ready), .rsp_payload_outputs_0(rsp),
             .reset(reset), .clk(clk));

    reg [31:0] expected [0:262143];
    integer fd, r, ncmd = 0, nout = 0, nerr = 0;
    reg [31:0] op, a, b, resp;
    time t_start = 0, t_end = 0;

    task do_cmd(input [6:0] f7, input [31:0] x, input [31:0] y);
        begin
            @(negedge clk);
            fid = {f7, 3'b000}; in0 = x; in1 = y; cmd_valid = 1;
            @(posedge clk);
            while (!cmd_ready) @(posedge clk);
            #1 cmd_valid = 0;
            @(posedge clk);
            while (!rsp_valid) @(posedge clk);
            resp = rsp;
            repeat (2) @(posedge clk);
        end
    endtask

    initial begin
        $readmemh("build/expected.hex", expected);
        repeat (8) @(posedge clk);
        reset = 0;
        repeat (4) @(posedge clk);

        do_cmd(7'd0, 0, 0);
        if (resp !== 32'hD5C00001) begin $display("FAIL: PING returned %h", resp); nerr = nerr + 1; end

        fd = $fopen("build/cmds.txt", "r");
        if (fd == 0) begin $display("cannot open build/cmds.txt"); $finish; end
        while (!$feof(fd)) begin
            r = $fscanf(fd, "%h %h %h\n", op, a, b);
            if (r == 3) begin
                if (op == 3) t_start = $time;
                do_cmd(op[6:0], a, b);
                if (op == 6) t_end = $time;
                if (op == 5) begin
                    if (resp !== expected[nout]) begin
                        if (nerr < 10) $display("MISMATCH word %0d: got %h expected %h", nout, resp, expected[nout]);
                        nerr = nerr + 1;
                    end
                    nout = nout + 1;
                end
                if (op == 7) $display("[tb] hardware busy cycles reported by CFU: %0d", resp);
                ncmd = ncmd + 1;
            end
        end
        $fclose(fd);
        $display("[tb] commands=%0d  output words checked=%0d  errors=%0d", ncmd, nout, nerr);
        $display("[tb] START->WAIT wall time = %0d cycles @100MHz", (t_end - t_start) / 10);
        if (nerr == 0 && nout > 0) $display("RESULT: PASS");
        else                       $display("RESULT: FAIL");
        $finish;
    end

    initial begin #2000000000; $display("RESULT: TIMEOUT"); $finish; end
endmodule
