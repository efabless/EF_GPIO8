from uvm.base.uvm_component import UVMComponent
from uvm.macros import uvm_component_utils
from uvm.tlm1.uvm_analysis_port import UVMAnalysisImp
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.tlm1.uvm_analysis_port import UVMAnalysisExport
from EF_UVM.ref_model.ref_model import ref_model
from EF_UVM.bus_env.bus_item import bus_irq_item
from EF_UVM.bus_env.bus_item import bus_item
from gpio8_item.gpio8_item import gpio8_item
from EF_UVM.ip_env.ip_agent.ip_monitor import ip_monitor
from cocotb.triggers import Timer, ClockCycles, FallingEdge, Event, RisingEdge, Combine, First
import cocotb


class gpio8_ref_model(ref_model):
    def __init__(self, name="gpio8_ref_model", parent=None):
        super().__init__(name, parent)
        self.prev_td = gpio8_item.type_id.create("td", self)
        self.first_tr = True
        self.ris_reg = 0 
        self.mis_reg = 0
        self.irq = 0
        self.mis_changed = Event()
        self.icr_changed = Event()

    def build_phase(self, phase):
        super().build_phase(phase)
        arr = []
        if (not UVMConfigDb.get(self, "", "ip_if", arr)):
            uvm_fatal(self.tag, "No interface specified for self driver instance")
        else:
            self.vif = arr[0]
        arr = []
        if (not UVMConfigDb.get(self, "", "bus_regs", arr)):
            uvm_fatal(self.tag, "No json file wrapper regs")
        else:
            self.regs = arr[0]
        self.bus_write_event = Event("bus_write_event")
        self.clock_period = 10



    async def run_phase(self, phase):
        super().run_phase(phase)
        uvm_info(self.tag, "run phase started", UVM_LOW)
        send_irq_tr = await cocotb.start (self.send_irq_tr())
        update_ris = await cocotb.start (self.update_ris())

        # await Combine(update_ris, send_irq_tr)


    def write_bus(self, tr):
        uvm_info(self.tag, "ref_model write: " + tr.convert2string(), UVM_HIGH)
        if tr.reset:
            self.bus_bus_export.write(tr)
            return
        if tr.kind == bus_item.WRITE:
            self.bus_write_event.set()
            self.regs.write_reg_value(tr.addr, tr.data)
            self.bus_bus_export.write(tr)
            if tr.addr == self.regs.reg_name_to_address["icr"] and tr.data != 0:
                self.icr_changed.set()
                # uvm_info(self.tag, "setting icr changed event", UVM_LOW)
        elif tr.kind == bus_item.READ:
            data = self.regs.read_reg_value(tr.addr)
            td = tr.do_clone()
            td.data = data
            self.bus_bus_export.write(td)
        self.bus_write_event.clear()

    def write_ip(self, tr):
        uvm_info(self.tag, "ip ref_model write: " + tr.convert2string(), UVM_HIGH)
        # when monitor detect patterns the ref_model should also send pattern
        td = gpio8_item.type_id.create("td", self)
        td.gpios = self.get_gpios_item(td, tr)
        if self.first_tr:
            self.update_interrupts(td)
            self.first_tr = False
        else:
            self.update_interrupts(td)
        self.prev_td = td.copy(self.prev_td)
        self.ip_export.write(td)
    
    # def write_ip_irq(self, tr):
    #     uvm_info(self.tag, "ref_model recieved irq tr from monitor" + tr.convert2string(), UVM_MEDIUM)
    #     # when irq_monitor detect firing interrupt the ref_model should also send an interrupt to scoreboard
    #     # td = self.get_irq_item()
    #     # self.bus_irq_export.write(td)

    def get_gpios_item (self, td, tr):
        direction = self.regs.read_reg_value("DIR")
        gpios_datao = self.regs.read_reg_value("DATAO")
        uvm_info(self.tag, f"in ref_model item creation direction = {direction}, gpios_datao= {gpios_datao}", UVM_LOW)
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
    

    def update_interrupts(self, td):
        uvm_info(self.tag, "calculate ris td = " + td.convert2string(), UVM_MEDIUM)
        uvm_info(self.tag, "calculate ris previous td = " + self.prev_td.convert2string(), UVM_MEDIUM)
        for i in range(8):
        # check what irqs should be triggered
            if (td.gpios[f"gpio{i}"].dir == "input"):  
                if (td.gpios[f"gpio{i}"].val): # gpio is high
                    self.ris_reg |= 1 << i
                    # uvm_info(self.tag, f"gpio{i}: high", UVM_LOW)
                    if (not self.first_tr):                                                                         
                        if (self.prev_td.gpios[f"gpio{i}"].val==0): # rising edge (from low to high)
                            self.ris_reg |= 1 << (i+16)
                            # uvm_info(self.tag, f"gpio{i}: rising edge low to high", UVM_LOW)

                else:
                    # uvm_info(self.tag, f"gpio{i}: low", UVM_LOW)                       # gpio is low
                    self.ris_reg |= 1 << (i+8)
                    if (not self.first_tr):   
                        if (self.prev_td.gpios[f"gpio{i}"].val): # falling edge (from high to low)
                            self.ris_reg |= 1 << (i+24)
                            # uvm_info(self.tag, f"gpio{i}: falling edge high to low", UVM_LOW)

                # uvm_info(self.tag, f" ref_model calculated RIS {self.ris_reg:X}", UVM_LOW)
                # check for bits in icr to clear if 1
                
            
        
        # uvm_info(self.tag, f" ref_model calculated RIS without clearing icr {self.ris_reg:X}", UVM_LOW)
        self.regs.write_reg_value("ris", self.ris_reg, force_write=True)
        im_reg = self.regs.read_reg_value("im")
        mis_reg_new = self.ris_reg & im_reg
        uvm_info(self.tag, f" ref_model im =  {im_reg:X}, ris =  {self.ris_reg:X}, mis = {mis_reg_new:X}", UVM_LOW)
        if mis_reg_new != self.mis_reg:
            self.mis_changed.set()
        self.mis_reg = mis_reg_new
        self.regs.write_reg_value("mis", self.mis_reg, force_write=True)
        
        # function  executed while true  --> check on ic , calculate ris , write it , check on im and update mis 
        

    async def update_ris (self):
        while (True):
            await self.icr_changed.wait()
            icr_reg = self.regs.read_reg_value("icr")
            # uvm_info(self.tag, f" ref_model icr changed to =  {icr_reg:X}", UVM_LOW)
            mask = ~icr_reg
            self.ris_reg = self.ris_reg & mask
            # uvm_info(self.tag, f" ref_model updated RIS after clearing icr {self.ris_reg:X}", UVM_LOW)
            self.regs.write_reg_value("ris", self.ris_reg, force_write=True)
            im_reg = self.regs.read_reg_value("im")
            mis_reg_new = self.ris_reg & im_reg
            # uvm_info(self.tag, f" ref_model im =  {im_reg:X}, ris =  {self.ris_reg:X}, mis = {mis_reg_new:X}", UVM_LOW)
            if mis_reg_new != self.mis_reg:
                self.mis_changed.set()
            self.mis_reg = mis_reg_new
            self.regs.write_reg_value("mis", self.mis_reg, force_write=True)
            self.regs.write_reg_value("icr", 0, force_write=True)  # clear icr register 
            self.icr_changed.clear()
    
    async def send_irq_tr(self):
        while (True):
            await self.mis_changed.wait()
            irq_new = 1 if self.mis_reg else 0                                        
            if irq_new and not self.irq: # irq changed from low to high 
                # send a tr irq
                self.irq = 1 
                tr = bus_irq_item.type_id.create("tr", self)
                tr.trg_irq = 1
                # uvm_info(self.tag, "ref_model set interrupt = " + tr.convert2string(), UVM_MEDIUM)                       
                self.bus_irq_export.write(tr)
            elif not irq_new and self.irq: # irq changed from high to low 
                # send a tr irq
                self.irq = 0
                tr = bus_irq_item.type_id.create("tr", self)
                tr.trg_irq = 0
                # uvm_info(self.tag, "ref_model clear interrupt = " + tr.convert2string(), UVM_MEDIUM)
                self.bus_irq_export.write(tr)
            
            self.mis_changed.clear()
    



uvm_component_utils(gpio8_ref_model)
