`timescale 1ns/1ps

module top();
wire [7:0] io_in;
wire [7:0] io_out;
wire [7:0] io_oe;
reg CLK = 0;
wire RESETn;
wire [31:0] PADDR;
wire PWRITE;
wire PSEL;
wire PENABLE;
wire [31:0] PWDATA;
wire [31:0] PRDATA;
wire PREADY;
wire irq;

EF_GPIO8_APB uut(
    .io_in(io_in),
    .io_out(io_out),
    .io_oe(io_oe),
    .PCLK(CLK),
    .PRESETn(RESETn),
    .PADDR(PADDR),
    .PWRITE(PWRITE),
    .PSEL(PSEL),
    .PENABLE(PENABLE),
    .PWDATA(PWDATA),
    .PRDATA(PRDATA),
    .PREADY(PREADY),
    .IRQ(irq)
);

`ifndef SKIP_WAVE_DUMP
initial begin
    $dumpfile("waves.vcd");
    $dumpvars(0, top);
end
`endif

always #5 CLK = !CLK;


endmodule