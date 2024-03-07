import cocotb
from uvm.comps import UVMTest
from uvm import UVMCoreService
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.base.uvm_printer import UVMTablePrinter
from uvm.base.sv import sv
from uvm.base.uvm_object_globals import UVM_FULL, UVM_LOW, UVM_ERROR
from uvm.base.uvm_globals import run_test
from EF_UVM.top_env import top_env
from gpio8_interface.gpio8_if import gpio8_if
from EF_UVM.bus_env.bus_interface.bus_if import bus_apb_if, bus_irq_if
from cocotb_coverage.coverage import coverage_db
from cocotb.triggers import Event, First, Timer
from EF_UVM.bus_env.bus_regs import bus_regs
from uvm.base.uvm_report_server import UVMReportServer
from uvm.base import UVMRoot
import random

# seq
from EF_UVM.bus_env.bus_seq_lib.write_read_regs import write_read_regs
from gpio8_seq_lib.gpio8_read_datai_seq import gpio8_read_datai_seq
from gpio8_seq_lib.gpio8_write_dir_seq import gpio8_write_dir_seq
from gpio8_seq_lib.gpio8_write_datao_seq import gpio8_write_datao_seq
from gpio8_seq_lib.gpio8_set_io_in_seq import gpio8_set_io_in_seq
from gpio8_seq_lib.gpio8_write_im_seq import gpio8_write_im_seq
from gpio8_seq_lib.gpio8_write_ic_seq import gpio8_write_ic_seq

# override classes
from EF_UVM.ip_env.ip_agent.ip_driver import ip_driver
from gpio8_agent.gpio8_driver import gpio8_driver
from EF_UVM.ip_env.ip_agent.ip_monitor import ip_monitor
from gpio8_agent.gpio8_monitor import gpio8_monitor
from EF_UVM.ref_model.ref_model import ref_model
from ref_model.ref_model import gpio8_ref_model
from EF_UVM.ip_env.ip_coverage.ip_coverage import ip_coverage
from gpio8_coverage.gpio8_coverage import gpio8_coverage
from EF_UVM.ip_env.ip_logger.ip_logger import ip_logger
from gpio8_logger.gpio8_logger import gpio8_logger
from EF_UVM.scoreboard import scoreboard
from EF_UVM.bus_env.bus_coverage.bus_coverage import bus_coverage
# import cProfile
# import pstats

@cocotb.test()
async def module_top(dut):
    # profiler = cProfile.Profile()
    # profiler.enable()

    pif = gpio8_if(dut)
    apb_if = bus_apb_if(dut)
    w_irq_if = bus_irq_if(dut)
    UVMConfigDb.set(None, "*", "ip_if", pif)
    UVMConfigDb.set(None, "*", "bus_if", apb_if)
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




class base_test(UVMTest):
    def __init__(self, name="base_test", parent=None):
        super().__init__(name, parent)
        self.test_pass = True
        self.top_env = None
        self.printer = None

    def build_phase(self, phase):
        # UVMConfigDb.set(self, "example_tb0.bus_env.bus_agent.bus_sequencer.run_phase", "default_sequence", write_seq.type_id.get())
        super().build_phase(phase)
        # override 
        self.set_type_override_by_type(ip_driver.get_type(), gpio8_driver.get_type())
        self.set_type_override_by_type(ip_monitor.get_type(), gpio8_monitor.get_type())
        self.set_type_override_by_type(ref_model.get_type(), gpio8_ref_model.get_type())
        self.set_type_override_by_type(ip_coverage.get_type(), gpio8_coverage.get_type())
        self.set_type_override_by_type(ip_logger.get_type(), gpio8_logger.get_type())
        # self.set_type_override_by_type(scoreboard.get_type(), gpio8_scoreboard.get_type())
        # Enable transaction recording for everything
        UVMConfigDb.set(self, "*", "recording_detail", UVM_FULL)
        # Create the tb
        self.example_tb0 = top_env.type_id.create("example_tb0", self)
        # uvm_info(self.tag, f"Hellooo", UVM_LOW)
        # Create a specific depth printer for printing the created topology
        self.printer = UVMTablePrinter()
        self.printer.knobs.depth = -1

        arr = []
        if UVMConfigDb.get(None, "*", "ip_if", arr) is True:
            UVMConfigDb.set(self, "*", "ip_if", arr[0])
        else:
            uvm_fatal("NOVIF", "Could not get ip_if from config DB")

        if UVMConfigDb.get(None, "*", "bus_if", arr) is True:
            UVMConfigDb.set(self, "*", "bus_if", arr[0])
        else:
            uvm_fatal("NOVIF", "Could not get bus_if from config DB")
        # set max number of uvm errors
        server = UVMReportServer()
        server.set_max_quit_count(5)
        UVMCoreService.get().set_report_server(server)


    def end_of_elaboration_phase(self, phase):
        # Set verbosity for the bus monitor for this demo
        uvm_info(self.get_type_name(), sv.sformatf("Printing the test topology :\n%s", self.sprint(self.printer)), UVM_LOW)

    def start_of_simulation_phase(self, phase):
        uvm_info(self.tag, f"start of simulation", UVM_LOW)
        self.bus_sqr = self.example_tb0.bus_env.bus_agent.bus_sequencer
        self.ip_sqr = self.example_tb0.ip_env.ip_agent.ip_sequencer

    async def run_phase(self, phase):
        uvm_info("sequence", "Starting test", UVM_LOW)

    def extract_phase(self, phase):
        super().check_phase(phase)
        server = UVMCoreService.get().get_report_server()
        errors = server.get_severity_count(UVM_ERROR)
        if errors > 0:
            uvm_fatal("FOUND ERRORS", "There were " + str(errors) + " UVM_ERRORs in the test")

    def report_phase(self, phase):
        uvm_info(self.get_type_name(), "report_phase", UVM_LOW)
        if self.test_pass:
            uvm_info(self.get_type_name(), "** UVM TEST PASSED **", UVM_LOW)
        else:
            uvm_fatal(self.get_type_name(), "** UVM TEST FAIL **\n" +
                self.err_msg)


uvm_component_utils(base_test)


class gpio8_all_out_test(base_test):
    def __init__(self, name="gpio8_all_out_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def run_phase(self, phase):
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

class gpio8_all_in_test(base_test):
    def __init__(self, name="gpio8_all_in_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def run_phase(self, phase):
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


class gpio8_rand_test(base_test):
    def __init__(self, name="gpio8_rand_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def run_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")
        bus_gpio8_write_dir_seq = gpio8_write_dir_seq("gpio8_write_dir_seq")
        bus_gpio8_write_datao_seq = gpio8_write_datao_seq("gpio8_write_datao_seq")
        ip_gpio_set_io_in_seq = gpio8_set_io_in_seq("gpio8_set_io_in_seq")
        bus_gpio8_read_datai_seq = gpio8_read_datai_seq("gpio8_read_datai_seq")
        
        for _ in range(70):
            rand_dir = random.choice (range(0, 0xFF))
            bus_gpio8_write_dir_seq.set_gpios_dir(rand_dir)
            bus_gpio8_write_datao_seq.set_gpios_dir(rand_dir)
            ip_gpio_set_io_in_seq.set_gpios_dir(rand_dir)
            await bus_gpio8_write_dir_seq.start(self.bus_sqr)
            await bus_gpio8_write_datao_seq.start(self.bus_sqr)
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)
            await bus_gpio8_read_datai_seq.start(self.bus_sqr)
        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")

uvm_component_utils(gpio8_rand_test)

class gpio8_interrupts_test(base_test):
    def __init__(self, name="gpio8_interrupts_test", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def run_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")
        bus_gpio8_write_dir_seq = gpio8_write_dir_seq("gpio8_write_dir_seq") 
        ip_gpio_set_io_in_seq = gpio8_set_io_in_seq("gpio8_set_io_in_seq")
        bus_gpio8_write_dir_seq.set_gpios_dir(0) # set all IOs dir to input 
        ip_gpio_set_io_in_seq.set_gpios_dir(0)
        bus_gpio8_write_im_seq = gpio8_write_im_seq("gpio8_write_im_seq")
        bus_gpio8_write_ic_seq = gpio8_write_ic_seq("gpio8_write_ic_seq")

        await bus_gpio8_write_dir_seq.start(self.bus_sqr)          # set all IOs direction to input because interrupts are for input IOs 
        
        # IO is high 
        for i in range (8):
            bus_gpio8_write_im_seq.set_im(1 << i)
            ip_gpio_set_io_in_seq.set_gpios_in (1 << i)
            bus_gpio8_write_ic_seq.set_ic (1 << i)
            await bus_gpio8_write_im_seq.start( self.bus_sqr)       # mask the interrupt 
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)          # set the IO
            ip_gpio_set_io_in_seq.set_gpios_in (0x00)               # set the IOs to low (to prevent the rising of the irq again)
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)          
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)        # clear the interrupt 
        
        # IO is low 
        ip_gpio_set_io_in_seq.set_gpios_in (0x00)
        await ip_gpio_set_io_in_seq.start(self.ip_sqr)              # set all IOs to low
        for i in range (8):
            bus_gpio8_write_im_seq.set_im(1 << (i+8))
            bus_gpio8_write_ic_seq.set_ic (1 << (i+8))
            await bus_gpio8_write_im_seq.start( self.bus_sqr)       # mask the interrupt 
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)          # set the IO
            ip_gpio_set_io_in_seq.set_gpios_in (1<<i)               # set IO {i} to high (to preven the rising of the irq again)
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)          
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)        # clear the interrupt 

        # Positive Edge interrupts
        ip_gpio_set_io_in_seq.set_gpios_in (0x00)
        await ip_gpio_set_io_in_seq.start(self.ip_sqr)              # set all IOs to low
        for i in range (8):
            bus_gpio8_write_im_seq.set_im(1 << (i+16))
            ip_gpio_set_io_in_seq.set_gpios_in (1 << i)
            bus_gpio8_write_ic_seq.set_ic (1 << (i+16))
            await bus_gpio8_write_im_seq.start( self.bus_sqr)       # mask the interrupt 
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)          # set the IO
            await Timer(10, "ns")
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)        # clear the interrupt 

        # Negative edge interrupts
        ip_gpio_set_io_in_seq.set_gpios_in (0xFF)
        await ip_gpio_set_io_in_seq.start(self.ip_sqr)              # set all IOs to high
        for i in range (8):
            gpios_in = 0xFF & ~(1 << i)                             # set IO {i} to low (to create a negative edge)
            bus_gpio8_write_im_seq.set_im(1 << (i+24))
            ip_gpio_set_io_in_seq.set_gpios_in (gpios_in)
            bus_gpio8_write_ic_seq.set_ic (1 << (i+24))
            await bus_gpio8_write_im_seq.start( self.bus_sqr)       # mask the interrupt 
            await ip_gpio_set_io_in_seq.start(self.ip_sqr)          # set the IO
            await Timer(10, "ns")
            await bus_gpio8_write_ic_seq.start(self.bus_sqr)        # clear the interrupt 
            
            
        await Timer(1000 , "ns")
        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")

uvm_component_utils(gpio8_interrupts_test)