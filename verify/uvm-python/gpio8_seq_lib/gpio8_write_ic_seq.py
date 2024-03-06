from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_fatal
from EF_UVM.bus_env.bus_item import bus_item
from uvm.base.uvm_config_db import UVMConfigDb
from cocotb.triggers import Timer
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from EF_UVM.bus_env.bus_seq_lib.bus_seq_base import bus_seq_base
from gpio8_item.gpio8_item import gpio8_item
import random


class gpio8_write_ic_seq(bus_seq_base):

    def __init__(self , name="gpio8_write_ic_seq"):
        super().__init__(name)
        self.ic = 0

    async def body(self):
        # get register names/address conversion dict
        await super().body()
        await self.send_req(is_write=True, reg="icr", data_condition=lambda data: data == self.ic ) # set interrupt mask

    def set_ic (self, ic):
        self.ic = ic

uvm_object_utils(gpio8_write_ic_seq)