#pragma once
#include <stdio.h>


#ifdef __cplusplus
extern "C" {
#endif
    //void swap(int *, int *);
    int *bubbleSort(int [], size_t , int(*)(int a, int b));
    int ascending(int, int);
    int descending(int, int);

#ifdef __cplusplus
}
#endif