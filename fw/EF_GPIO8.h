/*
	Copyright 2025 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

*/

/*! \file EF_GPIO8.h
    \brief C header file for GPIO8 APIs which contains the function prototypes 
    
*/

#ifndef EF_GPIO8_H
#define EF_GPIO8_H


/******************************************************************************
* Includes
******************************************************************************/
#include "EF_GPIO8_regs.h"
#include "EF_Driver_Common.h"

/******************************************************************************
* Macros and Constants
******************************************************************************/
#define GPIO8_INPUT 0
#define GPIO8_OUTPUT 1

#define EF_GPIO8_DATAI_MAX_VALUE    0x000000FF         // Maximum value of the DATAI register, 8 bits
#define EF_GPIO8_DATAO_MAX_VALUE    0x000000FF         // Maximum value of the DATAO register, 8 bits
#define EF_GPIO8_DIR_MAX_VALUE      0x000000FF         // Maximum value of the DIR register, 8 bits
#define EF_GPIO8_NUM_PINS           0x00000008         // Number of GPIO pins

/******************************************************************************
* Typedefs and Enums
******************************************************************************/



/******************************************************************************
* Function Prototypes
******************************************************************************/

//! sets the GCLK enable bit in the GPIO register to a certain value
    /*!
        \param [in] "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in] "value" The value of the GCLK enable bit

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_setGclkEnable (EF_GPIO8_TYPE_PTR gpio, uint32_t value);


//! reads the input value of the GPIOs
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [out]  "gpio_data" The value of the input GPIOs

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_readData(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_data);

//! wait until the input GPIOs have a certain value 
    /*!
        \param [in] "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in] "compare_value" the value to compare the input GPIOs with 

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_waitInput(EF_GPIO8_TYPE_PTR gpio, uint32_t compare_value);

//! wait until a  GPIO pin have a certain value 
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "pin" The pin number from 0 to 7 
        \param [in]   "compare_value" The value to compare the GPIO with 

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_wait_InputPin(EF_GPIO8_TYPE_PTR gpio, uint32_t pin, uint32_t compare_value);

//! drives the output value of the GPIOs
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "data" value to be driven to output GPIOs 

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_writeData(EF_GPIO8_TYPE_PTR gpio, uint32_t data);

//! sets the direction of all GPIOs 
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "data" GPIOs direction where 1 is output and 0 means input. It should be an eight bit value where each bit represents the direction of certain GPIO pin 

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_writeAllDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t data);

//! gets the direction of all GPIOs 
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [out]  "gpio_dir" GPIOs direction where 1 is output and 0 means input. It should be an eight bit value where each bit represents the direction of certain GPIO pin

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_readDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_dir);

//! sets the direction of one GPIO pin 
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "pin" pin number from 0 to 7 
        \param [in]   "dir" GPIO pin direction where 1 is output and 0 means input.

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_setPinDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t pin, uint32_t dir);

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
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [out]  "gpio_ris" The value of the RIS register

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_getRIS(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_ris);


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
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [out]  "gpio_mis" The value of the MIS register

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_getMIS(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_mis);


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
        \param [in]   gpio An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "mask" The required mask value

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_setIM(EF_GPIO8_TYPE_PTR gpio, uint32_t mask);


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
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [out]  "gpio_im" The value of the IM register

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_getIM(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_im);


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
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "mask" The required mask value

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_setICR(EF_GPIO8_TYPE_PTR gpio, uint32_t mask);




// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/

//! This function sets the direction of a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it sets the direction of the pin(s) to the required value.
/// \note All the specified pins are set to the same direction (dir).
/// \note  The function does not affect the direction of the other pins in the port.
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "pins" The bit-packed representation of the pin(s).
        \param [in]   "dir" The required direction value

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_setPinPackedDirection(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint32_t dir);


//! This function reads the data from a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it reads the data from the pin(s).
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "pins" The bit-packed representation of the pin(s).
        \param [out]  "packed_data" The data read from the pin(s)

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_readPackedData(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint32_t* packed_data);

//! This function writes the data to a specified set of pins in a GPIO port. Given a bit-packed representation of the pin(s), it writes the data to the pin(s).
//! Note that all the specified pins are set to the corresponding value of the corresponding bit in the data parameter.
    /*!
        \param [in]   "gpio" An \ref EF_GPIO8_TYPE pointer, which points to the base memory address of GPIO registers. \ref EF_GPIO8_TYPE is a structure that contains the GPIO registers.
        \param [in]   "pins" The bit-packed representation of the pin(s).
        \param [in]   "data" The data to be written to the pin(s)

        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
EF_DRIVER_STATUS EF_GPIO8_writePackedData(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint8_t data);



/******************************************************************************
* External Variables
******************************************************************************/




#endif // EF_GPIO8_H

/******************************************************************************
* End of File
******************************************************************************/
