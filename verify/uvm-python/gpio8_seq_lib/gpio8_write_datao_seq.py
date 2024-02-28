from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_fatal
from EF_UVM.wrapper_env.wrapper_item import wrapper_bus_item
from uvm.base.uvm_config_db import UVMConfigDb
from cocotb.triggers import Timer
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from EF_UVM.wrapper_env.wrapper_seq_lib.wrapper_seq_base import wrapper_seq_base
import random


class gpio8_write_datao_seq(wrapper_seq_base):

    def __init__(self, gpios_dir, name="gpio8_write_datao_seq"):
        super().__init__(name)
        self.gpios_dir = gpios_dir

    async def body(self):
        # get register names/address conversion dict
        await super().body()
        gpios_datao = 0
        for i in range (8):
            if ((self.gpios_dir >> i) & 0b1):
                gpios_datao |= (self.rand_io_val() << i)
        await self.send_req(is_write=True, reg="DATAO", data_condition=lambda data: data == gpios_datao)


    def rand_io_val(self):
        return random.choice([0,1])

uvm_object_utils(gpio8_write_datao_seq)