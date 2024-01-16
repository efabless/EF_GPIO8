
# Entity: EF_GPIO8 
- **File**: EF_GPIO8.v

## Diagram
![Diagram](EF_GPIO8.svg "Diagram")
## Ports

| Port name | Direction | Type       | Description |
| --------- | --------- | ---------- | ----------- |
| clk       | input     | wire       |             |
| rst_n     | input     | wire       |             |
| io_in     | input     | wire [7:0] |             |
| bus_in    | output    | wire [7:0] |             |
| io_out    | output    | wire [7:0] |             |
| bus_out   | input     | wire [7:0] |             |
| io_oe     | output    | wire [7:0] |             |
| bus_oe    | input     | wire [7:0] |             |
| pin0_hi   | output    | wire       |             |
| pin1_hi   | output    | wire       |             |
| pin2_hi   | output    | wire       |             |
| pin3_hi   | output    | wire       |             |
| pin4_hi   | output    | wire       |             |
| pin5_hi   | output    | wire       |             |
| pin6_hi   | output    | wire       |             |
| pin7_hi   | output    | wire       |             |
| pin0_lo   | output    | wire       |             |
| pin1_lo   | output    | wire       |             |
| pin2_lo   | output    | wire       |             |
| pin3_lo   | output    | wire       |             |
| pin4_lo   | output    | wire       |             |
| pin5_lo   | output    | wire       |             |
| pin6_lo   | output    | wire       |             |
| pin7_lo   | output    | wire       |             |
| pin0_pe   | output    | wire       |             |
| pin1_pe   | output    | wire       |             |
| pin2_pe   | output    | wire       |             |
| pin3_pe   | output    | wire       |             |
| pin4_pe   | output    | wire       |             |
| pin5_pe   | output    | wire       |             |
| pin6_pe   | output    | wire       |             |
| pin7_pe   | output    | wire       |             |
| pin0_ne   | output    | wire       |             |
| pin1_ne   | output    | wire       |             |
| pin2_ne   | output    | wire       |             |
| pin3_ne   | output    | wire       |             |
| pin4_ne   | output    | wire       |             |
| pin5_ne   | output    | wire       |             |
| pin6_ne   | output    | wire       |             |
| pin7_ne   | output    | wire       |             |

## Signals

| Name       | Type       | Description |
| ---------- | ---------- | ----------- |
| sync_io_in | wire [7:0] |             |

## Instantiations

- synchronizer[7:0]: bf_sync2
- ped_0: edge_detect_pe
- ped_1: edge_detect_pe
- ped_2: edge_detect_pe
- ped_3: edge_detect_pe
- ped_4: edge_detect_pe
- ped_5: edge_detect_pe
- ped_6: edge_detect_pe
- ped_7: edge_detect_pe
- ned_0: edge_detect_ne
- ned_1: edge_detect_ne
- ned_2: edge_detect_ne
- ned_3: edge_detect_ne
- ned_4: edge_detect_ne
- ned_5: edge_detect_ne
- ned_6: edge_detect_ne
- ned_7: edge_detect_ne
