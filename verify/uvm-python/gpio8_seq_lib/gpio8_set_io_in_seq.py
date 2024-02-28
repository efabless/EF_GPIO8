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

    def __init__(self, gpios_dir, name="gpio8_set_io_in_seq"):
        UVMSequence.__init__(self, name)
        self.set_automatic_phase_objection(1)
        self.req = gpio8_item()
        self.rsp = gpio8_item()
        self.tag = name
        self.gpios_dir = gpios_dir


    async def body(self):
        for i in range (8):
            if ((self.gpios_dir >> i) & 0b1) == 0:
                self.req.gpios[f"gpio{i}"].val = self.rand_io_val()
                # uvm_info(self.tag, f"gpio{i} rand io value = {self.req.gpios[f'gpio{i}'].val}", UVM_LOW)
            else:
                self.req.gpios[f"gpio{i}"].dir = "output" # to not overide direction if output
        uvm_info(self.tag, "body of set io in " + self.req.convert2string(), UVM_LOW)
        await uvm_do(self, self.req)
    

    def rand_io_val(self):
        return random.choice([0,1])



uvm_object_utils(gpio8_set_io_in_seq)