from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_info, uvm_fatal
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from uvm.base import sv, UVM_HIGH, UVM_LOW
from EF_UVM.bus_env.bus_item import bus_item
from uvm.base.uvm_config_db import UVMConfigDb
import random


class gpio8_read_datai_seq(UVMSequence):

    def __init__(self, name="gpio8_read_datai_seq"):
        UVMSequence.__init__(self, name)
        self.set_automatic_phase_objection(1)
        self.req = bus_item()
        self.rsp = bus_item()
        self.tag = name
        # self.gpios_datai = gpios_datai

    async def body(self):
        # get register names/address conversion dict
        arr = []
        if (not UVMConfigDb.get(self, "", "bus_regs", arr)):
            uvm_fatal(self.tag, "No json file wrapper regs")
        else:
            adress_dict = arr[0].reg_name_to_address
       
        await uvm_do_with(self, self.req, lambda addr: addr == adress_dict["DATAI"], lambda kind: kind == bus_item.READ)


uvm_object_utils(gpio8_read_datai_seq)
