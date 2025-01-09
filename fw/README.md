# API Reference

## Header files

- [EF_Driver_Common.h](#file-ef_driver_commonh)
- [EF_GPIO8.h](#file-ef_gpio8h)
- [EF_GPIO8_regs.h](#file-ef_gpio8_regsh)

## File EF_Driver_Common.h

_C header file for common driver definitions and types._



## Structures and Types

| Type | Name |
| ---: | :--- |
| typedef uint32\_t | [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status)  <br>_A type that is used to return the status of the driver functions._ |


## Macros

| Type | Name |
| ---: | :--- |
| define  | [**EF\_DRIVER\_ERROR**](#define-ef_driver_error)  1<br>_Unspecified error._ |
| define  | [**EF\_DRIVER\_ERROR\_BUSY**](#define-ef_driver_error_busy)  2<br>_Driver is busy._ |
| define  | [**EF\_DRIVER\_ERROR\_NO\_DATA**](#define-ef_driver_error_no_data)  7<br>_No data available._ |
| define  | [**EF\_DRIVER\_ERROR\_PARAMETER**](#define-ef_driver_error_parameter)  5<br>_Parameter error._ |
| define  | [**EF\_DRIVER\_ERROR\_SPECIFIC**](#define-ef_driver_error_specific)  6<br>_Start of driver specific errors._ |
| define  | [**EF\_DRIVER\_ERROR\_TIMEOUT**](#define-ef_driver_error_timeout)  3<br>_Timeout occurred._ |
| define  | [**EF\_DRIVER\_ERROR\_UNSUPPORTED**](#define-ef_driver_error_unsupported)  4<br>_Operation not supported._ |
| define  | [**EF\_DRIVER\_OK**](#define-ef_driver_ok)  0<br>_Operation succeeded._ |

## Structures and Types Documentation

### typedef `EF_DRIVER_STATUS`

_A type that is used to return the status of the driver functions._
```c
typedef uint32_t EF_DRIVER_STATUS;
```



## Macros Documentation

### define `EF_DRIVER_ERROR`

_Unspecified error._
```c
#define EF_DRIVER_ERROR 1
```

### define `EF_DRIVER_ERROR_BUSY`

_Driver is busy._
```c
#define EF_DRIVER_ERROR_BUSY 2
```

### define `EF_DRIVER_ERROR_NO_DATA`

_No data available._
```c
#define EF_DRIVER_ERROR_NO_DATA 7
```

### define `EF_DRIVER_ERROR_PARAMETER`

_Parameter error._
```c
#define EF_DRIVER_ERROR_PARAMETER 5
```

### define `EF_DRIVER_ERROR_SPECIFIC`

_Start of driver specific errors._
```c
#define EF_DRIVER_ERROR_SPECIFIC 6
```

### define `EF_DRIVER_ERROR_TIMEOUT`

_Timeout occurred._
```c
#define EF_DRIVER_ERROR_TIMEOUT 3
```

### define `EF_DRIVER_ERROR_UNSUPPORTED`

_Operation not supported._
```c
#define EF_DRIVER_ERROR_UNSUPPORTED 4
```

### define `EF_DRIVER_OK`

_Operation succeeded._
```c
#define EF_DRIVER_OK 0
```


## File EF_GPIO8.h

_C header file for GPIO8 APIs which contains the function prototypes._




## Functions

| Type | Name |
| ---: | :--- |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_getIM**](#function-ef_gpio8_getim) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t \*gpio\_im) <br> |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_getMIS**](#function-ef_gpio8_getmis) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t \*gpio\_mis) <br> |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_getRIS**](#function-ef_gpio8_getris) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t \*gpio\_ris) <br> |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_readData**](#function-ef_gpio8_readdata) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t \*gpio\_data) <br>_reads the input value of the GPIOs_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_readDirection**](#function-ef_gpio8_readdirection) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t \*gpio\_dir) <br>_gets the direction of all GPIOs_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_readPackedData**](#function-ef_gpio8_readpackeddata) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint8\_t pins, uint32\_t \*packed\_data) <br>_This function reads the data from a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it reads the data from the pin(s)._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_setGclkEnable**](#function-ef_gpio8_setgclkenable) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t value) <br>_sets the GCLK enable bit in the GPIO register to a certain value_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_setICR**](#function-ef_gpio8_seticr) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t mask) <br> |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_setIM**](#function-ef_gpio8_setim) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t mask) <br> |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_setPinDirection**](#function-ef_gpio8_setpindirection) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t pin, uint32\_t dir) <br>_sets the direction of one GPIO pin_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_setPinPackedDirection**](#function-ef_gpio8_setpinpackeddirection) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint8\_t pins, uint32\_t dir) <br> |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_waitInput**](#function-ef_gpio8_waitinput) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t compare\_value) <br>_wait until the input GPIOs have a certain value_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_wait\_InputPin**](#function-ef_gpio8_wait_inputpin) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t pin, uint32\_t compare\_value) <br>_wait until a GPIO pin have a certain value_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_writeAllDirection**](#function-ef_gpio8_writealldirection) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t data) <br>_sets the direction of all GPIOs_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_writeData**](#function-ef_gpio8_writedata) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint32\_t data) <br>_drives the output value of the GPIOs_ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_GPIO8\_writePackedData**](#function-ef_gpio8_writepackeddata) ([**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr) gpio, uint8\_t pins, uint8\_t data) <br> |

## Macros

| Type | Name |
| ---: | :--- |
| define  | [**EF\_GPIO8\_DATAI\_MAX\_VALUE**](#define-ef_gpio8_datai_max_value)  0x000000FF<br> |
| define  | [**EF\_GPIO8\_DATAO\_MAX\_VALUE**](#define-ef_gpio8_datao_max_value)  0x000000FF<br> |
| define  | [**EF\_GPIO8\_DIR\_MAX\_VALUE**](#define-ef_gpio8_dir_max_value)  0x000000FF<br> |
| define  | [**EF\_GPIO8\_NUM\_PINS**](#define-ef_gpio8_num_pins)  0x00000008<br> |
| define  | [**GPIO8\_INPUT**](#define-gpio8_input)  0<br> |
| define  | [**GPIO8\_OUTPUT**](#define-gpio8_output)  1<br> |


## Functions Documentation

### function `EF_GPIO8_getIM`

```c
EF_DRIVER_STATUS EF_GPIO8_getIM (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t *gpio_im
) 
```


returns the value of the Interrupts Masking Register; which enable and disables interrupts

* bit 0 P0HI : Pin 0 is high
* bit 1 P1HI : Pin 1 is high
* bit 2 P2HI : Pin 2 is high
* bit 3 P3HI : Pin 3 is high
* bit 4 P4HI : Pin 4 is high
* bit 5 P5HI : Pin 5 is high
* bit 6 P6HI : Pin 6 is high
* bit 7 P7HI : Pin 7 is high
* bit 8 P0LO : Pin 0 is low
* bit 9 P1LO : Pin 1 is low
* bit 10 P2LO : Pin 2 is low
* bit 11 P3LO : Pin 3 is low
* bit 12 P4LO : Pin 4 is low
* bit 13 P5LO : Pin 5 is low
* bit 14 P6LO : Pin 6 is low
* bit 15 P7LO : Pin 7 is low
* bit 16 P0PE : Pin 0 has observed a rising edge
* bit 17 P1PE : Pin 1 has observed a rising edge
* bit 18 P2PE : Pin 2 has observed a rising edge
* bit 19 P3PE : Pin 3 has observed a rising edge
* bit 20 P4PE : Pin 4 has observed a rising edge
* bit 21 P5PE : Pin 5 has observed a rising edge
* bit 22 P6PE : Pin 6 has observed a rising edge
* bit 23 P7PE : Pin 7 has observed a rising edge
* bit 24 P0NE : Pin 0 has observed a falling edge
* bit 25 P1NE : Pin 1 has observed a falling edge
* bit 26 P2NE : Pin 2 has observed a falling edge
* bit 27 P3NE : Pin 3 has observed a falling edge
* bit 28 P4NE : Pin 4 has observed a falling edge
* bit 29 P5NE : Pin 5 has observed a falling edge
* bit 30 P6NE : Pin 6 has observed a falling edge
* bit 31 P7NE : Pin 7 has observed a falling edge



**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `gpio_im` The value of the IM register


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_getMIS`

```c
EF_DRIVER_STATUS EF_GPIO8_getMIS (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t *gpio_mis
) 
```


returns the value of the Masked Interrupt Status Register

* bit 0 P0HI : Pin 0 is high
* bit 1 P1HI : Pin 1 is high
* bit 2 P2HI : Pin 2 is high
* bit 3 P3HI : Pin 3 is high
* bit 4 P4HI : Pin 4 is high
* bit 5 P5HI : Pin 5 is high
* bit 6 P6HI : Pin 6 is high
* bit 7 P7HI : Pin 7 is high
* bit 8 P0LO : Pin 0 is low
* bit 9 P1LO : Pin 1 is low
* bit 10 P2LO : Pin 2 is low
* bit 11 P3LO : Pin 3 is low
* bit 12 P4LO : Pin 4 is low
* bit 13 P5LO : Pin 5 is low
* bit 14 P6LO : Pin 6 is low
* bit 15 P7LO : Pin 7 is low
* bit 16 P0PE : Pin 0 has observed a rising edge
* bit 17 P1PE : Pin 1 has observed a rising edge
* bit 18 P2PE : Pin 2 has observed a rising edge
* bit 19 P3PE : Pin 3 has observed a rising edge
* bit 20 P4PE : Pin 4 has observed a rising edge
* bit 21 P5PE : Pin 5 has observed a rising edge
* bit 22 P6PE : Pin 6 has observed a rising edge
* bit 23 P7PE : Pin 7 has observed a rising edge
* bit 24 P0NE : Pin 0 has observed a falling edge
* bit 25 P1NE : Pin 1 has observed a falling edge
* bit 26 P2NE : Pin 2 has observed a falling edge
* bit 27 P3NE : Pin 3 has observed a falling edge
* bit 28 P4NE : Pin 4 has observed a falling edge
* bit 29 P5NE : Pin 5 has observed a falling edge
* bit 30 P6NE : Pin 6 has observed a falling edge
* bit 31 P7NE : Pin 7 has observed a falling edge



**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `gpio_mis` The value of the MIS register


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_getRIS`

```c
EF_DRIVER_STATUS EF_GPIO8_getRIS (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t *gpio_ris
) 
```


returns the value of the Raw Interrupt Status Register

* bit 0 P0HI : Pin 0 is high
* bit 1 P1HI : Pin 1 is high
* bit 2 P2HI : Pin 2 is high
* bit 3 P3HI : Pin 3 is high
* bit 4 P4HI : Pin 4 is high
* bit 5 P5HI : Pin 5 is high
* bit 6 P6HI : Pin 6 is high
* bit 7 P7HI : Pin 7 is high
* bit 8 P0LO : Pin 0 is low
* bit 9 P1LO : Pin 1 is low
* bit 10 P2LO : Pin 2 is low
* bit 11 P3LO : Pin 3 is low
* bit 12 P4LO : Pin 4 is low
* bit 13 P5LO : Pin 5 is low
* bit 14 P6LO : Pin 6 is low
* bit 15 P7LO : Pin 7 is low
* bit 16 P0PE : Pin 0 has observed a rising edge
* bit 17 P1PE : Pin 1 has observed a rising edge
* bit 18 P2PE : Pin 2 has observed a rising edge
* bit 19 P3PE : Pin 3 has observed a rising edge
* bit 20 P4PE : Pin 4 has observed a rising edge
* bit 21 P5PE : Pin 5 has observed a rising edge
* bit 22 P6PE : Pin 6 has observed a rising edge
* bit 23 P7PE : Pin 7 has observed a rising edge
* bit 24 P0NE : Pin 0 has observed a falling edge
* bit 25 P1NE : Pin 1 has observed a falling edge
* bit 26 P2NE : Pin 2 has observed a falling edge
* bit 27 P3NE : Pin 3 has observed a falling edge
* bit 28 P4NE : Pin 4 has observed a falling edge
* bit 29 P5NE : Pin 5 has observed a falling edge
* bit 30 P6NE : Pin 6 has observed a falling edge
* bit 31 P7NE : Pin 7 has observed a falling edge



**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `gpio_ris` The value of the RIS register


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_readData`

_reads the input value of the GPIOs_
```c
EF_DRIVER_STATUS EF_GPIO8_readData (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t *gpio_data
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `gpio_data` The value of the input GPIOs


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_readDirection`

_gets the direction of all GPIOs_
```c
EF_DRIVER_STATUS EF_GPIO8_readDirection (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t *gpio_dir
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `gpio_dir` GPIOs direction where 1 is output and 0 means input. It should be an eight bit value where each bit represents the direction of certain GPIO pin


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_readPackedData`

_This function reads the data from a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it reads the data from the pin(s)._
```c
EF_DRIVER_STATUS EF_GPIO8_readPackedData (
    EF_GPIO8_TYPE_PTR gpio,
    uint8_t pins,
    uint32_t *packed_data
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `pins` The bit-packed representation of the pin(s). 
* `packed_data` The data read from the pin(s)


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_setGclkEnable`

_sets the GCLK enable bit in the GPIO register to a certain value_
```c
EF_DRIVER_STATUS EF_GPIO8_setGclkEnable (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t value
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `value` The value of the GCLK enable bit


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_setICR`

```c
EF_DRIVER_STATUS EF_GPIO8_setICR (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t mask
) 
```


sets the value of the Interrupts Clear Register; write 1 to clear the flag

* bit 0 P0HI : Pin 0 is high
* bit 1 P1HI : Pin 1 is high
* bit 2 P2HI : Pin 2 is high
* bit 3 P3HI : Pin 3 is high
* bit 4 P4HI : Pin 4 is high
* bit 5 P5HI : Pin 5 is high
* bit 6 P6HI : Pin 6 is high
* bit 7 P7HI : Pin 7 is high
* bit 8 P0LO : Pin 0 is low
* bit 9 P1LO : Pin 1 is low
* bit 10 P2LO : Pin 2 is low
* bit 11 P3LO : Pin 3 is low
* bit 12 P4LO : Pin 4 is low
* bit 13 P5LO : Pin 5 is low
* bit 14 P6LO : Pin 6 is low
* bit 15 P7LO : Pin 7 is low
* bit 16 P0PE : Pin 0 has observed a rising edge
* bit 17 P1PE : Pin 1 has observed a rising edge
* bit 18 P2PE : Pin 2 has observed a rising edge
* bit 19 P3PE : Pin 3 has observed a rising edge
* bit 20 P4PE : Pin 4 has observed a rising edge
* bit 21 P5PE : Pin 5 has observed a rising edge
* bit 22 P6PE : Pin 6 has observed a rising edge
* bit 23 P7PE : Pin 7 has observed a rising edge
* bit 24 P0NE : Pin 0 has observed a falling edge
* bit 25 P1NE : Pin 1 has observed a falling edge
* bit 26 P2NE : Pin 2 has observed a falling edge
* bit 27 P3NE : Pin 3 has observed a falling edge
* bit 28 P4NE : Pin 4 has observed a falling edge
* bit 29 P5NE : Pin 5 has observed a falling edge
* bit 30 P6NE : Pin 6 has observed a falling edge
* bit 31 P7NE : Pin 7 has observed a falling edge



**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `mask` The required mask value


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_setIM`

```c
EF_DRIVER_STATUS EF_GPIO8_setIM (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t mask
) 
```


sets the value of the Interrupts Masking Register; which enable and disables interrupts

* bit 0 P0HI : Pin 0 is high
* bit 1 P1HI : Pin 1 is high
* bit 2 P2HI : Pin 2 is high
* bit 3 P3HI : Pin 3 is high
* bit 4 P4HI : Pin 4 is high
* bit 5 P5HI : Pin 5 is high
* bit 6 P6HI : Pin 6 is high
* bit 7 P7HI : Pin 7 is high
* bit 8 P0LO : Pin 0 is low
* bit 9 P1LO : Pin 1 is low
* bit 10 P2LO : Pin 2 is low
* bit 11 P3LO : Pin 3 is low
* bit 12 P4LO : Pin 4 is low
* bit 13 P5LO : Pin 5 is low
* bit 14 P6LO : Pin 6 is low
* bit 15 P7LO : Pin 7 is low
* bit 16 P0PE : Pin 0 has observed a rising edge
* bit 17 P1PE : Pin 1 has observed a rising edge
* bit 18 P2PE : Pin 2 has observed a rising edge
* bit 19 P3PE : Pin 3 has observed a rising edge
* bit 20 P4PE : Pin 4 has observed a rising edge
* bit 21 P5PE : Pin 5 has observed a rising edge
* bit 22 P6PE : Pin 6 has observed a rising edge
* bit 23 P7PE : Pin 7 has observed a rising edge
* bit 24 P0NE : Pin 0 has observed a falling edge
* bit 25 P1NE : Pin 1 has observed a falling edge
* bit 26 P2NE : Pin 2 has observed a falling edge
* bit 27 P3NE : Pin 3 has observed a falling edge
* bit 28 P4NE : Pin 4 has observed a falling edge
* bit 29 P5NE : Pin 5 has observed a falling edge
* bit 30 P6NE : Pin 6 has observed a falling edge
* bit 31 P7NE : Pin 7 has observed a falling edge



**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `mask` The required mask value


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_setPinDirection`

_sets the direction of one GPIO pin_
```c
EF_DRIVER_STATUS EF_GPIO8_setPinDirection (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t pin,
    uint32_t dir
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `pin` pin number from 0 to 7 
* `dir` GPIO pin direction where 1 is output and 0 means input.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_setPinPackedDirection`

```c
EF_DRIVER_STATUS EF_GPIO8_setPinPackedDirection (
    EF_GPIO8_TYPE_PTR gpio,
    uint8_t pins,
    uint32_t dir
) 
```


This function sets the direction of a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it sets the direction of the pin(s) to the required value. 

**Note:**

All the specified pins are set to the same direction (dir). 



**Note:**

The function does not affect the direction of the other pins in the port.



**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `pins` The bit-packed representation of the pin(s). 
* `dir` The required direction value


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_waitInput`

_wait until the input GPIOs have a certain value_
```c
EF_DRIVER_STATUS EF_GPIO8_waitInput (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t compare_value
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `compare_value` the value to compare the input GPIOs with


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_wait_InputPin`

_wait until a GPIO pin have a certain value_
```c
EF_DRIVER_STATUS EF_GPIO8_wait_InputPin (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t pin,
    uint32_t compare_value
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `pin` The pin number from 0 to 7 
* `compare_value` The value to compare the GPIO with


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_writeAllDirection`

_sets the direction of all GPIOs_
```c
EF_DRIVER_STATUS EF_GPIO8_writeAllDirection (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t data
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `data` GPIOs direction where 1 is output and 0 means input. It should be an eight bit value where each bit represents the direction of certain GPIO pin


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_writeData`

_drives the output value of the GPIOs_
```c
EF_DRIVER_STATUS EF_GPIO8_writeData (
    EF_GPIO8_TYPE_PTR gpio,
    uint32_t data
) 
```


**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `data` value to be driven to output GPIOs


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_GPIO8_writePackedData`

```c
EF_DRIVER_STATUS EF_GPIO8_writePackedData (
    EF_GPIO8_TYPE_PTR gpio,
    uint8_t pins,
    uint8_t data
) 
```


This function writes the data to a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it writes the data to the pin(s). Note that all the specified pins are set to the corresponding value of the corresponding bit in the data parameter.



**Parameters:**


* `gpio` An [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) pointer, which points to the base memory address of GPIO registers.[**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) is a structure that contains the GPIO registers.
* `pins` The bit-packed representation of the pin(s). 
* `data` The data to be written to the pin(s)


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code

## Macros Documentation

### define `EF_GPIO8_DATAI_MAX_VALUE`

```c
#define EF_GPIO8_DATAI_MAX_VALUE 0x000000FF
```

### define `EF_GPIO8_DATAO_MAX_VALUE`

```c
#define EF_GPIO8_DATAO_MAX_VALUE 0x000000FF
```

### define `EF_GPIO8_DIR_MAX_VALUE`

```c
#define EF_GPIO8_DIR_MAX_VALUE 0x000000FF
```

### define `EF_GPIO8_NUM_PINS`

```c
#define EF_GPIO8_NUM_PINS 0x00000008
```

### define `GPIO8_INPUT`

```c
#define GPIO8_INPUT 0
```

### define `GPIO8_OUTPUT`

```c
#define GPIO8_OUTPUT 1
```


## File EF_GPIO8_regs.h





## Structures and Types

| Type | Name |
| ---: | :--- |
| typedef struct [**\_EF\_GPIO8\_TYPE\_**](#struct-_ef_gpio8_type_) | [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type)  <br> |
| typedef [**EF\_GPIO8\_TYPE**](#typedef-ef_gpio8_type) \* | [**EF\_GPIO8\_TYPE\_PTR**](#typedef-ef_gpio8_type_ptr)  <br> |
| struct | [**\_EF\_GPIO8\_TYPE\_**](#struct-_ef_gpio8_type_) <br> |


## Macros

| Type | Name |
| ---: | :--- |
| define  | [**EF\_GPIO8\_P0HI\_FLAG**](#define-ef_gpio8_p0hi_flag)  0x1<br> |
| define  | [**EF\_GPIO8\_P0LO\_FLAG**](#define-ef_gpio8_p0lo_flag)  0x100<br> |
| define  | [**EF\_GPIO8\_P0NE\_FLAG**](#define-ef_gpio8_p0ne_flag)  0x1000000<br> |
| define  | [**EF\_GPIO8\_P0PE\_FLAG**](#define-ef_gpio8_p0pe_flag)  0x10000<br> |
| define  | [**EF\_GPIO8\_P1HI\_FLAG**](#define-ef_gpio8_p1hi_flag)  0x2<br> |
| define  | [**EF\_GPIO8\_P1LO\_FLAG**](#define-ef_gpio8_p1lo_flag)  0x200<br> |
| define  | [**EF\_GPIO8\_P1NE\_FLAG**](#define-ef_gpio8_p1ne_flag)  0x2000000<br> |
| define  | [**EF\_GPIO8\_P1PE\_FLAG**](#define-ef_gpio8_p1pe_flag)  0x20000<br> |
| define  | [**EF\_GPIO8\_P2HI\_FLAG**](#define-ef_gpio8_p2hi_flag)  0x4<br> |
| define  | [**EF\_GPIO8\_P2LO\_FLAG**](#define-ef_gpio8_p2lo_flag)  0x400<br> |
| define  | [**EF\_GPIO8\_P2NE\_FLAG**](#define-ef_gpio8_p2ne_flag)  0x4000000<br> |
| define  | [**EF\_GPIO8\_P2PE\_FLAG**](#define-ef_gpio8_p2pe_flag)  0x40000<br> |
| define  | [**EF\_GPIO8\_P3HI\_FLAG**](#define-ef_gpio8_p3hi_flag)  0x8<br> |
| define  | [**EF\_GPIO8\_P3LO\_FLAG**](#define-ef_gpio8_p3lo_flag)  0x800<br> |
| define  | [**EF\_GPIO8\_P3NE\_FLAG**](#define-ef_gpio8_p3ne_flag)  0x8000000<br> |
| define  | [**EF\_GPIO8\_P3PE\_FLAG**](#define-ef_gpio8_p3pe_flag)  0x80000<br> |
| define  | [**EF\_GPIO8\_P4HI\_FLAG**](#define-ef_gpio8_p4hi_flag)  0x10<br> |
| define  | [**EF\_GPIO8\_P4LO\_FLAG**](#define-ef_gpio8_p4lo_flag)  0x1000<br> |
| define  | [**EF\_GPIO8\_P4NE\_FLAG**](#define-ef_gpio8_p4ne_flag)  0x10000000<br> |
| define  | [**EF\_GPIO8\_P4PE\_FLAG**](#define-ef_gpio8_p4pe_flag)  0x100000<br> |
| define  | [**EF\_GPIO8\_P5HI\_FLAG**](#define-ef_gpio8_p5hi_flag)  0x20<br> |
| define  | [**EF\_GPIO8\_P5LO\_FLAG**](#define-ef_gpio8_p5lo_flag)  0x2000<br> |
| define  | [**EF\_GPIO8\_P5NE\_FLAG**](#define-ef_gpio8_p5ne_flag)  0x20000000<br> |
| define  | [**EF\_GPIO8\_P5PE\_FLAG**](#define-ef_gpio8_p5pe_flag)  0x200000<br> |
| define  | [**EF\_GPIO8\_P6HI\_FLAG**](#define-ef_gpio8_p6hi_flag)  0x40<br> |
| define  | [**EF\_GPIO8\_P6LO\_FLAG**](#define-ef_gpio8_p6lo_flag)  0x4000<br> |
| define  | [**EF\_GPIO8\_P6NE\_FLAG**](#define-ef_gpio8_p6ne_flag)  0x40000000<br> |
| define  | [**EF\_GPIO8\_P6PE\_FLAG**](#define-ef_gpio8_p6pe_flag)  0x400000<br> |
| define  | [**EF\_GPIO8\_P7HI\_FLAG**](#define-ef_gpio8_p7hi_flag)  0x80<br> |
| define  | [**EF\_GPIO8\_P7LO\_FLAG**](#define-ef_gpio8_p7lo_flag)  0x8000<br> |
| define  | [**EF\_GPIO8\_P7NE\_FLAG**](#define-ef_gpio8_p7ne_flag)  0x80000000<br> |
| define  | [**EF\_GPIO8\_P7PE\_FLAG**](#define-ef_gpio8_p7pe_flag)  0x800000<br> |
| define  | [**IO\_TYPES**](#define-io_types)  <br> |
| define  | [**\_\_R**](#define-__r)  volatile const uint32\_t<br> |
| define  | [**\_\_RW**](#define-__rw)  volatile       uint32\_t<br> |
| define  | [**\_\_W**](#define-__w)  volatile       uint32\_t<br> |

## Structures and Types Documentation

### typedef `EF_GPIO8_TYPE`

```c
typedef struct _EF_GPIO8_TYPE_ EF_GPIO8_TYPE;
```

### typedef `EF_GPIO8_TYPE_PTR`

```c
typedef EF_GPIO8_TYPE* EF_GPIO8_TYPE_PTR;
```

### struct `_EF_GPIO8_TYPE_`


Variables:

-  [**\_\_R**](#define-__r) DATAI  

-  [**\_\_W**](#define-__w) DATAO  

-  [**\_\_W**](#define-__w) DIR  

-  [**\_\_W**](#define-__w) GCLK  

-  [**\_\_W**](#define-__w) IC  

-  [**\_\_RW**](#define-__rw) IM  

-  [**\_\_R**](#define-__r) MIS  

-  [**\_\_R**](#define-__r) RIS  

-  [**\_\_R**](#define-__r) reserved_0  



## Macros Documentation

### define `EF_GPIO8_P0HI_FLAG`

```c
#define EF_GPIO8_P0HI_FLAG 0x1
```

### define `EF_GPIO8_P0LO_FLAG`

```c
#define EF_GPIO8_P0LO_FLAG 0x100
```

### define `EF_GPIO8_P0NE_FLAG`

```c
#define EF_GPIO8_P0NE_FLAG 0x1000000
```

### define `EF_GPIO8_P0PE_FLAG`

```c
#define EF_GPIO8_P0PE_FLAG 0x10000
```

### define `EF_GPIO8_P1HI_FLAG`

```c
#define EF_GPIO8_P1HI_FLAG 0x2
```

### define `EF_GPIO8_P1LO_FLAG`

```c
#define EF_GPIO8_P1LO_FLAG 0x200
```

### define `EF_GPIO8_P1NE_FLAG`

```c
#define EF_GPIO8_P1NE_FLAG 0x2000000
```

### define `EF_GPIO8_P1PE_FLAG`

```c
#define EF_GPIO8_P1PE_FLAG 0x20000
```

### define `EF_GPIO8_P2HI_FLAG`

```c
#define EF_GPIO8_P2HI_FLAG 0x4
```

### define `EF_GPIO8_P2LO_FLAG`

```c
#define EF_GPIO8_P2LO_FLAG 0x400
```

### define `EF_GPIO8_P2NE_FLAG`

```c
#define EF_GPIO8_P2NE_FLAG 0x4000000
```

### define `EF_GPIO8_P2PE_FLAG`

```c
#define EF_GPIO8_P2PE_FLAG 0x40000
```

### define `EF_GPIO8_P3HI_FLAG`

```c
#define EF_GPIO8_P3HI_FLAG 0x8
```

### define `EF_GPIO8_P3LO_FLAG`

```c
#define EF_GPIO8_P3LO_FLAG 0x800
```

### define `EF_GPIO8_P3NE_FLAG`

```c
#define EF_GPIO8_P3NE_FLAG 0x8000000
```

### define `EF_GPIO8_P3PE_FLAG`

```c
#define EF_GPIO8_P3PE_FLAG 0x80000
```

### define `EF_GPIO8_P4HI_FLAG`

```c
#define EF_GPIO8_P4HI_FLAG 0x10
```

### define `EF_GPIO8_P4LO_FLAG`

```c
#define EF_GPIO8_P4LO_FLAG 0x1000
```

### define `EF_GPIO8_P4NE_FLAG`

```c
#define EF_GPIO8_P4NE_FLAG 0x10000000
```

### define `EF_GPIO8_P4PE_FLAG`

```c
#define EF_GPIO8_P4PE_FLAG 0x100000
```

### define `EF_GPIO8_P5HI_FLAG`

```c
#define EF_GPIO8_P5HI_FLAG 0x20
```

### define `EF_GPIO8_P5LO_FLAG`

```c
#define EF_GPIO8_P5LO_FLAG 0x2000
```

### define `EF_GPIO8_P5NE_FLAG`

```c
#define EF_GPIO8_P5NE_FLAG 0x20000000
```

### define `EF_GPIO8_P5PE_FLAG`

```c
#define EF_GPIO8_P5PE_FLAG 0x200000
```

### define `EF_GPIO8_P6HI_FLAG`

```c
#define EF_GPIO8_P6HI_FLAG 0x40
```

### define `EF_GPIO8_P6LO_FLAG`

```c
#define EF_GPIO8_P6LO_FLAG 0x4000
```

### define `EF_GPIO8_P6NE_FLAG`

```c
#define EF_GPIO8_P6NE_FLAG 0x40000000
```

### define `EF_GPIO8_P6PE_FLAG`

```c
#define EF_GPIO8_P6PE_FLAG 0x400000
```

### define `EF_GPIO8_P7HI_FLAG`

```c
#define EF_GPIO8_P7HI_FLAG 0x80
```

### define `EF_GPIO8_P7LO_FLAG`

```c
#define EF_GPIO8_P7LO_FLAG 0x8000
```

### define `EF_GPIO8_P7NE_FLAG`

```c
#define EF_GPIO8_P7NE_FLAG 0x80000000
```

### define `EF_GPIO8_P7PE_FLAG`

```c
#define EF_GPIO8_P7PE_FLAG 0x800000
```

### define `IO_TYPES`

```c
#define IO_TYPES 
```

### define `__R`

```c
#define __R volatile const uint32_t
```

### define `__RW`

```c
#define __RW volatile       uint32_t
```

### define `__W`

```c
#define __W volatile       uint32_t
```


