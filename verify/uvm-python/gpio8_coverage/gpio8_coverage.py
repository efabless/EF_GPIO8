from uvm.base.uvm_component import UVMComponent
from uvm.macros import uvm_component_utils
from uvm.tlm1.uvm_analysis_port import UVMAnalysisImp
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW 
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.macros.uvm_tlm_defines import uvm_analysis_imp_decl
from gpio8_coverage.gpio8_cov_groups import gpio8_cov_groups
from EF_UVM.ip_env.ip_coverage.ip_coverage import ip_coverage


class gpio8_coverage(ip_coverage):
    """
    component that initialize the coverage groups and control when to sample the data.
    """
    def __init__(self, name="gpio8_coverage", parent=None):
        super().__init__(name, parent)

    def build_phase(self, phase):
        super().build_phase(phase)
        
        regs_arr = []
        if (not UVMConfigDb.get(self, "", "bus_regs", regs_arr)):
            uvm_fatal(self.tag, "No json file wrapper regs")
        else:
            self.regs = regs_arr[0]
        self.cov_groups = gpio8_cov_groups("top.ip", self.regs)

    def write(self, tr):
        self.cov_groups.ip_cov(tr)

uvm_component_utils(gpio8_coverage)
