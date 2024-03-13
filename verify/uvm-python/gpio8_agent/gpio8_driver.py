from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info, uvm_warning
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM
from cocotb.triggers import Timer, ClockCycles, FallingEdge, Event, RisingEdge, First
from gpio8_item.gpio8_item import gpio8_item
import cocotb
import random
from EF_UVM.ip_env.ip_agent.ip_driver import ip_driver


class gpio8_driver(ip_driver):
    def __init__(self, name="gpio8_driver", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def run_phase(self, phase):
        uvm_info(self.tag, "run_phase started", UVM_LOW)
        self.vif.io_in.value = 0
        while True:
            await self.drive_delay()
            tr = []
            await self.seq_item_port.get_next_item(tr)
            await self.drive_delay()
            tr = tr[0]
            uvm_info(self.tag, f"recieved transaction {tr.convert2string()}" , UVM_LOW)
            mask = 0
            for i in range (8):
                if (tr.gpios[f"gpio{i}"].dir) == "input":
                    if tr.gpios[f"gpio{i}"].val:
                        mask |= 1 << i  # Create a mask
            self.vif.io_in.value = mask
            # await NextTimeStep()
            uvm_info(self.tag, f"mask = {mask}, driving io_in to  {self.vif.io_in.value}" , UVM_LOW)
            self.seq_item_port.item_done()

    async def drive_delay(self):
        await RisingEdge(self.vif.CLK)
    
uvm_component_utils(gpio8_driver)
