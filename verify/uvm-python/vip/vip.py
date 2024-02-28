from uvm.base.uvm_component import UVMComponent
from uvm.macros import uvm_component_utils
from uvm.tlm1.uvm_analysis_port import UVMAnalysisImp
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.tlm1.uvm_analysis_port import UVMAnalysisExport
from EF_UVM.vip.vip import VIP
from EF_UVM.wrapper_env.wrapper_item import wrapper_bus_item
from gpio8_item.gpio8_item import gpio8_item
from EF_UVM.ip_env.ip_agent.ip_monitor import ip_monitor
from cocotb.triggers import Timer, ClockCycles, FallingEdge, Event, RisingEdge, Combine, First
import cocotb


class gpio8_VIP(VIP):
    def __init__(self, name="gpio8_VIP", parent=None):
        super().__init__(name, parent)

    def build_phase(self, phase):
        super().build_phase(phase)
        arr = []
        if (not UVMConfigDb.get(self, "", "ip_if", arr)):
            uvm_fatal(self.tag, "No interface specified for self driver instance")
        else:
            self.vif = arr[0]
        arr = []
        if (not UVMConfigDb.get(self, "", "wrapper_regs", arr)):
            uvm_fatal(self.tag, "No json file wrapper regs")
        else:
            self.regs = arr[0]
        self.bus_write_event = Event("bus_write_event")
        self.clock_period = 10

    async def run_phase(self, phase):
        super().run_phase(phase)
        uvm_info(self.tag, "run phase started", UVM_LOW)
        # while True:
        # await self.gpio8()

    def write_bus(self, tr):
        uvm_info(self.tag, "Vip write: " + tr.convert2string(), UVM_HIGH)
        if tr.reset:
            self.wrapper_bus_export.write(tr)
            return
        if tr.kind == wrapper_bus_item.WRITE:
            self.bus_write_event.set()
            self.regs.write_reg_value(tr.addr, tr.data)
            self.wrapper_bus_export.write(tr)
        elif tr.kind == wrapper_bus_item.READ:
            data = self.regs.read_reg_value(tr.addr)
            td = tr.do_clone()
            td.data = data
            self.wrapper_bus_export.write(td)
        self.bus_write_event.clear()

    def write_ip(self, tr):
        uvm_info(self.tag, "ip Vip write: " + tr.convert2string(), UVM_HIGH)
        # when monitor detect patterns the vip should also send pattern
        td = gpio8_item.type_id.create("td", self)
        td.gpios = self.get_gpios_item(td, tr)
        self.ip_export.write(td)
    

    def get_gpios_item (self, td, tr):
        direction = self.regs.read_reg_value("DIR")
        gpios_datao = self.regs.read_reg_value("DATAO")
        uvm_info(self.tag, f"in vip item creation direction = {direction}, gpios_datao= {gpios_datao}", UVM_LOW)
        gpios_datai = 0
        for i in range (8):
            td.gpios[f"gpio{i}"].dir = "output" if (direction >> i) & 0b1 else "input"
            if(td.gpios[f"gpio{i}"].dir == "output"):
                td.gpios[f"gpio{i}"].val = (gpios_datao >> i) & 0b1
                # td.gpios[f"gpio{i}"].val = 0
            else:
                io_in_val =  tr.gpios[f"gpio{i}"].val
                if io_in_val != 'z':
                    td.gpios[f"gpio{i}"].val = io_in_val
                    gpios_datai |= io_in_val << i
                else:
                    gpios_datai = 0 
        self.regs.write_reg_value("DATAI", gpios_datai, force_write=True)
        return td.gpios



uvm_component_utils(gpio8_VIP)
