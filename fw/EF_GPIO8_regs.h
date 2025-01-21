/*
	Copyright 2024 Efabless Corp.

	Author: Efabless Corp. (ip_admin@efabless.com)

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

#ifndef EF_GPIO8REGS_H
#define EF_GPIO8REGS_H

 
/******************************************************************************
* Includes
******************************************************************************/
#include <stdint.h>

/******************************************************************************
* Macros and Constants
******************************************************************************/

#ifndef IO_TYPES
#define IO_TYPES
#define   __R     volatile const uint32_t
#define   __W     volatile       uint32_t
#define   __RW    volatile       uint32_t
#endif

#define EF_GPIO8_DATAI_REG_DATAI_BIT	((uint32_t)0)
#define EF_GPIO8_DATAI_REG_DATAI_MASK	((uint32_t)0xff)
#define EF_GPIO8_DATAI_REG_MAX_VALUE	((uint32_t)0xFF)

#define EF_GPIO8_DATAO_REG_DATAO_BIT	((uint32_t)0)
#define EF_GPIO8_DATAO_REG_DATAO_MASK	((uint32_t)0xff)
#define EF_GPIO8_DATAO_REG_MAX_VALUE	((uint32_t)0xFF)

#define EF_GPIO8_DIR_REG_DIR_BIT	((uint32_t)0)
#define EF_GPIO8_DIR_REG_DIR_MASK	((uint32_t)0xff)
#define EF_GPIO8_DIR_REG_MAX_VALUE	((uint32_t)0xFF)


#define EF_GPIO8_P0HI_FLAG	((uint32_t)0x1)
#define EF_GPIO8_P1HI_FLAG	((uint32_t)0x2)
#define EF_GPIO8_P2HI_FLAG	((uint32_t)0x4)
#define EF_GPIO8_P3HI_FLAG	((uint32_t)0x8)
#define EF_GPIO8_P4HI_FLAG	((uint32_t)0x10)
#define EF_GPIO8_P5HI_FLAG	((uint32_t)0x20)
#define EF_GPIO8_P6HI_FLAG	((uint32_t)0x40)
#define EF_GPIO8_P7HI_FLAG	((uint32_t)0x80)
#define EF_GPIO8_P0LO_FLAG	((uint32_t)0x100)
#define EF_GPIO8_P1LO_FLAG	((uint32_t)0x200)
#define EF_GPIO8_P2LO_FLAG	((uint32_t)0x400)
#define EF_GPIO8_P3LO_FLAG	((uint32_t)0x800)
#define EF_GPIO8_P4LO_FLAG	((uint32_t)0x1000)
#define EF_GPIO8_P5LO_FLAG	((uint32_t)0x2000)
#define EF_GPIO8_P6LO_FLAG	((uint32_t)0x4000)
#define EF_GPIO8_P7LO_FLAG	((uint32_t)0x8000)
#define EF_GPIO8_P0PE_FLAG	((uint32_t)0x10000)
#define EF_GPIO8_P1PE_FLAG	((uint32_t)0x20000)
#define EF_GPIO8_P2PE_FLAG	((uint32_t)0x40000)
#define EF_GPIO8_P3PE_FLAG	((uint32_t)0x80000)
#define EF_GPIO8_P4PE_FLAG	((uint32_t)0x100000)
#define EF_GPIO8_P5PE_FLAG	((uint32_t)0x200000)
#define EF_GPIO8_P6PE_FLAG	((uint32_t)0x400000)
#define EF_GPIO8_P7PE_FLAG	((uint32_t)0x800000)
#define EF_GPIO8_P0NE_FLAG	((uint32_t)0x1000000)
#define EF_GPIO8_P1NE_FLAG	((uint32_t)0x2000000)
#define EF_GPIO8_P2NE_FLAG	((uint32_t)0x4000000)
#define EF_GPIO8_P3NE_FLAG	((uint32_t)0x8000000)
#define EF_GPIO8_P4NE_FLAG	((uint32_t)0x10000000)
#define EF_GPIO8_P5NE_FLAG	((uint32_t)0x20000000)
#define EF_GPIO8_P6NE_FLAG	((uint32_t)0x40000000)
#define EF_GPIO8_P7NE_FLAG	((uint32_t)0x80000000)


          
/******************************************************************************
* Typedefs and Enums
******************************************************************************/
          
typedef struct _EF_GPIO8_TYPE_ {
	__R 	DATAI;
	__W 	DATAO;
	__W 	DIR;
	__R 	reserved_0[16317];
	__RW	IM;
	__R 	MIS;
	__R 	RIS;
	__W 	IC;
	__W 	GCLK;
} EF_GPIO8_TYPE;

typedef struct _EF_GPIO8_TYPE_ *EF_GPIO8_TYPE_PTR;     // Pointer to the register structure

  
/******************************************************************************
* Function Prototypes
******************************************************************************/



/******************************************************************************
* External Variables
******************************************************************************/




#endif

/******************************************************************************
* End of File
******************************************************************************/
          
          
