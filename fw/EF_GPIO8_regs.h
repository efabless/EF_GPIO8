/*
	Copyright 2023 Efabless Corp.

	Author: Mohamed Shalan (mshalan@aucegypt.edu)

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

#ifndef EF_GPIO8REGS_H
#define EF_GPIO8REGS_H

#ifndef IO_TYPES
#define IO_TYPES
#define   __R     volatile const unsigned int
#define   __W     volatile       unsigned int
#define   __RW    volatile       unsigned int
#endif


#define EF_GPIO8_P0HI_FLAG	0x1
#define EF_GPIO8_P1HI_FLAG	0x2
#define EF_GPIO8_P2HI_FLAG	0x4
#define EF_GPIO8_P3HI_FLAG	0x8
#define EF_GPIO8_P4HI_FLAG	0x10
#define EF_GPIO8_P5HI_FLAG	0x20
#define EF_GPIO8_P6HI_FLAG	0x40
#define EF_GPIO8_P7HI_FLAG	0x80
#define EF_GPIO8_P0LO_FLAG	0x100
#define EF_GPIO8_P1LO_FLAG	0x200
#define EF_GPIO8_P2LO_FLAG	0x400
#define EF_GPIO8_P3LO_FLAG	0x800
#define EF_GPIO8_P4LO_FLAG	0x1000
#define EF_GPIO8_P5LO_FLAG	0x2000
#define EF_GPIO8_P6LO_FLAG	0x4000
#define EF_GPIO8_P7LO_FLAG	0x8000
#define EF_GPIO8_P0PE_FLAG	0x10000
#define EF_GPIO8_P1PE_FLAG	0x20000
#define EF_GPIO8_P2PE_FLAG	0x40000
#define EF_GPIO8_P3PE_FLAG	0x80000
#define EF_GPIO8_P4PE_FLAG	0x100000
#define EF_GPIO8_P5PE_FLAG	0x200000
#define EF_GPIO8_P6PE_FLAG	0x400000
#define EF_GPIO8_P7PE_FLAG	0x800000
#define EF_GPIO8_P0NE_FLAG	0x1000000
#define EF_GPIO8_P1NE_FLAG	0x2000000
#define EF_GPIO8_P2NE_FLAG	0x4000000
#define EF_GPIO8_P3NE_FLAG	0x8000000
#define EF_GPIO8_P4NE_FLAG	0x10000000
#define EF_GPIO8_P5NE_FLAG	0x20000000
#define EF_GPIO8_P6NE_FLAG	0x40000000
#define EF_GPIO8_P7NE_FLAG	0x80000000

typedef struct _EF_GPIO8_TYPE_ {
	__R 	DATAI;
	__W 	DATAO;
	__W 	DIR;
	__R 	reserved[957];
	__RW	im;
	__R 	mis;
	__R 	ris;
	__W 	icr;
} EF_GPIO8_TYPE;

#endif

