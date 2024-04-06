---
title: EF_GPIO8.c

---

# EF_GPIO8.c



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[EF_GPIO8_readData](Files/EF__GPIO8_8c.md#function-ef-gpio8-readdata)**(uint32_t gpio_base)<br>reads the input value of the GPIOs  |
| void | **[EF_GPIO8_waitInput](Files/EF__GPIO8_8c.md#function-ef-gpio8-waitinput)**(uint32_t gpio_base, int data)<br>wait until the input GPIOs have a certain value  |
| void | **[EF_GPIO8_wait_InputPin](Files/EF__GPIO8_8c.md#function-ef-gpio8-wait-inputpin)**(uint32_t gpio_base, int pin, int data)<br>wait until a GPIO pin have a certain value  |
| void | **[EF_GPIO8_writeData](Files/EF__GPIO8_8c.md#function-ef-gpio8-writedata)**(uint32_t gpio_base, int data)<br>drives the output value of the GPIOs  |
| void | **[EF_GPIO8_writeAllDirection](Files/EF__GPIO8_8c.md#function-ef-gpio8-writealldirection)**(uint32_t gpio_base, int data)<br>sets the direction of all GPIOs  |
| int | **[EF_GPIO8_readDirection](Files/EF__GPIO8_8c.md#function-ef-gpio8-readdirection)**(uint32_t gpio_base)<br>gets the direction of all GPIOs  |
| void | **[EF_GPIO8_setPinDirection](Files/EF__GPIO8_8c.md#function-ef-gpio8-setpindirection)**(uint32_t gpio_base, int pin, int dir)<br>sets the direction of one GPIO pin  |
| void | **[EF_GPIO8_setIM](Files/EF__GPIO8_8c.md#function-ef-gpio8-setim)**(uint32_t gpio_base, int mask) |
| int | **[EF_GPIO8_getRIS](Files/EF__GPIO8_8c.md#function-ef-gpio8-getris)**(uint32_t gpio_base) |
| int | **[EF_GPIO8_getMIS](Files/EF__GPIO8_8c.md#function-ef-gpio8-getmis)**(uint32_t gpio_base) |
| int | **[EF_GPIO8_getIM](Files/EF__GPIO8_8c.md#function-ef-gpio8-getim)**(uint32_t gpio_base) |
| void | **[EF_GPIO8_setICR](Files/EF__GPIO8_8c.md#function-ef-gpio8-seticr)**(uint32_t gpio_base, int mask) |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[EF_GPIO8_C](Files/EF__GPIO8_8c.md#define-ef-gpio8-c)**  |


## Functions Documentation

### function EF_GPIO8_readData

```cpp
int EF_GPIO8_readData(
    uint32_t gpio_base
)
```

reads the input value of the GPIOs 

**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 


**Return**: input GPIOs value 

### function EF_GPIO8_waitInput

```cpp
void EF_GPIO8_waitInput(
    uint32_t gpio_base,
    int data
)
```

wait until the input GPIOs have a certain value 

**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 
  * **data** the value to compare the input GPIOs with 


### function EF_GPIO8_wait_InputPin

```cpp
void EF_GPIO8_wait_InputPin(
    uint32_t gpio_base,
    int pin,
    int data
)
```

wait until a GPIO pin have a certain value 

**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 
  * **pin** pin number from 0 to 7 
  * **data** the value to compare the GPIO with 


### function EF_GPIO8_writeData

```cpp
void EF_GPIO8_writeData(
    uint32_t gpio_base,
    int data
)
```

drives the output value of the GPIOs 

**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 
  * **data** value to be driven to output GPIOs 


### function EF_GPIO8_writeAllDirection

```cpp
void EF_GPIO8_writeAllDirection(
    uint32_t gpio_base,
    int data
)
```

sets the direction of all GPIOs 

**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 
  * **data** GPIOs direction where 1 is output and 0 means input. It should be an eight bit value where each bit represents the direction of certain GPIO pin 


### function EF_GPIO8_readDirection

```cpp
int EF_GPIO8_readDirection(
    uint32_t gpio_base
)
```

gets the direction of all GPIOs 

**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 


**Return**: the direction of all GPIOs where each bit represents the direction of a GPIO pin 

### function EF_GPIO8_setPinDirection

```cpp
void EF_GPIO8_setPinDirection(
    uint32_t gpio_base,
    int pin,
    int dir
)
```

sets the direction of one GPIO pin 

**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 
  * **pin** pin number from 0 to 7 
  * **dir** GPIO pin direction where 1 is output and 0 means input. 


### function EF_GPIO8_setIM

```cpp
void EF_GPIO8_setIM(
    uint32_t gpio_base,
    int mask
)
```


**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 
  * **mask** The required mask value 


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


### function EF_GPIO8_getRIS

```cpp
int EF_GPIO8_getRIS(
    uint32_t gpio_base
)
```


**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 


**Return**: RIS register value 

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


### function EF_GPIO8_getMIS

```cpp
int EF_GPIO8_getMIS(
    uint32_t gpio_base
)
```


**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 


**Return**: MIS register value 

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


### function EF_GPIO8_getIM

```cpp
int EF_GPIO8_getIM(
    uint32_t gpio_base
)
```


**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 


**Return**: IM register value 

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


### function EF_GPIO8_setICR

```cpp
void EF_GPIO8_setICR(
    uint32_t gpio_base,
    int mask
)
```


**Parameters**: 

  * **gpio_base** The base memory address of GPIO registers. 
  * **mask** The required mask value 


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




## Macros Documentation

### define EF_GPIO8_C

```cpp
#define EF_GPIO8_C 
```


## Source code

```cpp
#ifndef EF_GPIO8_C
#define EF_GPIO8_C

#include <EF_GPIO8.h>


// inline int GPIO_readData(enum port_types port) __attribute__((always_inline));
int EF_GPIO8_readData(uint32_t gpio_base){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DATAI);
}

void EF_GPIO8_waitInput(uint32_t gpio_base, int data){
     EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while (EF_GPIO_readData(gpio_base) != data);
}

void EF_GPIO8_wait_InputPin(uint32_t gpio_base, int pin, int data){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while ((EF_GPIO_readData(gpio_base) & (1 << pin)) != data);
}

// inline void GPIO_writeData(enum port_types port, int data) __attribute__((always_inline));

void EF_GPIO8_writeData(uint32_t gpio_base, int data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->DATAO = data;
}

void EF_GPIO8_writeAllDirection(uint32_t gpio_base, int data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->DIR = data;
}


int EF_GPIO8_readDirection(uint32_t gpio_base){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DIR);
}


void EF_GPIO8_setPinDirection(uint32_t gpio_base, int pin, int dir){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    int directions  = gpio->DIR;
    if (dir == GPIO8_OUTPUT)
        directions |= (1 << pin);
    else
        directions &= ~(1 << pin);
    gpio->DIR = directions;
}

void EF_GPIO8_setIM(uint32_t gpio_base, int data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->im = data;
}

// Interrupts bits in RIS, MIS, IM, and ICR
 // bit 0: TX FIFO is Empty
 // bit 1: TX FIFO level is below the value in the TX FIFO Level Threshold Register
 // bit 2: RX FIFO is Full
 // bit 3: RX FIFO level is above the value in the RX FIFO Level Threshold Register
 // bit 4: line break
 // bit 5: match
 // bit 6: frame error
 // bit 7: parity error
 // bit 8: overrun 
 // bit 9: timeout 

int EF_GPIO8_getRIS(uint32_t gpio_base){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->ris);
}

int EF_GPIO8_getMIS(uint32_t gpio_base){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->mis);
}

void EF_GPIO8_setIM(uint32_t gpio_base, int mask){
   
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->im |= mask;
}

int EF_GPIO8_getIM(uint32_t gpio_base){

   EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->im);
}

void EF_GPIO8_setICR(uint32_t gpio_base, int mask){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    (gpio->icr) |= mask;
}   

#endif // GPIO_H
```


-------------------------------

Updated on 2024-04-06 at 14:43:24 +0200
