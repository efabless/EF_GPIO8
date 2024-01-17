/*
	Copyright 2023 Efabless Corp.

	Author: Mohamed Shalan (mshalan@aucegypt.edu)

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

*/

/* THIS FILE IS GENERATED, edit it to complete the testbench */

`timescale		1ns/1ps

`default_nettype	none

`define			AHBL_AW			16
`define			MS_TB_SIMTIME		1_000_000

`include		"tb_macros.vh"

module EF_GPIO8_AHBL_tb;

	// Change the following parameters as desired
	parameter real CLOCK_PERIOD = 100.0;
	parameter real RESET_DURATION = 999.0;

	// DON NOT Change the following parameters
	localparam [`AHBL_AW-1:0]
			DATAI_REG_OFFSET =	`AHBL_AW'h0000,
			DATAO_REG_OFFSET =	`AHBL_AW'h0004,
			DIR_REG_OFFSET =	`AHBL_AW'h0008,
			IM_REG_OFFSET =		`AHBL_AW'h0f00,
			IC_REG_OFFSET =		`AHBL_AW'h0f0c,
			RIS_REG_OFFSET =	`AHBL_AW'h0f08,
			MIS_REG_OFFSET =	`AHBL_AW'h0f04;

	`TB_AHBL_SIG

	reg	[7:0]	io_in;
	wire	[7:0]	io_out;
	wire	[7:0]	io_oe;

	`TB_CLK(HCLK, CLOCK_PERIOD)
	`TB_ESRST(HRESETn, 1'b0, HCLK, RESET_DURATION)
	`TB_DUMP("AHBL_EF_GPIO8_tb.vcd", EF_GPIO8_AHBL_tb, 0)
	`TB_FINISH(`MS_TB_SIMTIME)

	EF_GPIO8_AHBL DUV (
		`TB_AHBL_SLAVE_CONN,
		.io_in(io_in),
		.io_out(io_out),
		.io_oe(io_oe)
	);

	`include "ahbl_tasks.vh"

	`TB_TEST_EVENT(test1)
	`TB_TEST_EVENT(test2)


	initial begin
		#999 -> e_assert_reset;
		@(e_reset_done);

		// Perform Test 1
		#1000 -> e_test1_start;
		@(e_test1_done);

		// Perform other tests
		#1000 -> e_test2_start;
		@(e_test2_done);

		// Finish the simulation
		$display("All tests have passed");
		#10_000 $finish();
	end

    reg [31:0] data_out;


	// Test 1
	`TB_TEST_BEGIN(test1)
		// Test 1 code goes here
		AHBL_W_WRITE(DIR_REG_OFFSET, 32'hFF);
		AHBL_W_WRITE(DATAO_REG_OFFSET, 32'hA5);
        #100;
        if(io_out === 8'hA5)
            $display("Test 1: Passed");
        else
			begin
			$display("Test 1: Failed - Got (%X instead of %X)", data_out, 8'hA5);
			$finish;
			end
        #100;

	`TB_TEST_END(test1)
	
	`TB_TEST_BEGIN(test2)

		// Period = 20
        AHBL_W_WRITE(DIR_REG_OFFSET, 32'h00);
        io_in =  8'hAB;
        AHBL_W_READ(DATAI_REG_OFFSET, data_out);
        #100;
        if(data_out === 8'hAB)
            $display("Test 2: Passed");
        else
			begin
            $display("Test 2: Failed - Got (%X instead of %X)", data_out, 8'hAB);
			$finish;
			end
        #100;

	`TB_TEST_END(test2)

endmodule
