/*
	Copyright 2025 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

*/

#ifndef EF_GPIO8_C
#define EF_GPIO8_C

#include <EF_GPIO8.h>

void EF_GPIO8_setGclkEnable (uint32_t gpio_base, uint32_t value){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->GCLK = value;
}

// inline uint32_t GPIO_readData(enum port_types port) __attribute__((always_inline));
uint32_t EF_GPIO8_readData(uint32_t gpio_base){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DATAI);
}

void EF_GPIO8_waitInput(uint32_t gpio_base, uint32_t data){
     EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while (EF_GPIO8_readData(gpio_base) != data);
}

void EF_GPIO8_wait_InputPin(uint32_t gpio_base, uint32_t pin, uint32_t data){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while ((EF_GPIO8_readData(gpio_base) & (1 << pin)) != data);
}

// inline void GPIO_writeData(enum port_types port, uint32_t data) __attribute__((always_inline));

void EF_GPIO8_writeData(uint32_t gpio_base, uint32_t data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->DATAO = data;
}

void EF_GPIO8_writeAllDirection(uint32_t gpio_base, uint32_t data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->DIR = data;
}


uint32_t EF_GPIO8_readDirection(uint32_t gpio_base){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DIR);
}


void EF_GPIO8_setPinDirection(uint32_t gpio_base, uint32_t pin, uint32_t dir){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    uint32_t directions  = gpio->DIR;
    if (dir == GPIO8_OUTPUT)
        directions |= (1 << pin);
    else
        directions &= ~(1 << pin);
    gpio->DIR = directions;
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

uint32_t EF_GPIO8_getRIS(uint32_t gpio_base){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->RIS);
}

uint32_t EF_GPIO8_getMIS(uint32_t gpio_base){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->MIS);
}

void EF_GPIO8_setIM(uint32_t gpio_base, uint32_t mask){
   
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->IM |= mask;
}

uint32_t EF_GPIO8_getIM(uint32_t gpio_base){

   EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->IM);
}

void EF_GPIO8_setICR(uint32_t gpio_base, uint32_t mask){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    (gpio->IC) |= mask;
}	

// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


void EF_GPIO8_setPinPackedDirection(uint32_t gpio_base, uint8_t pins, uint32_t dir){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    uint32_t directions  = gpio->DIR;
    if (dir == GPIO8_OUTPUT)
        directions |= pins;
    else
        directions &= ~pins;
    gpio->DIR = directions;
    return;
}

uint32_t EF_GPIO8_readPackedData(uint32_t gpio_base, uint8_t pins){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DATAI & pins);
}

void EF_GPIO8_writePackedData(uint32_t gpio_base, uint8_t pins, uint8_t data){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->DATAO = (gpio->DATAO & ~pins) | (data & pins);
    return;
}

/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


#endif // GPIO_H