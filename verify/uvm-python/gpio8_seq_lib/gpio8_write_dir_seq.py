from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_fatal
from EF_UVM.wrapper_env.wrapper_item import wrapper_bus_item
from uvm.base.uvm_config_db import UVMConfigDb
from cocotb.triggers import Timer
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from EF_UVM.wrapper_env.wrapper_seq_lib.wrapper_seq_base import wrapper_seq_base
import random


class gpio8_write_dir_seq(wrapper_seq_base):

    def __init__(self, gpios_dir, name="gpio8_write_dir_seq"):
        super().__init__(name)
        self.gpios_dir = gpios_dir

    async def body(self):
        # get register names/address conversion dict
        await super().body()
        await self.send_req(is_write=True, reg="DIR", data_condition=lambda data: data == self.gpios_dir)


uvm_object_utils(gpio8_write_dir_seq)