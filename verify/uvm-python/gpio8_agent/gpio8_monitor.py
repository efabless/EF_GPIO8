from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info, uvm_error, uvm_warning
from uvm.comps.uvm_monitor import UVMMonitor
from uvm.tlm1.uvm_analysis_port import UVMAnalysisPort
from uvm.base.uvm_config_db import UVMConfigDb
from cocotb.triggers import Timer, ClockCycles, FallingEdge, Event, RisingEdge, Combine, First, Edge
from gpio8_item.gpio8_item import gpio8_item
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM
import cocotb
import math
from EF_UVM.ip_env.ip_agent.ip_monitor import ip_monitor


class gpio8_monitor(ip_monitor):
    def __init__(self, name="gpio8_monitor", parent=None):
        super().__init__(name, parent)

    async def run_phase(self, phase):
        await self.sample_gpios()
            
    async def sample_gpios(self):
        await RisingEdge (self.vif.RESETn)
        while(True):
            tr = self.set_gpio()
            uvm_info(self.tag, "sampled GPIO value: " + tr.convert2string(), UVM_LOW)
            await RisingEdge(self.vif.CLK) # just to sync the vip with the monitor
            self.monitor_port.write(tr)
            await self.wait_gpio_change()
    
    async def wait_gpio_change(self):
        io_in =  Edge(self.vif.io_in)
        io_out = Edge(self.vif.io_out)
        io_oe =  Edge(self.vif.io_oe)
        await First (io_in, io_out, io_oe)
        uvm_info(self.tag, f"io change detected: io_oe = {self.vif.io_oe} , io_out = {self.vif.io_out}, io_in = {self.vif.io_in} " , UVM_LOW)
        return

    
    def set_gpio(self):
        tr = gpio8_item.type_id.create("tr", self)
        for i in range(8):
            direction = "output" if ((self.vif.io_oe.value.integer >> i ) & 0b1 ) else "input"
            tr.gpios[f"gpio{i}"].dir = direction
            if direction == "output":
                tr.gpios[f"gpio{i}"].val = (self.vif.io_out.value.integer >> i) & 0b1
                # uvm_info(self.tag, f"out value for gpio {i} = {tr.gpios[f'gpio{i}'].val}" , UVM_LOW)
            else:
                try:
                    tr.gpios[f"gpio{i}"].val = (self.vif.io_in.value.integer >> i) & 0b1
                except ValueError:
                    tr.gpios[f"gpio{i}"].val = self.vif.io_in.value.binstr[i]
                    pass
        return tr


uvm_component_utils(gpio8_monitor)
