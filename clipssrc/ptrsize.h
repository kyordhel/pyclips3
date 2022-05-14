#ifndef _H_ptrsize
#define _H_ptrsize

#include <stdint.h>

#if UINTPTR_MAX == 0xFFFF
	#define PTR16
	#define PTR_SIZE 16
#elif UINTPTR_MAX == 0xFFFFFFFF
	#define PTR32
	#define PTR_SIZE 32
#elif UINTPTR_MAX == 0xFFFFFFFFFFFFFFFFu
	#define PTR64
	#define PTR_SIZE 64
#else
	#error Unknown pointer size
#endif

#endif //_H_ptrsize
