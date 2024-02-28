from uvm.macros.uvm_message_defines import uvm_info
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW
from cocotb_coverage.coverage import CoverPoint, CoverCross
from uvm.macros import uvm_component_utils
from gpio8_item.gpio8_item import gpio8_item


class gpio8_cov_groups():
    def __init__(self, hierarchy, regs) -> None:
        self.hierarchy = hierarchy
        self.regs = regs
        self.ios_coverage = self.ios_cov()
        self.ip_cov(None, do_sampling=False)

    

    def ip_cov(self, tr, do_sampling=True):
        @self.apply_decorators(decorators=self.ios_coverage)
        def sample(tr):
            uvm_info("coverage_ip", f"tr = {tr.gpios['gpio0'].dir} type {type(tr.gpios['gpio0'].val)}", UVM_LOW)
        if do_sampling:
            sample(tr)

    def ios_cov(self):
        cov_points = []
        for i in range(8):
            cov_points.append(CoverPoint(
                f"{self.hierarchy}. GPIO {i}.Input",
                xf=lambda tr, ii=i: (tr.gpios[f"gpio{ii}"].dir == "input", tr.gpios[f"gpio{ii}"].val),
                bins=[ (True, 1), (True, 0) ],
                bins_labels=[("Input", "High") , ("Input", "Low")],
                # at_least=3,
            ))
            cov_points.append(CoverPoint(
                f"{self.hierarchy}. GPIO {i}.Output",
                xf=lambda tr, ii=i: (tr.gpios[f"gpio{ii}"].dir == "output", tr.gpios[f"gpio{ii}"].val),
                bins=[ (True, 1), (True, 0) ],
                bins_labels=[("Output", "High") , ("Output", "Low")],
                # at_least=3,
            ))
        return cov_points

    def apply_decorators(self, decorators):
        def decorator_wrapper(func):
            for decorator in decorators:
                func = decorator(func)
            return func
        return decorator_wrapper


       # @CoverPoint(
        # f"{self.hierarchy}. GPIO {0}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{0}"].dir == "input", tr.gpios[f"gpio{0}"].val),
        # bins=[ (True, 1), (True, 0) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )
        # @CoverPoint(
        # f"{self.hierarchy}. GPIO {1}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{1}"].dir == "input", tr.gpios[f"gpio{1}"].val==1),
        # bins=[ (True, True), (True, False) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )
        # @CoverPoint(
        # f"{self.hierarchy}. GPIO {2}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{2}"].dir == "input", tr.gpios[f"gpio{2}"].val==1),
        # bins=[ (True, True), (True, False) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )
        # @CoverPoint(
        # f"{self.hierarchy}. GPIO {3}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{3}"].dir == "input", tr.gpios[f"gpio{3}"].val==1),
        # bins=[ (True, True), (True, False) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )
        # @CoverPoint(
        # f"{self.hierarchy}. GPIO {4}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{4}"].dir == "input", tr.gpios[f"gpio{4}"].val==1),
        # bins=[ (True, True), (True, False) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )
        # @CoverPoint(
        # f"{self.hierarchy}. GPIO {5}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{5}"].dir == "input", tr.gpios[f"gpio{5}"].val==1),
        # bins=[ (True, True), (True, False) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )
        # @CoverPoint(
        # f"{self.hierarchy}. GPIO {6}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{6}"].dir == "input", tr.gpios[f"gpio{6}"].val==1),
        # bins=[ (True, True), (True, False) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )
        # @CoverPoint(
        # f"{self.hierarchy}. GPIO {7}.Input",
        # xf=lambda tr: (tr.gpios[f"gpio{7}"].dir == "input", tr.gpios[f"gpio{7}"].val==1),
        # bins=[ (True, True), (True, False) ],
        # bins_labels=[("Input", "High") , ("Input", "Low")],
        # # at_least=3,
        # )