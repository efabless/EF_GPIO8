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



void EF_GPIO8_setGclkEnable (EF_GPIO8_TYPE_PTR gpio, uint32_t value){
    
    gpio->GCLK = value;
}

void EF_GPIO8_readData(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_data){

    gpio_data = &(gpio->DATAI);

}

void EF_GPIO8_waitInput(EF_GPIO8_TYPE_PTR gpio, uint32_t compare_value){

    uint32_t gpio_data;

    do {
        EF_GPIO8_readData(gpio, &gpio_data);
    } while (gpio_data != compare_value);
}

void EF_GPIO8_wait_InputPin(EF_GPIO8_TYPE_PTR gpio, uint32_t pin, uint32_t compare_value){
    uint32_t gpio_data;

    do {
        EF_GPIO8_readData(gpio, &gpio_data);

    } while ((gpio_data & (1 << pin)) != compare_value);
}

void EF_GPIO8_writeData(EF_GPIO8_TYPE_PTR gpio, uint32_t data){
    
    gpio->DATAO = data;
}

void EF_GPIO8_writeAllDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t data){
    
    
    gpio->DIR = data;
}


void EF_GPIO8_readDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_dir){
    
    gpio_dir = &(gpio->DIR);

}

void EF_GPIO8_setPinDirection(EF_GPIO8_TYPE_PTR gpio, uint32_t pin, uint32_t gpio_dir){
    
    
    uint32_t directions  = gpio->DIR;
    if (gpio_dir == GPIO8_OUTPUT)
        directions |= (1 << pin);
    else
        directions &= ~(1 << pin);
    gpio->DIR = directions;
}

void EF_GPIO8_getRIS(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_ris){

    gpio_ris = &(gpio->RIS);
}

void EF_GPIO8_getMIS(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_mis){

    gpio_mis = &(gpio->MIS);
}

void EF_GPIO8_setIM(EF_GPIO8_TYPE_PTR gpio, uint32_t mask){
    
    gpio->IM |= mask;
}

void EF_GPIO8_getIM(EF_GPIO8_TYPE_PTR gpio, uint32_t* gpio_im){
    
    gpio_im = &(gpio->IM);
}

void EF_GPIO8_setICR(EF_GPIO8_TYPE_PTR gpio, uint32_t mask){
    
    gpio->IC |= mask;
}	

// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


void EF_GPIO8_setPinPackedDirection(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint32_t dir){
    
    
    uint32_t directions  = gpio->DIR;
    if (dir == GPIO8_OUTPUT)
        directions |= pins;
    else
        directions &= ~pins;
    gpio->DIR = directions;
    return;
}

void EF_GPIO8_readPackedData(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint32_t* packed_data){

    packed_data = &(gpio->DATAI);
}

void EF_GPIO8_writePackedData(EF_GPIO8_TYPE_PTR gpio, uint8_t pins, uint8_t data){
    
    gpio->DATAO = (gpio->DATAO & ~pins) | (data & pins);
    return;
}


/******************************************************************************
* Static Function Definitions
******************************************************************************/





#endif // EF_GPIO8_C

/******************************************************************************
* End of File
******************************************************************************/
