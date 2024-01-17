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

module EF_GPIO8 (
    input  wire         clk,
    input  wire         rst_n,
    input  wire [7:0]   io_in,
    output wire [7:0]   bus_in,
    output wire [7:0]   io_out,
    input  wire [7:0]   bus_out,
    output wire [7:0]   io_oe,
    input  wire [7:0]   bus_oe,

    output wire pin0_hi,
    output wire pin1_hi,
    output wire pin2_hi,
    output wire pin3_hi,
    output wire pin4_hi,
    output wire pin5_hi,
    output wire pin6_hi,
    output wire pin7_hi,
    
    output wire pin0_lo,
    output wire pin1_lo,
    output wire pin2_lo,
    output wire pin3_lo,
    output wire pin4_lo,
    output wire pin5_lo,
    output wire pin6_lo,
    output wire pin7_lo,

    output wire pin0_pe,
    output wire pin1_pe,
    output wire pin2_pe,
    output wire pin3_pe,
    output wire pin4_pe,
    output wire pin5_pe,
    output wire pin6_pe,
    output wire pin7_pe,

    output wire pin0_ne,
    output wire pin1_ne,
    output wire pin2_ne,
    output wire pin3_ne,
    output wire pin4_ne,
    output wire pin5_ne,
    output wire pin6_ne,
    output wire pin7_ne
    
);
    wire [7:0] sync_io_in;

    bf_sync2 synchronizer[7:0] (.clk(clk), .sig(io_in), .sync_sig(sync_io_in));
    
    assign bus_in = sync_io_in;
    assign io_out = bus_out;
    assign io_oe  = bus_oe;

    assign pin0_hi = (sync_io_in[0] == 1'b1);
    assign pin1_hi = (sync_io_in[1] == 1'b1);
    assign pin2_hi = (sync_io_in[2] == 1'b1);
    assign pin3_hi = (sync_io_in[3] == 1'b1);
    assign pin4_hi = (sync_io_in[4] == 1'b1);
    assign pin5_hi = (sync_io_in[5] == 1'b1);
    assign pin6_hi = (sync_io_in[6] == 1'b1);
    assign pin7_hi = (sync_io_in[7] == 1'b1);
    
    assign pin0_lo = (sync_io_in[0] == 1'b0);
    assign pin1_lo = (sync_io_in[1] == 1'b0);
    assign pin2_lo = (sync_io_in[2] == 1'b0);
    assign pin3_lo = (sync_io_in[3] == 1'b0);
    assign pin4_lo = (sync_io_in[4] == 1'b0);
    assign pin5_lo = (sync_io_in[5] == 1'b0);
    assign pin6_lo = (sync_io_in[6] == 1'b0);
    assign pin7_lo = (sync_io_in[7] == 1'b0);

    edge_detect_pe ped_0 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[0]), .pe(pin0_pe));
    edge_detect_pe ped_1 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[1]), .pe(pin1_pe));
    edge_detect_pe ped_2 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[2]), .pe(pin2_pe));
    edge_detect_pe ped_3 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[3]), .pe(pin3_pe));
    edge_detect_pe ped_4 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[4]), .pe(pin4_pe));
    edge_detect_pe ped_5 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[5]), .pe(pin5_pe));
    edge_detect_pe ped_6 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[6]), .pe(pin6_pe));
    edge_detect_pe ped_7 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[7]), .pe(pin7_pe));

    edge_detect_ne ned_0 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[0]), .ne(pin0_ne));
    edge_detect_ne ned_1 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[1]), .ne(pin1_ne));
    edge_detect_ne ned_2 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[2]), .ne(pin2_ne));
    edge_detect_ne ned_3 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[3]), .ne(pin3_ne));
    edge_detect_ne ned_4 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[4]), .ne(pin4_ne));
    edge_detect_ne ned_5 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[5]), .ne(pin5_ne));
    edge_detect_ne ned_6 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[6]), .ne(pin6_ne));
    edge_detect_ne ned_7 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[7]), .ne(pin7_ne));

    

endmodule

module edge_detect_pe(
    input wire clk,
    input wire rst_n,
    input wire sig,
    output wire pe
);
    reg sig_delayed;
    always @(posedge clk or negedge rst_n)
        if(!rst_n) 
            sig_delayed <= 1'b0;
        else
            sig_delayed <= sig;
            
    assign pe = ~sig_delayed & sig;

endmodule

module edge_detect_ne(
    input wire clk,
    input wire rst_n,
    input wire sig,
    output wire ne
);
    reg sig_delayed;
    always @(posedge clk or negedge rst_n)
        if(!rst_n) 
            sig_delayed <= 1'b0;
        else
            sig_delayed <= sig;
            
    assign ne = sig_delayed & ~sig;

endmodule

module bf_sync2(
    input wire clk,
    input wire sig,
    output wire sync_sig    
);
    reg[1:0] sync_ff;
    always @(posedge clk)
        sync_ff <= {sync_ff[0], sig};
    
    assign sync_sig = sync_ff[1];

endmodule
