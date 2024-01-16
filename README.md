# EF_GPIO
A generic 8-bit GPIO port with the following features
- Eight bidirectional pins.
- Input synchronizers
- Input edge detectors.
- Direction control.
- Edge and Level Interrupts generation per pin.
- Wrappers for AHB-Lite, APB and WB buses.

## The Interface 


### Ports 

|Port|Direction|Width|Description|
|---|---|---|---|
|io_in|input|8|GPIOs input (external interface)|
|bus_in|output|8|Synchronized GPIOs input connected to the bus (it drives the DATAI register)|
|io_out|output|8|GPIOs output (external interface)|
|bus_out|input|8|GPIOs output connected to the bus (it's driven by wriring to DATAO register)|
|io_oe|output|8|GPIOs output enable (external interface)|
|bus_oe|input|8|GPIOs output enable connected to the bus (it's driven by wriring to DIR register)|
|pin0_hi|output|1|Pin 0 high flag|
|pin1_hi|output|1|Pin 1 high flag|
|pin2_hi|output|1|Pin 2 high flag|
|pin3_hi|output|1|Pin 3 high flag|
|pin4_hi|output|1|Pin 4 high flag|
|pin5_hi|output|1|Pin 5 high flag|
|pin6_hi|output|1|Pin 6 high flag|
|pin7_hi|output|1|Pin 7 high flag|
|pin0_lo|output|1|Pin 0 low flag|
|pin1_lo|output|1|Pin 1 low flag|
|pin2_lo|output|1|Pin 2 low flag|
|pin3_lo|output|1|Pin 3 low flag|
|pin4_lo|output|1|Pin 4 low flag|
|pin5_lo|output|1|Pin 5 low flag|
|pin6_lo|output|1|Pin 6 low flag|
|pin7_lo|output|1|Pin 7 low flag|
|pin0_pe|output|1|Pin 0 positive edge flag|
|pin1_pe|output|1|Pin 1 positive edge flag|
|pin2_pe|output|1|Pin 2 positive edge flag|
|pin3_pe|output|1|Pin 3 positive edge flag|
|pin4_pe|output|1|Pin 4 positive edge flag|
|pin5_pe|output|1|Pin 5 positive edge flag|
|pin6_pe|output|1|Pin 6 positive edge flag|
|pin7_pe|output|1|Pin 7 positive edge flag|
|pin0_ne|output|1|Pin 0 negative edge flag|
|pin1_ne|output|1|Pin 1 negative edge flag|
|pin2_ne|output|1|Pin 2 negative edge flag|
|pin3_ne|output|1|Pin 3 negative edge flag|
|pin4_ne|output|1|Pin 4 negative edge flag|
|pin5_ne|output|1|Pin 5 negative edge flag|
|pin6_ne|output|1|Pin 6 negative edge flag|
|pin7_ne|output|1|Pin 7 negative edge flag|

## Sky130 Implementation 

|Module | Number of cells | Max. freq |
|---|---|---|
|EF_GPIO8|||
|EF_GPIO8_APB|||
|EF_GPIO8_AHBL|||
|EF_GPIO8_WB|||

## System Integration


## I/O Registers

|Name|Offset|Reset Value|Access Mode|Description|
|---|---|---|---|---|
|DATAI|0000|0x00000000|r|Data In Register; Reading from this register returns the pins status (8 pins); one bit per pin|
|DATAO|0004|0x00000000|w|Data Out Register; Writing to this register change the status of the port pins (8 pins); one bit per pin|
|DIR|0008|0x00000000|w|Direction Register; One bit per pin 1: output, 0: input|
|IM|0f00|0x00000000|w|Interrupt Mask Register; write 1/0 to enable/disable interrupts; check the interrupt flags table for more details|
|RIS|0f08|0x00000000|w|Raw Interrupt Status; reflects the current interrupts status;check the interrupt flags table for more details|
|MIS|0f04|0x00000000|w|Masked Interrupt Status; On a read, this register gives the current masked status value of the corresponding interrupt. A write has no effect; check the interrupt flags table for more details|
|IC|0f0c|0x00000000|w|Interrupt Clear Register; On a write of 1, the corresponding interrupt (both raw interrupt and masked interrupt, if enabled) is cleared; check the interrupt flags table for more details|

### DATAI Register [Offset: 0x0, mode: r]

Data In Register; Reading from this register returns the pins status (8 pins); one bit per pin
<img src="https://svg.wavedrom.com/{reg:[{name:'DATAI', bits:8},{bits: 24}], config: {lanes: 2, hflip: true}} "/>


### DATAO Register [Offset: 0x4, mode: w]

Data Out Register; Writing to this register change the status of the port pins (8 pins); one bit per pin
<img src="https://svg.wavedrom.com/{reg:[{name:'DATAO', bits:8},{bits: 24}], config: {lanes: 2, hflip: true}} "/>


### DIR Register [Offset: 0x8, mode: w]

Direction Register; One bit per pin 1: output, 0: input
<img src="https://svg.wavedrom.com/{reg:[{name:'DIR', bits:8},{bits: 24}], config: {lanes: 2, hflip: true}} "/>


## Interrupt Flags


The following are the bit definitions for the interrupt registers: IM, RIS, MIS, and IC.

|Bit|Flag|Width|Description|
|---|---|---|---|
|0|P0HI|1|Pin 0 is high|
|1|P1HI|1|Pin 1 is high|
|2|P2HI|1|Pin 2 is high|
|3|P3HI|1|Pin 3 is high|
|4|P4HI|1|Pin 4 is high|
|5|P5HI|1|Pin 5 is high|
|6|P6HI|1|Pin 6 is high|
|7|P7HI|1|Pin 7 is high|
|8|P0LO|1|Pin 0 is low|
|9|P1LO|1|Pin 1 is low|
|10|P2LO|1|Pin 2 is low|
|11|P3LO|1|Pin 3 is low|
|12|P4LO|1|Pin 4 is low|
|13|P5LO|1|Pin 5 is low|
|14|P6LO|1|Pin 6 is low|
|15|P7LO|1|Pin 7 is low|
|16|P0PE|1|Pin 0 has observed a rising edge|
|17|P1PE|1|Pin 1 has observed a rising edge|
|18|P2PE|1|Pin 2 has observed a rising edge|
|19|P3PE|1|Pin 3 has observed a rising edge|
|20|P4PE|1|Pin 4 has observed a rising edge|
|21|P5PE|1|Pin 5 has observed a rising edge|
|22|P6PE|1|Pin 6 has observed a rising edge|
|23|P7PE|1|Pin 7 has observed a rising edge|
|24|P0NE|1|Pin 0 has observed a falling edge|
|25|P1NE|1|Pin 1 has observed a falling edge|
|26|P2NE|1|Pin 2 has observed a falling edge|
|27|P3NE|1|Pin 3 has observed a falling edge|
|28|P4NE|1|Pin 4 has observed a falling edge|
|29|P5NE|1|Pin 5 has observed a falling edge|
|30|P6NE|1|Pin 6 has observed a falling edge|
|31|P7NE|1|Pin 7 has observed a falling edge|

## F/W Usage Guidelines:
## Installation:
## Simulation:
### Run Verilog Testbench:
### Run cocotb UVM Testbench:
