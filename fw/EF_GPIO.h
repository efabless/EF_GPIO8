#ifndef EF_GPIO_H
#define EF_GPIO_H

#include <EF_GPIO_regs.h>
#include <stdint.h>

#define GPIO_INPUT 0
#define GPIO_OUTPUT 1

int EF_GPIO_readData(uint32_t gpio_base);

void EF_GPIO_waitInput(uint32_t gpio_base, int data);

void EF_GPIO_wait_InputPin(uint32_t gpio_base, int pin, int data);

void EF_GPIO_writeData(uint32_t gpio_base, int data);

void EF_GPIO_writeAllDirection(uint32_t gpio_base, int data);

int EF_GPIO_readDirection(uint32_t gpio_base);

void EF_GPIO_setPinDirection(uint32_t gpio_base, int pin, int dir);

void EF_GPIO_setIM(uint32_t gpio_base, int data);

#endif