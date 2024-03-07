PLUSARGS += "+UVM_VERBOSITY=UVM_MEDIUM"
TOPLEVEL := top
MODULE   ?= top_module
VERILOG_SOURCES ?=  $(PWD)/top.v $(PWD)/../../hdl/rtl/bus_wrappers/EF_GPIO8_APB.v  $(PWD)/../../hdl/rtl/EF_GPIO8.v
RTL_MACROS ?= ""
YAML_FILE = $(PWD)/../../EF_GPIO8.yaml
MAKEFLAGS += --no-print-directory

# List of tests
TESTS := gpio8_all_out_test gpio8_all_in_test gpio8_rand_test gpio8_interrupts_test

# Variable for tag - set this as required
SIM_TAG ?= default_tag

# Define SIM_PATH variable
SIM_PATH := $(PWD)/sim/$(SIM_TAG)

include EF_UVM/Makefile.test
