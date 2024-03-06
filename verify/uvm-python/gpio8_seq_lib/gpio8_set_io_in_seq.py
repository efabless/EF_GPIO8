from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_info, uvm_fatal
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from uvm.base import sv, UVM_HIGH, UVM_LOW
from gpio8_item.gpio8_item import gpio8_item
from uvm.base.uvm_config_db import UVMConfigDb
from cocotb_coverage.coverage import coverage_db
import os
import random


class gpio8_set_io_in_seq(UVMSequence):

    def __init__(self, name="gpio8_set_io_in_seq"):
        UVMSequence.__init__(self, name)
        self.set_automatic_phase_objection(1)
        self.req = gpio8_item()
        self.rsp = gpio8_item()
        self.tag = name
        self.gpios_dir = 0
        self.gpios_in = None


    async def body(self):
        for i in range (8):
            if ((self.gpios_dir >> i) & 0b1) == 0:
                if self.gpios_in is None: 
                    self.req.gpios[f"gpio{i}"].dir = "input"
                    self.req.gpios[f"gpio{i}"].val = self.rand_io_val() # assign a random value if no value is given 
                    uvm_info(self.tag, f"rand input gpio {i} value = {self.req.gpios[f'gpio{i}'].val}", UVM_LOW)
                else:
                    self.req.gpios[f"gpio{i}"].val = (self.gpios_in >> i ) & 0b1 # assign the value given to the gpios
            else:
                uvm_info(self.tag, f" gpio {i} is output", UVM_LOW)
                self.req.gpios[f"gpio{i}"].dir = "output" # to not overide direction if output
        uvm_info(self.tag, f"direction = {self.gpios_dir:X} body of set io in {self.req.convert2string()}", UVM_LOW)
        await uvm_do(self, self.req)
    

    def rand_io_val(self):
        return random.choice([0,1])

    def set_gpios_dir (self, dir):
        self.gpios_dir = dir

    def set_gpios_in (self, io_in):
        self.gpios_in = io_in


uvm_object_utils(gpio8_set_io_in_seq)