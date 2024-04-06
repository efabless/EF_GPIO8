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


class gpio8_write_im_seq(bus_seq_base):

    def __init__(self, im , name="gpio8_write_im_seq"):
        super().__init__(name)
        self.im = 0

    async def body(self):
        # get register names/address conversion dict
        await super().body()
        # self.req.rand_mode(0)
        # self.req.addr = self.adress_dict["im"]
        # self.req.data = self.im
        # self.req.kind = bus_item.WRITE
        # await uvm_do(self, self.req)

        await self.send_req(is_write=True, reg="im"  ,data_value = self.im ) # set interrupt mask

    def set_im (self, im):
        self.im = im

uvm_object_utils(gpio8_write_im_seq)