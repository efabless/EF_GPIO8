from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_info, uvm_fatal
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from uvm.base import sv, UVM_HIGH, UVM_LOW
from EF_UVM.bus_env.bus_item import bus_item
from uvm.base.uvm_config_db import UVMConfigDb
from EF_UVM.bus_env.bus_seq_lib.bus_seq_base import bus_seq_base
import random


class gpio8_read_datai_seq(bus_seq_base):

    def __init__(self, name="gpio8_read_datai_seq"):
        super().__init__(name)

    async def body(self):
        await super().body()
        await self.send_req(is_write=False, reg="DATAO")


uvm_object_utils(gpio8_read_datai_seq)
