/*! \file EF_GPIO8.h
    \brief C header file for GPIO8 APIs which contains the function prototypes 
    
*/

#ifndef EF_GPIO8_H
#define EF_GPIO8_H

#include <EF_GPIO8_regs.h>
#include <stdint.h>

#define GPIO8_INPUT 0
#define GPIO8_OUTPUT 1

void EF_GPIO8_setGclkEnable (uint32_t gpio_base, uint32_t value);


//! reads the input value of the GPIOs
    /*!
      \param gpio_base The base memory address of GPIO registers.
       \return input GPIOs value 
    */
uint32_t EF_GPIO8_readData(uint32_t gpio_base);

//! wait until the input GPIOs have a certain value 
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param data the value to compare the input GPIOs with 
    */
void EF_GPIO8_waitInput(uint32_t gpio_base, uint32_t data);

//! wait until a  GPIO pin have a certain value 
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param pin pin number from 0 to 7 
      \param data the value to compare the GPIO with 
    */
void EF_GPIO8_wait_InputPin(uint32_t gpio_base, uint32_t pin, uint32_t data);

//! drives the output value of the GPIOs
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param data value to be driven to output GPIOs 
    */
void EF_GPIO8_writeData(uint32_t gpio_base, uint32_t data);

//! sets the direction of all GPIOs 
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param data GPIOs direction where 1 is output and 0 means input. It should be an eight bit value where each bit represents the direction of certain GPIO pin 
    */
void EF_GPIO8_writeAllDirection(uint32_t gpio_base, uint32_t data);

//! gets the direction of all GPIOs 
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \return the direction of all GPIOs where each bit represents the direction of a GPIO pin 
    */
uint32_t EF_GPIO8_readDirection(uint32_t gpio_base);

//! sets the direction of one GPIO pin 
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param pin pin number from 0 to 7 
      \param dir GPIO pin direction where 1 is output and 0 means input.
    */
void EF_GPIO8_setPinDirection(uint32_t gpio_base, uint32_t pin, uint32_t dir);

//! returns the value of the Raw Interrupt Status Register
//! *  bit 0 P0HI : Pin 0 is high
//! *  bit 1 P1HI : Pin 1 is high
//! *  bit 2 P2HI : Pin 2 is high
//! *  bit 3 P3HI : Pin 3 is high
//! *  bit 4 P4HI : Pin 4 is high
//! *  bit 5 P5HI : Pin 5 is high
//! *  bit 6 P6HI : Pin 6 is high
//! *  bit 7 P7HI : Pin 7 is high
//! *  bit 8 P0LO : Pin 0 is low
//! *  bit 9 P1LO : Pin 1 is low
//! *  bit 10 P2LO : Pin 2 is low
//! *  bit 11 P3LO : Pin 3 is low
//! *  bit 12 P4LO : Pin 4 is low
//! *  bit 13 P5LO : Pin 5 is low
//! *  bit 14 P6LO : Pin 6 is low
//! *  bit 15 P7LO : Pin 7 is low
//! *  bit 16 P0PE : Pin 0 has observed a rising edge
//! *  bit 17 P1PE : Pin 1 has observed a rising edge
//! *  bit 18 P2PE : Pin 2 has observed a rising edge
//! *  bit 19 P3PE : Pin 3 has observed a rising edge
//! *  bit 20 P4PE : Pin 4 has observed a rising edge
//! *  bit 21 P5PE : Pin 5 has observed a rising edge
//! *  bit 22 P6PE : Pin 6 has observed a rising edge
//! *  bit 23 P7PE : Pin 7 has observed a rising edge
//! *  bit 24 P0NE : Pin 0 has observed a falling edge
//! *  bit 25 P1NE : Pin 1 has observed a falling edge
//! *  bit 26 P2NE : Pin 2 has observed a falling edge
//! *  bit 27 P3NE : Pin 3 has observed a falling edge
//! *  bit 28 P4NE : Pin 4 has observed a falling edge
//! *  bit 29 P5NE : Pin 5 has observed a falling edge
//! *  bit 30 P6NE : Pin 6 has observed a falling edge
//! *  bit 31 P7NE : Pin 7 has observed a falling edge
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \return RIS register value 
    */
uint32_t EF_GPIO8_getRIS(uint32_t gpio_base);


//! returns the value of the Masked Interrupt Status Register
//! *  bit 0 P0HI : Pin 0 is high
//! *  bit 1 P1HI : Pin 1 is high
//! *  bit 2 P2HI : Pin 2 is high
//! *  bit 3 P3HI : Pin 3 is high
//! *  bit 4 P4HI : Pin 4 is high
//! *  bit 5 P5HI : Pin 5 is high
//! *  bit 6 P6HI : Pin 6 is high
//! *  bit 7 P7HI : Pin 7 is high
//! *  bit 8 P0LO : Pin 0 is low
//! *  bit 9 P1LO : Pin 1 is low
//! *  bit 10 P2LO : Pin 2 is low
//! *  bit 11 P3LO : Pin 3 is low
//! *  bit 12 P4LO : Pin 4 is low
//! *  bit 13 P5LO : Pin 5 is low
//! *  bit 14 P6LO : Pin 6 is low
//! *  bit 15 P7LO : Pin 7 is low
//! *  bit 16 P0PE : Pin 0 has observed a rising edge
//! *  bit 17 P1PE : Pin 1 has observed a rising edge
//! *  bit 18 P2PE : Pin 2 has observed a rising edge
//! *  bit 19 P3PE : Pin 3 has observed a rising edge
//! *  bit 20 P4PE : Pin 4 has observed a rising edge
//! *  bit 21 P5PE : Pin 5 has observed a rising edge
//! *  bit 22 P6PE : Pin 6 has observed a rising edge
//! *  bit 23 P7PE : Pin 7 has observed a rising edge
//! *  bit 24 P0NE : Pin 0 has observed a falling edge
//! *  bit 25 P1NE : Pin 1 has observed a falling edge
//! *  bit 26 P2NE : Pin 2 has observed a falling edge
//! *  bit 27 P3NE : Pin 3 has observed a falling edge
//! *  bit 28 P4NE : Pin 4 has observed a falling edge
//! *  bit 29 P5NE : Pin 5 has observed a falling edge
//! *  bit 30 P6NE : Pin 6 has observed a falling edge
//! *  bit 31 P7NE : Pin 7 has observed a falling edge
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \return MIS register value 
    */
uint32_t EF_GPIO8_getMIS(uint32_t gpio_base);


//! sets the value of the Interrupts Masking Register; which enable and disables interrupts
//! *  bit 0 P0HI : Pin 0 is high
//! *  bit 1 P1HI : Pin 1 is high
//! *  bit 2 P2HI : Pin 2 is high
//! *  bit 3 P3HI : Pin 3 is high
//! *  bit 4 P4HI : Pin 4 is high
//! *  bit 5 P5HI : Pin 5 is high
//! *  bit 6 P6HI : Pin 6 is high
//! *  bit 7 P7HI : Pin 7 is high
//! *  bit 8 P0LO : Pin 0 is low
//! *  bit 9 P1LO : Pin 1 is low
//! *  bit 10 P2LO : Pin 2 is low
//! *  bit 11 P3LO : Pin 3 is low
//! *  bit 12 P4LO : Pin 4 is low
//! *  bit 13 P5LO : Pin 5 is low
//! *  bit 14 P6LO : Pin 6 is low
//! *  bit 15 P7LO : Pin 7 is low
//! *  bit 16 P0PE : Pin 0 has observed a rising edge
//! *  bit 17 P1PE : Pin 1 has observed a rising edge
//! *  bit 18 P2PE : Pin 2 has observed a rising edge
//! *  bit 19 P3PE : Pin 3 has observed a rising edge
//! *  bit 20 P4PE : Pin 4 has observed a rising edge
//! *  bit 21 P5PE : Pin 5 has observed a rising edge
//! *  bit 22 P6PE : Pin 6 has observed a rising edge
//! *  bit 23 P7PE : Pin 7 has observed a rising edge
//! *  bit 24 P0NE : Pin 0 has observed a falling edge
//! *  bit 25 P1NE : Pin 1 has observed a falling edge
//! *  bit 26 P2NE : Pin 2 has observed a falling edge
//! *  bit 27 P3NE : Pin 3 has observed a falling edge
//! *  bit 28 P4NE : Pin 4 has observed a falling edge
//! *  bit 29 P5NE : Pin 5 has observed a falling edge
//! *  bit 30 P6NE : Pin 6 has observed a falling edge
//! *  bit 31 P7NE : Pin 7 has observed a falling edge
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param mask The required mask value
    */
void EF_GPIO8_setIM(uint32_t gpio_base, uint32_t mask);


//! returns the value of the Interrupts Masking Register; which enable and disables interrupts
//! *  bit 0 P0HI : Pin 0 is high
//! *  bit 1 P1HI : Pin 1 is high
//! *  bit 2 P2HI : Pin 2 is high
//! *  bit 3 P3HI : Pin 3 is high
//! *  bit 4 P4HI : Pin 4 is high
//! *  bit 5 P5HI : Pin 5 is high
//! *  bit 6 P6HI : Pin 6 is high
//! *  bit 7 P7HI : Pin 7 is high
//! *  bit 8 P0LO : Pin 0 is low
//! *  bit 9 P1LO : Pin 1 is low
//! *  bit 10 P2LO : Pin 2 is low
//! *  bit 11 P3LO : Pin 3 is low
//! *  bit 12 P4LO : Pin 4 is low
//! *  bit 13 P5LO : Pin 5 is low
//! *  bit 14 P6LO : Pin 6 is low
//! *  bit 15 P7LO : Pin 7 is low
//! *  bit 16 P0PE : Pin 0 has observed a rising edge
//! *  bit 17 P1PE : Pin 1 has observed a rising edge
//! *  bit 18 P2PE : Pin 2 has observed a rising edge
//! *  bit 19 P3PE : Pin 3 has observed a rising edge
//! *  bit 20 P4PE : Pin 4 has observed a rising edge
//! *  bit 21 P5PE : Pin 5 has observed a rising edge
//! *  bit 22 P6PE : Pin 6 has observed a rising edge
//! *  bit 23 P7PE : Pin 7 has observed a rising edge
//! *  bit 24 P0NE : Pin 0 has observed a falling edge
//! *  bit 25 P1NE : Pin 1 has observed a falling edge
//! *  bit 26 P2NE : Pin 2 has observed a falling edge
//! *  bit 27 P3NE : Pin 3 has observed a falling edge
//! *  bit 28 P4NE : Pin 4 has observed a falling edge
//! *  bit 29 P5NE : Pin 5 has observed a falling edge
//! *  bit 30 P6NE : Pin 6 has observed a falling edge
//! *  bit 31 P7NE : Pin 7 has observed a falling edge
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \return IM register value 
    */
uint32_t EF_GPIO8_getIM(uint32_t gpio_base);


//! sets the value of the Interrupts Clear Register; write 1 to clear the flag
//! *  bit 0 P0HI : Pin 0 is high
//! *  bit 1 P1HI : Pin 1 is high
//! *  bit 2 P2HI : Pin 2 is high
//! *  bit 3 P3HI : Pin 3 is high
//! *  bit 4 P4HI : Pin 4 is high
//! *  bit 5 P5HI : Pin 5 is high
//! *  bit 6 P6HI : Pin 6 is high
//! *  bit 7 P7HI : Pin 7 is high
//! *  bit 8 P0LO : Pin 0 is low
//! *  bit 9 P1LO : Pin 1 is low
//! *  bit 10 P2LO : Pin 2 is low
//! *  bit 11 P3LO : Pin 3 is low
//! *  bit 12 P4LO : Pin 4 is low
//! *  bit 13 P5LO : Pin 5 is low
//! *  bit 14 P6LO : Pin 6 is low
//! *  bit 15 P7LO : Pin 7 is low
//! *  bit 16 P0PE : Pin 0 has observed a rising edge
//! *  bit 17 P1PE : Pin 1 has observed a rising edge
//! *  bit 18 P2PE : Pin 2 has observed a rising edge
//! *  bit 19 P3PE : Pin 3 has observed a rising edge
//! *  bit 20 P4PE : Pin 4 has observed a rising edge
//! *  bit 21 P5PE : Pin 5 has observed a rising edge
//! *  bit 22 P6PE : Pin 6 has observed a rising edge
//! *  bit 23 P7PE : Pin 7 has observed a rising edge
//! *  bit 24 P0NE : Pin 0 has observed a falling edge
//! *  bit 25 P1NE : Pin 1 has observed a falling edge
//! *  bit 26 P2NE : Pin 2 has observed a falling edge
//! *  bit 27 P3NE : Pin 3 has observed a falling edge
//! *  bit 28 P4NE : Pin 4 has observed a falling edge
//! *  bit 29 P5NE : Pin 5 has observed a falling edge
//! *  bit 30 P6NE : Pin 6 has observed a falling edge
//! *  bit 31 P7NE : Pin 7 has observed a falling edge
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param mask The required mask value
    */
void EF_GPIO8_setICR(uint32_t gpio_base, uint32_t mask);




// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


//! This function sets the direction of a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it sets the direction of the pin(s) to the required value.
//! Note that all the specified pins are set to the same direction (dir).
//! Note that the function does not affect the direction of the other pins in the port.
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param pins The bit-packed representation of the pin(s).
      \param dir The required direction value
    */
void EF_GPIO8_setPinPackedDirection(uint32_t gpio_base, uint8_t pins, uint32_t dir);


//! This function reads the data from a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it reads the data from the pin(s).
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param pins The bit-packed representation of the pin(s).
      \return The data read from the pin(s)
    */
uint32_t EF_GPIO8_readPackedData(uint32_t gpio_base, uint8_t pins);

//! This function writes the data to a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it writes the data to the pin(s).
//! Note that all the specified pins are set to the corresponding value of the corresponding bit in the data parameter.
    /*!
      \param gpio_base The base memory address of GPIO registers.
      \param pins The bit-packed representation of the pin(s).
      \param data The data to be written to the pin(s)
    */
void EF_GPIO8_writePackedData(uint32_t gpio_base, uint8_t pins, uint8_t data);


/******************************************************************************************************************************************/
/******************************************************************************************************************************************/




#endif