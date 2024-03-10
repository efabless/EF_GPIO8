PLUSARGS += "+UVM_VERBOSITY=UVM_MEDIUM"
TOPLEVEL := top
MODULE   ?= top_module
AHB_FILES ?= $(PWD)/../../hdl/rtl/bus_wrappers/EF_GPIO8_AHBL.pp.v
APB_FILES ?= $(PWD)/../../hdl/rtl/bus_wrappers/EF_GPIO8_APB.pp.v
WB_FILES ?= ""
HDL_FILES ?=  $(PWD)/../../hdl/rtl/EF_GPIO8.pp.v
VERILOG_SOURCES ?=  $(PWD)/top.v $(AHB_FILES) $(APB_FILES) $(WB_FILES) $(HDL_FILES)
RTL_MACROS += ""
BUS_TYPE ?= APB
ifeq ($(BUS_TYPE),APB)
    RTL_MACROS += -DBUS_TYPE_APB
else ifeq ($(BUS_TYPE),AHB)
    RTL_MACROS += -DBUS_TYPE_AHB
else ifeq ($(BUS_TYPE),WISHBONE)
    RTL_MACROS += -DBUS_TYPE_WISHBONE
endif
YAML_FILE = $(PWD)/../../EF_GPIO8.yaml
MAKEFLAGS += --no-print-directory

# List of tests
TESTS := gpio8_all_out_test gpio8_all_in_test gpio8_rand_test gpio8_interrupts_test
# TESTS := pwm_tmr_test

# Variable for tag - set this as required
SIM_TAG ?= default_tag

# Define SIM_PATH variable
SIM_PATH := $(PWD)/sim/$(SIM_TAG)

clone_ef_uvm := $(shell if [ ! -d "EF_UVM" ]; then \
	echo "Cloning the EF_UVM repository..."; \
	git clone https://github.com/efabless/EF_UVM.git; \
fi;)

# clone_ip_util := $(shell if [ ! -d "IP_Utilities" ]; then \
# 	echo "Cloning the IP_Utilities repository..."; \
# 	git clone https://github.com/shalan/IP_Utilities.git; \
# fi;)

include EF_UVM/Makefile.test
