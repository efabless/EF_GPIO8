/*
    Testbench for the WB wrapper for the EF_TMR32 IP (EF_TMR32_wb)
    Author: Mohamed Shalan (mshalan@aucegypt.edu)
    License: MIT
*/

`timescale 1ns/1ns

module EF_GPIO8_apb_tb;

    `include "params.vh"
    `include "apb_tasks.vh"

    localparam CLK_PERIOD = 40;
    localparam TIMEOUT = 1000_000;

    reg  [7:0]	io_in;
	wire [7:0]	io_out;
	wire [7:0]	io_oe;

    reg  		PCLK;
	reg  		PRESETn;
	reg  [31:0]	PADDR;
	reg  		PWRITE;
	reg  		PSEL;
	reg  		PENABLE;
	reg  [31:0]	PWDATA;
	wire [31:0]	PRDATA;
	wire 		PREADY;
	wire 		irq;

    EF_GPIO8_apb MUV (
	    .io_in(io_in),
        .io_out(io_out),
        .io_oe(io_oe),
	    .PCLK(PCLK),
	    .PRESETn(PRESETn),
	    .PADDR(PADDR),
	    .PWRITE(PWRITE),
	    .PSEL(PSEL),
	    .PENABLE(PENABLE),
	    .PWDATA(PWDATA),
	    .PRDATA(PRDATA),
	    .PREADY(PREADY),
	    .irq(irq)
    );

    // Dump the signals
    initial begin
        $dumpfile("EF_GPIO8_apb_tb.vcd");
        $dumpvars(0, MUV);
    end

    // Stop the simulation after 1ms (Tiemout)
    initial begin
        #TIMEOUT;
        $display("Failed: Timeout");
        $finish; 
    end

    // clock and rest generator
    event power_on, reset_done;
    initial begin
        PCLK <= 1'bx;
        PRESETn <= 1'bx;
        // Power ON
        #25;
        -> power_on;
        PSEL <= 0;
        PENABLE <= 0;
    end

    always #(CLK_PERIOD/2) PCLK <= ~PCLK;

    initial begin
        @(power_on);
        PRESETn <= 1'b0;
        PCLK <= 1'b0;
        #999;
        @(posedge PCLK);
        PRESETn <= 1'b1;
        -> reset_done;
        @(test2_done);
        $finish;
    end

    
    // Test Cases
    reg [31:0] data_out;
    event test1_done, test2_done, test3_done, test4_done, test5_done;
    
    // Test case 1
    // Configure the gPIO as an output port and write a unique pattern
    initial begin
        @(reset_done);
        // Period = 20
        apb_w_wr(DIR_REG_ADDR, 32'hFF);
        apb_w_wr(DATAO_REG_ADDR, 32'hA5);
        #10;
        if(io_out === 8'hA5)
            $display("Test 1: Passed");
        else
            $display("Test 1: Failed - Got (%X instead of %X)", data_out, 8'hA5);
        #100;
        -> test1_done;
    end    

    // Test case 2
    // Configure the GPIO as an input port then read Something from the TB
    initial begin
        @(test1_done);
        // Period = 20
        apb_w_wr(DIR_REG_ADDR, 32'h00);
        io_in =  8'hAB;
        apb_w_rd(DATAI_REG_ADDR, data_out);
        #10;
        if(data_out === 8'hAB)
            $display("Test 2: Passed");
        else
            $display("Test 2: Failed - Got (%X instead of %X)", data_out, 8'hAB);
        #100;
        -> test2_done;
    end    

endmodule