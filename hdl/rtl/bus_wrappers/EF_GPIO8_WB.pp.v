/*
	Copyright 2023 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)

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

/* THIS FILE IS GENERATED, DO NOT EDIT */

`timescale			1ns/1ps
`default_nettype	none


module EF_GPIO8_WB (
	input   wire            ext_clk,
                                        input   wire            clk_i,
                                        input   wire            rst_i,
                                        input   wire [31:0]     adr_i,
                                        input   wire [31:0]     dat_i,
                                        output  wire [31:0]     dat_o,
                                        input   wire [3:0]      sel_i,
                                        input   wire            cyc_i,
                                        input   wire            stb_i,
                                        output  reg             ack_o,
                                        input   wire            we_i,
                                        output  wire            IRQ,
	input	[7:0]	io_in,
	output	[7:0]	io_out,
	output	[7:0]	io_oe
);

	localparam	DATAI_REG_OFFSET = 16'd0;
	localparam	DATAO_REG_OFFSET = 16'd4;
	localparam	DIR_REG_OFFSET = 16'd8;
	localparam	IM_REG_OFFSET = 16'd3840;
	localparam	MIS_REG_OFFSET = 16'd3844;
	localparam	RIS_REG_OFFSET = 16'd3848;
	localparam	IC_REG_OFFSET = 16'd3852;

	wire		clk = clk_i;
	wire		rst_n = (~rst_i);


	wire            wb_valid    = cyc_i & stb_i;
                                        wire            wb_we       = we_i & wb_valid;
                                        wire            wb_re       = ~we_i & wb_valid;
                                        wire[3:0]       wb_byte_sel = sel_i & {4{wb_we}};

	wire [8-1:0]	bus_in;
	wire [8-1:0]	bus_out;
	wire [8-1:0]	bus_oe;
	wire [1-1:0]	pin0_hi;
	wire [1-1:0]	pin1_hi;
	wire [1-1:0]	pin2_hi;
	wire [1-1:0]	pin3_hi;
	wire [1-1:0]	pin4_hi;
	wire [1-1:0]	pin5_hi;
	wire [1-1:0]	pin6_hi;
	wire [1-1:0]	pin7_hi;
	wire [1-1:0]	pin0_lo;
	wire [1-1:0]	pin1_lo;
	wire [1-1:0]	pin2_lo;
	wire [1-1:0]	pin3_lo;
	wire [1-1:0]	pin4_lo;
	wire [1-1:0]	pin5_lo;
	wire [1-1:0]	pin6_lo;
	wire [1-1:0]	pin7_lo;
	wire [1-1:0]	pin0_pe;
	wire [1-1:0]	pin1_pe;
	wire [1-1:0]	pin2_pe;
	wire [1-1:0]	pin3_pe;
	wire [1-1:0]	pin4_pe;
	wire [1-1:0]	pin5_pe;
	wire [1-1:0]	pin6_pe;
	wire [1-1:0]	pin7_pe;
	wire [1-1:0]	pin0_ne;
	wire [1-1:0]	pin1_ne;
	wire [1-1:0]	pin2_ne;
	wire [1-1:0]	pin3_ne;
	wire [1-1:0]	pin4_ne;
	wire [1-1:0]	pin5_ne;
	wire [1-1:0]	pin6_ne;
	wire [1-1:0]	pin7_ne;

	wire [8-1:0]	DATAI_WIRE;
	assign	DATAI_WIRE = bus_in;

	reg [8-1:0]	DATAO_REG;
	assign	bus_out = DATAO_REG;
	always @(posedge clk_i or posedge rst_i) if(rst_i) DATAO_REG <= 0; else if(wb_we & (adr_i[16-1:0]==DATAO_REG_OFFSET)) DATAO_REG <= dat_i[8-1:0];

	reg [8-1:0]	DIR_REG;
	assign	bus_oe = DIR_REG;
	always @(posedge clk_i or posedge rst_i) if(rst_i) DIR_REG <= 0; else if(wb_we & (adr_i[16-1:0]==DIR_REG_OFFSET)) DIR_REG <= dat_i[8-1:0];

	reg [31:0] IM_REG;
	reg [31:0] IC_REG;
	reg [31:0] RIS_REG;

	wire[32-1:0]      MIS_REG	= RIS_REG & IM_REG;
	always @(posedge clk_i or posedge rst_i) if(rst_i) IM_REG <= 0; else if(wb_we & (adr_i[16-1:0]==IM_REG_OFFSET)) IM_REG <= dat_i[32-1:0];
	always @(posedge clk_i or posedge rst_i) if(rst_i) IC_REG <= 32'b0;
                                        else if(wb_we & (adr_i[16-1:0]==IC_REG_OFFSET))
                                            IC_REG <= dat_i[32-1:0];
                                        else
                                            IC_REG <= 32'd0;

	wire [0:0] P0HI = pin0_hi;
	wire [0:0] P1HI = pin1_hi;
	wire [0:0] P2HI = pin2_hi;
	wire [0:0] P3HI = pin3_hi;
	wire [0:0] P4HI = pin4_hi;
	wire [0:0] P5HI = pin5_hi;
	wire [0:0] P6HI = pin6_hi;
	wire [0:0] P7HI = pin7_hi;
	wire [0:0] P0LO = pin0_lo;
	wire [0:0] P1LO = pin1_lo;
	wire [0:0] P2LO = pin2_lo;
	wire [0:0] P3LO = pin3_lo;
	wire [0:0] P4LO = pin4_lo;
	wire [0:0] P5LO = pin5_lo;
	wire [0:0] P6LO = pin6_lo;
	wire [0:0] P7LO = pin7_lo;
	wire [0:0] P0PE = pin0_pe;
	wire [0:0] P1PE = pin1_pe;
	wire [0:0] P2PE = pin2_pe;
	wire [0:0] P3PE = pin3_pe;
	wire [0:0] P4PE = pin4_pe;
	wire [0:0] P5PE = pin5_pe;
	wire [0:0] P6PE = pin6_pe;
	wire [0:0] P7PE = pin7_pe;
	wire [0:0] P0NE = pin0_ne;
	wire [0:0] P1NE = pin1_ne;
	wire [0:0] P2NE = pin2_ne;
	wire [0:0] P3NE = pin3_ne;
	wire [0:0] P4NE = pin4_ne;
	wire [0:0] P5NE = pin5_ne;
	wire [0:0] P6NE = pin6_ne;
	wire [0:0] P7NE = pin7_ne;


	integer _i_;
	always @(posedge clk_i or posedge rst_i) if(rst_i) RIS_REG <= 0; else begin
		for(_i_ = 0; _i_ < 1; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P0HI[_i_ - 0] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 1; _i_ < 2; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P1HI[_i_ - 1] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 2; _i_ < 3; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P2HI[_i_ - 2] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 3; _i_ < 4; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P3HI[_i_ - 3] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 4; _i_ < 5; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P4HI[_i_ - 4] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 5; _i_ < 6; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P5HI[_i_ - 5] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 6; _i_ < 7; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P6HI[_i_ - 6] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 7; _i_ < 8; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P7HI[_i_ - 7] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 8; _i_ < 9; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P0LO[_i_ - 8] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 9; _i_ < 10; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P1LO[_i_ - 9] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 10; _i_ < 11; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P2LO[_i_ - 10] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 11; _i_ < 12; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P3LO[_i_ - 11] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 12; _i_ < 13; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P4LO[_i_ - 12] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 13; _i_ < 14; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P5LO[_i_ - 13] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 14; _i_ < 15; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P6LO[_i_ - 14] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 15; _i_ < 16; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P7LO[_i_ - 15] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 16; _i_ < 17; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P0PE[_i_ - 16] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 17; _i_ < 18; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P1PE[_i_ - 17] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 18; _i_ < 19; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P2PE[_i_ - 18] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 19; _i_ < 20; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P3PE[_i_ - 19] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 20; _i_ < 21; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P4PE[_i_ - 20] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 21; _i_ < 22; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P5PE[_i_ - 21] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 22; _i_ < 23; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P6PE[_i_ - 22] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 23; _i_ < 24; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P7PE[_i_ - 23] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 24; _i_ < 25; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P0NE[_i_ - 24] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 25; _i_ < 26; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P1NE[_i_ - 25] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 26; _i_ < 27; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P2NE[_i_ - 26] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 27; _i_ < 28; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P3NE[_i_ - 27] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 28; _i_ < 29; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P4NE[_i_ - 28] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 29; _i_ < 30; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P5NE[_i_ - 29] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 30; _i_ < 31; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P6NE[_i_ - 30] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 31; _i_ < 32; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(P7NE[_i_ - 31] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
	end

	assign IRQ = |MIS_REG;

	EF_GPIO8 instance_to_wrap (
		.clk(clk),
		.rst_n(rst_n),
		.bus_in(bus_in),
		.bus_out(bus_out),
		.bus_oe(bus_oe),
		.pin0_hi(pin0_hi),
		.pin1_hi(pin1_hi),
		.pin2_hi(pin2_hi),
		.pin3_hi(pin3_hi),
		.pin4_hi(pin4_hi),
		.pin5_hi(pin5_hi),
		.pin6_hi(pin6_hi),
		.pin7_hi(pin7_hi),
		.pin0_lo(pin0_lo),
		.pin1_lo(pin1_lo),
		.pin2_lo(pin2_lo),
		.pin3_lo(pin3_lo),
		.pin4_lo(pin4_lo),
		.pin5_lo(pin5_lo),
		.pin6_lo(pin6_lo),
		.pin7_lo(pin7_lo),
		.pin0_pe(pin0_pe),
		.pin1_pe(pin1_pe),
		.pin2_pe(pin2_pe),
		.pin3_pe(pin3_pe),
		.pin4_pe(pin4_pe),
		.pin5_pe(pin5_pe),
		.pin6_pe(pin6_pe),
		.pin7_pe(pin7_pe),
		.pin0_ne(pin0_ne),
		.pin1_ne(pin1_ne),
		.pin2_ne(pin2_ne),
		.pin3_ne(pin3_ne),
		.pin4_ne(pin4_ne),
		.pin5_ne(pin5_ne),
		.pin6_ne(pin6_ne),
		.pin7_ne(pin7_ne),
		.io_in(io_in),
		.io_out(io_out),
		.io_oe(io_oe)
	);

	assign	dat_o = 
			(adr_i[16-1:0] == DATAI_REG_OFFSET)	? DATAI_WIRE :
			(adr_i[16-1:0] == DATAO_REG_OFFSET)	? DATAO_REG :
			(adr_i[16-1:0] == DIR_REG_OFFSET)	? DIR_REG :
			(adr_i[16-1:0] == IM_REG_OFFSET)	? IM_REG :
			(adr_i[16-1:0] == MIS_REG_OFFSET)	? MIS_REG :
			(adr_i[16-1:0] == RIS_REG_OFFSET)	? RIS_REG :
			(adr_i[16-1:0] == IC_REG_OFFSET)	? IC_REG :
			32'hDEADBEEF;

	always @ (posedge clk_i or posedge rst_i)
		if(rst_i)
			ack_o <= 1'b0;
		else if(wb_valid & ~ack_o)
			ack_o <= 1'b1;
		else
			ack_o <= 1'b0;
endmodule
