from uvm.base.uvm_component import UVMComponent
from uvm.macros import uvm_component_utils
from uvm.tlm1.uvm_analysis_port import UVMAnalysisImp
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM 
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.tlm1.uvm_analysis_port import UVMAnalysisExport
import cocotb
from cocotb.triggers import Timer, ClockCycles, FallingEdge, Event, RisingEdge, Combine, First
from gpio8_item.gpio8_item import gpio8_item
from EF_UVM.ref_model.ref_model import ref_model
from EF_UVM.bus_env.bus_item import bus_item, bus_irq_item



class gpio8_ref_model(ref_model):
    """
    The reference model is a crucial element within the top-level verification environment, designed to validate the functionality and performance of both the IP (Intellectual Property) and the bus system. Its primary role is to act as a representative or mimic of the actual hardware components, including the IP and the bus. Key features and functions of the reference model include:
    1) Input Simulation: The reference model is capable of receiving the same inputs that would be provided to the actual IP and bus via connection with the monitors of the bus and IP.
    2) Functional Emulation: It emulates the behavior and responses of the IP and bus under test. By replicating the operational characteristics of these components, the reference model serves as a benchmark for expected performance and behavior.
    3) Output Generation: Upon receiving inputs, the reference model processes them in a manner akin to the real hardware, subsequently generating expected outputs. These outputs are essential for comparison in the verification process.
    4) Interface with Scoreboard: The outputs from the reference model, representing the expected results, are forwarded to the scoreboard. The scoreboard then compares these expected results with the actual outputs from the IP and bus for verification.
    5)Register Abstraction Layer (RAL) Integration: The reference model includes a RAL model that mirrors the register values of the RTL, ensuring synchronization between expected and actual register states. This model facilitates register-level tests and error detection, offering accessible and up-to-date register values for other verification components. It enhances the automation and coverage of register testing, playing a vital role in ensuring the accuracy and comprehensiveness of the verification process.
    """
    def __init__(self, name="gpio8_ref_model", parent=None):
        super().__init__(name, parent)
        self.tag = name
        self.prev_td_in = gpio8_item.type_id.create("prev_td", self)
        self.td = gpio8_item.type_id.create("td", self)
        self.first_tr = True
        self.ris_reg = 0 
        self.mis_reg = 0
        self.irq = 0
        self.mis_changed = Event()
        self.icr_changed = Event()

    def build_phase(self, phase):
        super().build_phase(phase)
        # Here adding any initialize for user classes for the model

    async def run_phase(self, phase):
        super().run_phase(phase)
        uvm_info(self.tag, "run phase started", UVM_LOW)
        send_irq_tr = await cocotb.start (self.send_irq_tr())
        update_ris = await cocotb.start (self.update_ris())

    def write_bus(self, tr):
        # Called when new transaction is received from the bus monitor
        uvm_info(self.tag, " write: " + tr.convert2string(), UVM_HIGH)
        if tr.kind == bus_item.RESET:
            self.bus_bus_export.write(tr)
            uvm_info("vip", "reset from the vip", UVM_LOW)
            return
        if tr.kind == bus_item.WRITE:
            self.regs.write_reg_value(tr.addr, tr.data)
            self.bus_bus_export.write(tr)
            if tr.addr == self.regs.reg_name_to_address["icr"] and tr.data != 0:
                self.icr_changed.set()
        elif tr.kind == bus_item.READ:
            data = self.regs.read_reg_value(tr.addr)
            td = tr.do_clone()
            td.data = data
            self.bus_bus_export.write(td)

    def write_ip(self, tr):
        uvm_info(self.tag, "ip  write: " + tr.convert2string(), UVM_HIGH)
        # Called when new transaction is received from the ip monitor
        # td = gpio8_item.type_id.create("td", self)
        self.td.gpios = self.get_gpios_item(tr)
        if self.first_tr:
            self.update_interrupts()
            self.first_tr = False
        else:
            self.update_interrupts()
        for i in range(8):
            if(self.td.gpios[f"gpio{i}"].dir == "input"):
                self.prev_td_in.gpios[f"gpio{i}"].dir = "input"
                self.prev_td_in.gpios[f"gpio{i}"].val = self.td.gpios[f"gpio{i}"].val
            else:
                self.prev_td_in.gpios[f"gpio{i}"].dir = "input"
                self.prev_td_in.gpios[f"gpio{i}"].val = 0
        self.ip_export.write(self.td)
    

    def get_gpios_item (self, tr):
        direction = self.regs.read_reg_value("DIR")
        gpios_datao = self.regs.read_reg_value("DATAO")
        uvm_info(self.tag, f"in ref_model item creation direction = {direction}, gpios_datao= {gpios_datao}", UVM_LOW)
        gpios_datai = 0
        for i in range (8):
            self.td.gpios[f"gpio{i}"].dir = "output" if (direction >> i) & 0b1 else "input"
            if(self.td.gpios[f"gpio{i}"].dir == "output"):
                self.td.gpios[f"gpio{i}"].val = (gpios_datao >> i) & 0b1
                # td.gpios[f"gpio{i}"].val = 0
            else:
                io_in_val =  tr.gpios[f"gpio{i}"].val
                if io_in_val != 'z':
                    self.td.gpios[f"gpio{i}"].val = io_in_val
                    gpios_datai |= io_in_val << i
                else:
                    gpios_datai = 0 
        self.regs.write_reg_value("DATAI", gpios_datai, force_write=True)
        return self.td.gpios
    

    def update_interrupts(self):
        uvm_info(self.tag, "calculate ris previous td = " + self.prev_td_in.convert2string(), UVM_LOW)
        uvm_info(self.tag, "calculate ris td = " + self.td.convert2string(), UVM_LOW)
        for i in range(8):
        # check what irqs should be triggered
            current_val = self.td.gpios[f"gpio{i}"].val if self.td.gpios[f"gpio{i}"].dir == "input" else 0 
            prev_val = self.prev_td_in.gpios[f"gpio{i}"].val

            if (current_val): # current gpio is high
                self.ris_reg |= 1 << i
                if (not self.first_tr):                                                                         
                    if (prev_val==0): # rising edge (from low to high)
                        self.ris_reg |= 1 << (i+16)

            else:   # current gpio is low
                self.ris_reg |= 1 << (i+8)
                if (not self.first_tr):   
                    if (prev_val==1): # falling edge (from high to low)
                        self.ris_reg |= 1 << (i+24)
        
        self.regs.write_reg_value("ris", self.ris_reg, force_write=True)
        im_reg = self.regs.read_reg_value("im")
        mis_reg_new = self.ris_reg & im_reg
        uvm_info(self.tag, f" ref_model new tr :  im =  {im_reg:X}, ris =  {self.ris_reg:X}, mis = {mis_reg_new:X}", UVM_LOW)
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
            
            # recheck for high and low interrupts because they might be fired again right after clearing without getting a new tr
            for i in range(8):
                current_val = self.td.gpios[f"gpio{i}"].val if self.td.gpios[f"gpio{i}"].dir == "input" else 0 
                if (current_val): # current gpio is high
                    self.ris_reg |= 1 << i
                else:   # current gpio is low
                    self.ris_reg |= 1 << (i+8)
        
            self.regs.write_reg_value("ris", self.ris_reg, force_write=True)
            im_reg = self.regs.read_reg_value("im")
            mis_reg_new = self.ris_reg & im_reg
            uvm_info(self.tag, f" ref_model update ris:  im =  {im_reg:X}, ris =  {self.ris_reg:X}, mis = {mis_reg_new:X}", UVM_LOW)
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
