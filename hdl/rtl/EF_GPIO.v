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


    assign pin0_hi = (io_in[0] == 1'b1);

    assign pin0_lo = (io_in[0] == 1'b0);

    edge_detect_pe ped_0 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[0]), .pe(pin0_pe));

    edge_detect_ne ned_0 (.clk(clk), .rst_n(rst_n), .sig(sync_io_in[0]), .ne(pin0_ne));

    

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
