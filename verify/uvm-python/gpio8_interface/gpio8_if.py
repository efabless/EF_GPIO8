from uvm.base.sv import sv_if


class gpio8_if(sv_if):
    def __init__(self, dut):
        bus_map = {"CLK": "CLK", "RESETn": "RESETn", "io_in": "io_in", "io_out": "io_out", "io_oe": "io_oe"}
        super().__init__(dut, "", bus_map)
