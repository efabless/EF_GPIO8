from EF_UVM.ip_env.ip_logger.ip_logger import ip_logger
import cocotb 
from uvm.macros import uvm_component_utils, uvm_fatal
from gpio8_item.gpio8_item import gpio8_item


class gpio8_logger(ip_logger):
    def __init__(self, name="gpio8_logger", parent=None):
        super().__init__(name, parent)
        self.header = ['Time (ns)', 'GPIO0', 'GPIO1', 'GPIO2', 'GPIO3', 'GPIO4', 'GPIO5', 'GPIO6', 'GPIO7']
        self.col_widths = [10]* len(self.header)

    def logger_formatter(self, transaction):
        sim_time = f"{cocotb.utils.get_sim_time(units='ns')} ns"
        if type(transaction) is gpio8_item:
            gpios_list = []
            for i in range (8):
                gpios_list.append(f'{transaction.gpios[f"gpio{i}"]}')
            return [sim_time] + gpios_list


uvm_component_utils(gpio8_logger)
