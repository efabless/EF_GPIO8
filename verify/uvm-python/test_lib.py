import cocotb
import random
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.base.uvm_object_globals import UVM_LOW
from uvm.base.uvm_globals import run_test
from gpio8_interface.gpio8_if import gpio8_if
from EF_UVM.bus_env.bus_interface.bus_if import (
    bus_apb_if,
    bus_irq_if,
    bus_ahb_if,
    bus_wb_if,
)
from cocotb_coverage.coverage import coverage_db
from cocotb.triggers import Event, First, Timer
from EF_UVM.bus_env.bus_regs import bus_regs
from uvm.base import UVMRoot
from EF_UVM.base_test import base_test

# seqences import
from EF_UVM.bus_env.bus_seq_lib.write_read_regs import write_read_regs
from gpio8_seq_lib.gpio8_read_datai_seq import gpio8_read_datai_seq
from gpio8_seq_lib.gpio8_write_dir_seq import gpio8_write_dir_seq
from gpio8_seq_lib.gpio8_write_datao_seq import gpio8_write_datao_seq
from gpio8_seq_lib.gpio8_set_io_in_seq import gpio8_set_io_in_seq
from gpio8_seq_lib.gpio8_write_im_seq import gpio8_write_im_seq
from gpio8_seq_lib.gpio8_write_ic_seq import gpio8_write_ic_seq
from gpio8_seq_lib.gpio8_read_ris_seq import gpio8_read_ris_seq
from gpio8_seq_lib.gpio8_read_mis_seq import gpio8_read_mis_seq
from gpio8_seq_lib.gpio8_send_nop_seq import gpio8_send_nop_seq


# override classes
from EF_UVM.ip_env.ip_agent.ip_driver import ip_driver
from gpio8_agent.gpio8_driver import gpio8_driver
from EF_UVM.ip_env.ip_agent.ip_monitor import ip_monitor
from gpio8_agent.gpio8_monitor import gpio8_monitor
from EF_UVM.ref_model.ref_model import ref_model
from gpio8_ref_model.gpio8_ref_model import gpio8_ref_model
from EF_UVM.ip_env.ip_coverage.ip_coverage import ip_coverage
from gpio8_coverage.gpio8_coverage import gpio8_coverage
from EF_UVM.ip_env.ip_logger.ip_logger import ip_logger
from gpio8_logger.gpio8_logger import gpio8_logger


@cocotb.test()
async def module_top(dut):
    # profiler = cProfile.Profile()
    # profiler.enable()
    BUS_TYPE = cocotb.plusargs["BUS_TYPE"]
    pif = gpio8_if(dut)
    if BUS_TYPE == "APB":
        w_if = bus_apb_if(dut)
    elif BUS_TYPE == "AHB":
        w_if = bus_ahb_if(dut)
    elif BUS_TYPE == "WISHBONE":
        w_if = bus_wb_if(dut)
    else:
        uvm_fatal("module_top", f"unknown bus type {BUS_TYPE}")
    w_irq_if = bus_irq_if(dut)
    UVMConfigDb.set(None, "*", "ip_if", pif)
    UVMConfigDb.set(None, "*", "bus_if", w_if)
    UVMConfigDb.set(None, "*", "bus_irq_if", w_irq_if)
    yaml_file = []
    UVMRoot().clp.get_arg_values("+YAML_FILE=", yaml_file)
    yaml_file = yaml_file[0]
    regs = bus_regs(yaml_file)
    UVMConfigDb.set(None, "*", "bus_regs", regs)
    UVMConfigDb.set(None, "*", "irq_exist", regs.get_irq_exist())
    UVMConfigDb.set(None, "*", "collect_coverage", True)
    UVMConfigDb.set(None, "*", "disable_logger", False)
    test_path = []
    UVMRoot().clp.get_arg_values("+TEST_PATH=", test_path)
    test_path = test_path[0]
    await run_test()
    coverage_db.export_to_yaml(filename=f"{test_path}/coverage.yalm")
    # profiler.disable()
    # profiler.dump_stats("profile_result.prof")


class gpio8_base_test(base_test):
    def __init__(self, name="gpio8_first_test", parent=None):
        BUS_TYPE = cocotb.plusargs["BUS_TYPE"]
        super().__init__(name, bus_type=BUS_TYPE, parent=parent)
        self.tag = name

    def build_phase(self, phase):
        super().build_phase(phase)
        # override
        self.set_type_override_by_type(ip_driver.get_type(), gpio8_driver.get_type())
        self.set_type_override_by_type(ip_monitor.get_type(), gpio8_monitor.get_type())
        self.set_type_override_by_type(ref_model.get_type(), gpio8_ref_model.get_type())
        self.set_type_override_by_type(
            ip_coverage.get_type(), gpio8_coverage.get_type()
        )
        self.set_type_override_by_type(ip_logger.get_type(), gpio8_logger.get_type())

    def end_of_elaboration_phase(self, phase):
        super().end_of_elaboration_phase(phase)
        self.update_min_checkers(4)

    async def delay(self, cycles=None):
        bus_gpio8_send_nop_seq = gpio8_send_nop_seq("gpio8_send_nop_seq")
        if cycles is None:
            cycles = 1
        for _ in range(cycles):
            await bus_gpio8_send_nop_seq.start(self.bus_sqr)

uvm_component_utils(gpio8_base_test)


class gpio8_all_out_test(gpio8_base_test):
    def __init__(self, name="gpio8_all_out_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")
        bus_gpio8_write_dir_seq = gpio8_write_dir_seq("gpio8_write_dir_seq")
        bus_gpio8_write_datao_seq = gpio8_write_datao_seq("gpio8_write_datao_seq")
        gpios_dir = 0xFF
        bus_gpio8_write_dir_seq.set_gpios_dir(gpios_dir)
        bus_gpio8_write_datao_seq.set_gpios_dir(gpios_dir)
        await bus_gpio8_write_dir_seq.start(self.bus_sqr)
        await bus_gpio8_write_datao_seq.start(self.bus_sqr)
        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(gpio8_all_out_test)


class gpio8_all_in_test(gpio8_base_test):
    def __init__(self, name="gpio8_all_in_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")
        bus_gpio8_write_dir_seq = gpio8_write_dir_seq("gpio8_write_dir_seq")
        ip_gpio_set_io_in_seq = gpio8_set_io_in_seq("gpio8_set_io_in_seq")
        bus_gpio8_read_datai_seq = gpio8_read_datai_seq("gpio8_read_datai_seq")
        gpios_dir = 0x00
        bus_gpio8_write_dir_seq.set_gpios_dir(gpios_dir)
        ip_gpio_set_io_in_seq.set_gpios_dir(gpios_dir)
        await bus_gpio8_write_dir_seq.start(self.bus_sqr)
        await ip_gpio_set_io_in_seq.start(self.ip_sqr)
        await bus_gpio8_read_datai_seq.start(self.bus_sqr)
        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(gpio8_all_in_test)


class gpio8_rand_test(gpio8_base_test):
    def __init__(self, name="gpio8_rand_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")
        bus_gpio8_write_dir_seq = gpio8_write_dir_seq("gpio8_write_dir_seq")
        bus_gpio8_write_datao_seq = gpio8_write_datao_seq("gpio8_write_datao_seq")
        ip_gpio_set_io_in_seq = gpio8_set_io_in_seq("gpio8_set_io_in_seq")
        bus_gpio8_read_datai_seq = gpio8_read_datai_seq("gpio8_read_datai_seq")
        bus_gpio8_read_ris_seq = gpio8_read_ris_seq("gpio8_read_ris_seq")
        bus_gpio8_write_ic_seq = gpio8_write_ic_seq("gpio8_write_ic_seq")
        bus_gpio8_write_ic_seq.set_ic(0xFFFFFFFF)

        for _ in range(70):
            rand_dir = random.choice(range(0, 0xFF))
            bus_gpio8_write_dir_seq.set_gpios_dir(rand_dir)
            bus_gpio8_write_datao_seq.set_gpios_dir(rand_dir)
            ip_gpio_set_io_in_seq.set_gpios_dir(rand_dir)
            await bus_gpio8_write_dir_seq.start(self.bus_sqr)
            await bus_gpio8_write_datao_seq.start(self.bus_sqr)
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)
            await bus_gpio8_read_ris_seq.start(
                self.bus_sqr
            )  # read ris to check that it has the correct value
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)  # clear all interrupts
            await bus_gpio8_read_datai_seq.start(self.bus_sqr)
        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(gpio8_rand_test)


class gpio8_interrupts_test(gpio8_base_test):
    def __init__(self, name="gpio8_interrupts_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")
        bus_gpio8_write_dir_seq = gpio8_write_dir_seq("gpio8_write_dir_seq")
        ip_gpio_set_io_in_seq = gpio8_set_io_in_seq("gpio8_set_io_in_seq")
        bus_gpio8_write_dir_seq.set_gpios_dir(0)  # set all IOs dir to input
        ip_gpio_set_io_in_seq.set_gpios_dir(0)
        bus_gpio8_write_im_seq = gpio8_write_im_seq("gpio8_write_im_seq")
        bus_gpio8_write_ic_seq = gpio8_write_ic_seq("gpio8_write_ic_seq")
        bus_gpio8_read_ris_seq = gpio8_read_ris_seq("gpio8_read_ris_seq")
        bus_gpio8_read_mis_seq = gpio8_read_mis_seq("gpio8_read_mis_seq")

        await bus_gpio8_write_dir_seq.start(
            self.bus_sqr
        )  # set all IOs direction to input because interrupts are for input IOs

        # IO is high
        for i in range(8):
            bus_gpio8_write_im_seq.set_im(1 << i)
            ip_gpio_set_io_in_seq.set_gpios_in(1 << i)
            bus_gpio8_write_ic_seq.set_ic(1 << i)
            await bus_gpio8_write_im_seq.start(self.bus_sqr)  # mask the interrupt
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)  # set the IO
            await bus_gpio8_read_ris_seq.start(
                self.bus_sqr
            )  # read ris to check that it has the correct value
            await bus_gpio8_read_mis_seq.start(
                self.bus_sqr
            )  # read mis to check that it has the correct value
            ip_gpio_set_io_in_seq.set_gpios_in(
                0x00
            )  # set the IOs to low (to prevent the rising of the irq again)
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)  # clear the interrupt

        # IO is low
        ip_gpio_set_io_in_seq.set_gpios_in(0xFF)  # set all IOs to low
        await ip_gpio_set_io_in_seq.start(self.ip_sqr)
        for i in range(8):
            bus_gpio8_write_im_seq.set_im(1 << (i + 8))
            ip_gpio_set_io_in_seq.set_gpios_in(~(1 << i))
            bus_gpio8_write_ic_seq.set_ic(1 << (i + 8))
            await bus_gpio8_write_im_seq.start(self.bus_sqr)  # mask the interrupt
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)  # clear IO i
            await bus_gpio8_read_ris_seq.start(
                self.bus_sqr
            )  # read ris to check that it has the correct value
            await bus_gpio8_read_mis_seq.start(
                self.bus_sqr
            )  # read mis to check that it has the correct value
            ip_gpio_set_io_in_seq.set_gpios_in(
                1 << i
            )  # set IO {i} to high (to preven the rising of the irq again)
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)
            bus_gpio8_write_ic_seq.set_ic(0xFFFFFFFF)
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)  # clear the interrupt

        # Positive Edge interrupts
        ip_gpio_set_io_in_seq.set_gpios_in(0x00)
        await ip_gpio_set_io_in_seq.start(self.ip_sqr)  # set all IOs to low
        for i in range(8):
            bus_gpio8_write_im_seq.set_im(1 << (i + 16))
            ip_gpio_set_io_in_seq.set_gpios_in(1 << i)
            bus_gpio8_write_ic_seq.set_ic(1 << (i + 16))
            await bus_gpio8_write_im_seq.start(self.bus_sqr)  # mask the interrupt
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)  # set the IO
            await bus_gpio8_read_ris_seq.start(
                self.bus_sqr
            )  # read ris to check that it has the correct value
            await bus_gpio8_read_mis_seq.start(
                self.bus_sqr
            )  # read mis to check that it has the correct value
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)  # clear the interrupt

        # Negative edge interrupts
        ip_gpio_set_io_in_seq.set_gpios_in(0xFF)
        await ip_gpio_set_io_in_seq.start(self.ip_sqr)  # set all IOs to high
        for i in range(8):
            gpios_in = 0xFF & ~(1 << i)  # set IO {i} to low (to create a negative edge)
            bus_gpio8_write_im_seq.set_im(1 << (i + 24))
            ip_gpio_set_io_in_seq.set_gpios_in(gpios_in)
            bus_gpio8_write_ic_seq.set_ic(1 << (i + 24))
            await bus_gpio8_write_im_seq.start(self.bus_sqr)  # mask the interrupt
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)  # set the IO
            await bus_gpio8_read_ris_seq.start(
                self.bus_sqr
            )  # read ris to check that it has the correct value
            await bus_gpio8_read_mis_seq.start(
                self.bus_sqr
            )  # read mis to check that it has the correct value
            bus_gpio8_write_ic_seq.set_ic(0xFFFFFFFF)
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)  # clear the interrupt

        await Timer(1000, "ns")
        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(gpio8_interrupts_test)
