from uvm.macros import uvm_object_utils_begin, uvm_object_utils_end, uvm_field_int, uvm_object_utils, uvm_error, uvm_info
from uvm.base.uvm_object_globals import UVM_ALL_ON, UVM_NOPACK, UVM_HIGH, UVM_MEDIUM
from uvm.base.sv import sv
from EF_UVM.ip_env.ip_item import ip_item
from collections import namedtuple
import random

class gpio8_item(ip_item):


    def __init__(self, name="gpio8_item"):
        super().__init__(name)
        self.gpios = {"gpio0": GPIO_Bit('input',0), "gpio1": GPIO_Bit('input',0), "gpio2": GPIO_Bit('input',0), "gpio3": GPIO_Bit('input',0), "gpio4": GPIO_Bit('input',0), "gpio5": GPIO_Bit('input',0), "gpio6": GPIO_Bit('input',0), "gpio7": GPIO_Bit('input',0)}

    def convert2string(self):
        return sv.sformatf(" GPIOs = %s", self.gpios)

    def do_compare(self, tr):
        uvm_info(self.tag, "Comparing " + self.convert2string() + " with " + tr.convert2string(), UVM_MEDIUM)
        # uvm_info(self.tag, " transaction in compare " + tr.convert2string(), UVM_LOW)
        is_matching = True
        # uvm_info("ay 7aga", f"type of gpio {self.gpios} {type(self.gpios)}", UVM_MEDIUM)
        # value = tr.gpios["gpio0"]
        for i in range(8):
            if (self.gpios[f"gpio{i}"].dir == tr.gpios[f"gpio{i}"].dir) and (self.gpios[f"gpio{i}"].val == tr.gpios[f"gpio{i}"].val):
                is_matching = True
            else:
                is_matching = False
                exit 

        return is_matching
        # return self.gpios == tr.gpios 

    
    
    def set_or_randomize_gpios(self, gpios_dir=None, gpios_val=None):

        if(gpios_dir is None):
            gpios_dir = random.choice(range(0, 0xFF))
        
        for i in range(8):
            self.gpios[f"gpio{i}"].dir = (gpios_dir >> i ) & 0b1

        if(gpios_val is None):
            gpios_val = random.choice(range(0, 0xFF))
        
        for i in range(8):
            self.gpios[f"gpio{i}"].val = (gpios_val >> i ) & 0b1

        gpios_datai = 0
        gpios_datao = 0

        for i in range (8):
            bit_dir = (gpios_dir >> i ) & 0b1
            bit_val = (gpios_val >> i ) & 0b1
            if(bit_dir):
                if bit_val:
                    gpios_datao |= (1 << i)
            else:
                if bit_val:
                    gpios_datai |= (1 << i)
        
        return gpios_dir, gpios_datai , gpios_datao

        # def rand_dir():
        #     return random.choice(['input', 'output'])

        # def rand_val():
        #     return random.choice([0,1])

        # def get_gpio_dir (gpio_num):
        #     return "output" if ((direction >> gpio_num) & 0b1) else "input"
        
        # def get_gpio_val(value, io_num):
        #     return (value >> io_num) & 0b1
        

        # if (direction is None):
        #     direction = random.choice(range(0, 0xFF))
        #     self.gpios = {"gpio0": GPIO_Bit( rand_dir(), rand_val()), "gpio1": GPIO_Bit( rand_dir(), rand_val()), "gpio2": GPIO_Bit( rand_dir(), rand_val()), "gpio3": GPIO_Bit( rand_dir(), rand_val()), "gpio4": GPIO_Bit( rand_dir(), rand_val()), "gpio5": GPIO_Bit( rand_dir(), rand_val()), "gpio6": GPIO_Bit( rand_dir(), rand_val()), "gpio7": GPIO_Bit( rand_dir(), rand_val())} 
        # else:
        #     self.gpios = {"gpio0": GPIO_Bit( get_gpio_dir(0), get_gpio_val(gpios_value, 0)), "gpio1": GPIO_Bit( get_gpio_dir(1), get_gpio_val(gpios_value, 1)), "gpio2": GPIO_Bit( get_gpio_dir(2), get_gpio_val(gpios_value, 1)), "gpio3": GPIO_Bit( get_gpio_dir(3), get_gpio_val(gpios_value, 3)), "gpio4": GPIO_Bit( get_gpio_dir(4), get_gpio_val(gpios_value, 4)), "gpio5": GPIO_Bit( get_gpio_dir(5), get_gpio_val(gpios_value, 5)), "gpio6": GPIO_Bit( get_gpio_dir(6), get_gpio_val(gpios_value, 6)), "gpio7": GPIO_Bit( get_gpio_dir(7), get_gpio_val(gpios_value, 7))} 

        
        

        


    def set_gpios_dir(self, direction):
        for i in range(8):
            io_dir = (direction >> i ) & 0b1
            self.gpios[f"gpio{i}"].dir = io_dir
    
    def set_gpios_val(self, value):
        for i in range(8):
            io_val = (value >> i ) & 0b1
            self.gpios[f"gpio{i}"].val = io_val
    





class GPIO_Bit():
    def __init__(self, dir, val):
        self.dir = dir
        self.val = val
    
    def __repr__(self):
        return f"{self.dir}({self.val})"


uvm_object_utils(gpio8_item)

