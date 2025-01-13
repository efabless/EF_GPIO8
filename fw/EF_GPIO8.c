/*
	Copyright 2025 Efabless Corp.


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

/*! \file EF_GPIO8.c
    \brief C file for GPIO8 APIs which contains the function Implementations
    
*/

#ifndef EF_GPIO8_C
#define EF_GPIO8_C


/******************************************************************************
* Includes
******************************************************************************/
#include "EF_GPIO8.h"



/******************************************************************************
* File-Specific Macros and Constants
******************************************************************************/



/******************************************************************************
* Static Variables
******************************************************************************/



/******************************************************************************
* Static Function Prototypes
******************************************************************************/



/******************************************************************************
* Function Definitions
******************************************************************************/



EF_DRIVER_STATUS EF_GPIO8_setGclkEnable (EF_GPIO8_TYPE_PTR gpio, uint32_t value){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if ((value < (uint32_t)0x0) || (value > (uint32_t)0x1)) {  
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if value is out of range
    }else {
        gpio->GCLK = value;                     // Set the GCLK enable bit to the given value
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_readData(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_data){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (gpio_data == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if gpio_data is NULL
                                                // i.e. there is no memory location to store the value
    }else {
        *gpio_data = gpio->DATAI;               // Read the input value of the GPIOs
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_waitInput(EF_GPIO8_TYPE_PTR gpio, uint32_t compare_value){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;                 // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (compare_value > EF_GPIO8_DATAI_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;                 // Return EF_DRIVER_ERROR_PARAMETER if compare_value is out of range
    }else {
        uint32_t gpio_data;
        do {
            status = EF_GPIO8_readData(gpio, &gpio_data);   // Read the input value of the GPIOs
        } while ((status == EF_DRIVER_OK) && (gpio_data != compare_value));               // Wait until the input GPIOs have the required value
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_wait_InputPin(EF_GPIO8_TYPE_PTR gpio, uint32_t pin, uint32_t compare_value){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;                 // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (pin > (uint32_t)7) {
        status = EF_DRIVER_ERROR_PARAMETER;                 // Return EF_DRIVER_ERROR_PARAMETER if pin is out of range
    }else if (compare_value > EF_GPIO8_DATAI_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;                 // Return EF_DRIVER_ERROR_PARAMETER if compare_value is out of range
    }else {
        uint32_t gpio_data;
        do {
            status = EF_GPIO8_readData(gpio, &gpio_data);   // Read the input value of the GPIOs
        } while ((status == EF_DRIVER_OK) && ((gpio_data & ((uint32_t)0x1 << pin)) != compare_value));  // Wait until the input GPIO pin has the required value
    }

    return status;
}


EF_DRIVER_STATUS EF_GPIO8_writeData(EF_GPIO8_TYPE_PTR gpio, uint32_t data){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL

    }else if (data > EF_GPIO8_DATAO_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if data is out of range
    }else {
        gpio->DATAO = data;                     // Drive the output value of the GPIOs
    }

    return status;
}


EF_DRIVER_STATUS EF_GPIO8_writeAllDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t data){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (data > EF_GPIO8_DIR_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if data is out of range
    }else {
        gpio->DIR = data;                     // Set the direction of all GPIOs
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_readDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_dir){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (gpio_dir == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio_dir is NULL
                                                // i.e. there is no memory location to store the value
    }else {
        *gpio_dir = gpio->DIR;                // Read the direction of all GPIOs
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_setPinDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t pin, uint32_t gpio_dir){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (pin > EF_GPIO8_NUM_PINS) {
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if pin is out of range
    }else if (gpio_dir > (uint32_t)0x1) {
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio_dir is out of range
    }else {
        uint32_t directions  = gpio->DIR;
        if (gpio_dir == GPIO8_OUTPUT)
            {directions |= ((uint32_t)0x1 << pin);}
        else
            {directions &= ~((uint32_t)0x1 << pin);}
        gpio->DIR = directions;                 // Set the direction of the specified GPIO pin
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_getRIS(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_ris){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (gpio_ris == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio_ris is NULL
                                                // i.e. there is no memory location to store the value
    }else {
        *gpio_ris = gpio->RIS;                // Read the value of the RIS register
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_getMIS(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_mis){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (gpio_mis == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio_mis is NULL
                                                // i.e. there is no memory location to store the value
    }else {
        *gpio_mis = gpio->MIS;                // Read the value of the MIS register
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_setIM(EF_GPIO8_TYPE_PTR gpio, uint32_t mask){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else {
        gpio->IM = mask;                        // Set the IM register with the required mask value
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_getIM(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_im){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (gpio_im == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio_im is NULL
                                                // i.e. there is no memory location to store the value
    }else {
        *gpio_im = gpio->IM;                  // Read the value of the IM register
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_setICR(EF_GPIO8_TYPE_PTR gpio, uint32_t mask){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else {
        gpio->IC = mask;                       // Set the IC register with the required mask value
    }

    return status;
}


// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


EF_DRIVER_STATUS EF_GPIO8_setPinPackedDirection(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint32_t dir){
    
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (dir > (uint32_t)0x1) {
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if dir is out of range
    }else {
        uint32_t directions  = gpio->DIR;
        if (dir == GPIO8_OUTPUT)
            {directions |= pins;}
        else
            {directions &= ~pins;}
        gpio->DIR = directions;                 // Set the direction of the specified set of pins
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_readPackedData(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint32_t* packed_data){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else if (packed_data == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if packed_data is NULL
                                                // i.e. there is no memory location to store the value
    }else {
        
        *packed_data = gpio->DATAI & pins;      // Read the data from the specified set of pins
    }

    return status;
}

EF_DRIVER_STATUS EF_GPIO8_writePackedData(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint8_t data){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (gpio == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;    // Return EF_DRIVER_ERROR_PARAMETER if gpio is NULL
    }else {
        gpio->DATAO = (gpio->DATAO & (~pins)) | (data & pins);  // Write the data to the specified set of pins
    }

    return status;
}


/******************************************************************************
* Static Function Definitions
******************************************************************************/





#endif // EF_GPIO8_C

/******************************************************************************
* End of File
******************************************************************************/
