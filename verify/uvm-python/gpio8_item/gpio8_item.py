from uvm.seq.uvm_sequence_item import UVMSequenceItem
from uvm.macros import uvm_object_utils_begin, uvm_object_utils_end, uvm_field_int, uvm_object_utils, uvm_error, uvm_info
from uvm.base.uvm_object_globals import UVM_ALL_ON, UVM_NOPACK, UVM_HIGH, UVM_MEDIUM
from uvm.base.sv import sv
from EF_UVM.ip_env.ip_item import ip_item

class gpio8_item(ip_item):
    def __init__(self, name="gpio8_item"):
        super().__init__(name)
        self.gpios = {"gpio0": GPIO_Bit('input',0), "gpio1": GPIO_Bit('input',0), "gpio2": GPIO_Bit('input',0), "gpio3": GPIO_Bit('input',0), "gpio4": GPIO_Bit('input',0), "gpio5": GPIO_Bit('input',0), "gpio6": GPIO_Bit('input',0), "gpio7": GPIO_Bit('input',0)}

    def convert2string(self):
        return sv.sformatf(" GPIOs = %s", self.gpios)

    def do_compare(self, tr):
        uvm_info(self.tag, "Comparing " + self.convert2string() + " with " + tr.convert2string(), UVM_MEDIUM)
        is_matching = True
        for i in range(8):
            if (self.gpios[f"gpio{i}"].dir == tr.gpios[f"gpio{i}"].dir) and (self.gpios[f"gpio{i}"].val == tr.gpios[f"gpio{i}"].val):
                is_matching = True
            else:
                is_matching = False
                return False 

        return is_matching
    
    def copy(self, tr):
        for i in range(8):
            tr.gpios[f"gpio{i}"].dir = self.gpios[f"gpio{i}"].dir
            tr.gpios[f"gpio{i}"].val = self.gpios[f"gpio{i}"].val
        return tr

class GPIO_Bit():
    def __init__(self, dir, val):
        self.dir = dir
        self.val = val
    
    def __repr__(self):
        return f"{self.dir}({self.val})"

uvm_object_utils(gpio8_item)
