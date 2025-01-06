#ifndef EF_GPIO8_C
#define EF_GPIO8_C

#include <EF_GPIO8.h>

void EF_GPIO8_setGclkEnable (uint32_t gpio_base, int value){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->GCLK = value;
}

// inline int GPIO_readData(enum port_types port) __attribute__((always_inline));
int EF_GPIO8_readData(uint32_t gpio_base){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DATAI);
}

void EF_GPIO8_waitInput(uint32_t gpio_base, int data){
     EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while (EF_GPIO8_readData(gpio_base) != data);
}

void EF_GPIO8_wait_InputPin(uint32_t gpio_base, int pin, int data){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while ((EF_GPIO8_readData(gpio_base) & (1 << pin)) != data);
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
    return (gpio->RIS);
}

int EF_GPIO8_getMIS(uint32_t gpio_base){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->MIS);
}

void EF_GPIO8_setIM(uint32_t gpio_base, int mask){
   
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->IM |= mask;
}

int EF_GPIO8_getIM(uint32_t gpio_base){

   EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->IM);
}

void EF_GPIO8_setICR(uint32_t gpio_base, int mask){

    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    (gpio->IC) |= mask;
}	

// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


void EF_GPIO8_setPinPackedDirection(uint32_t gpio_base, uint8_t pins, int dir){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    int directions  = gpio->DIR;
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