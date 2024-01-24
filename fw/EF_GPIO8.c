#ifndef EF_GPIO_C
#define EF_GPIO_C

#include <EF_GPIO8.h>


// inline int GPIO_readData(enum port_types port) __attribute__((always_inline));
int EF_GPIO_readData(uint32_t gpio_base){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DATAI);
}

void EF_GPIO_waitInput(uint32_t gpio_base, int data){
     EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while (EF_GPIO_readData(gpio_base) != data);
}

void EF_GPIO_wait_InputPin(uint32_t gpio_base, int pin, int data){
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    while ((EF_GPIO_readData(gpio_base) & (1 << pin)) != data);
}

// inline void GPIO_writeData(enum port_types port, int data) __attribute__((always_inline));

void EF_GPIO_writeData(uint32_t gpio_base, int data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->DATAO = data;
}

void EF_GPIO_writeAllDirection(uint32_t gpio_base, int data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->DIR = data;
}


int EF_GPIO_readDirection(uint32_t gpio_base){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    return (gpio->DIR);
}


void EF_GPIO_setPinDirection(uint32_t gpio_base, int pin, int dir){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    int directions  = gpio->DIR;
    if (dir == GPIO_OUTPUT)
        directions |= (1 << pin);
    else
        directions &= ~(1 << pin);
    gpio->DIR = directions;
}

void EF_GPIO_setIM(uint32_t gpio_base, int data){
    
    EF_GPIO8_TYPE* gpio = (EF_GPIO8_TYPE*)gpio_base;
    gpio->im = data;
}
	

#endif // GPIO_H