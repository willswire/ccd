#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

int getMode(int *array, int size)
{
    if (array == NULL)
        return -2;

    int max = array[0];
 
    for (int i = 1; i < size; i++)
        if (array[i] > max)
            max = array[i];
    
    int result[size];
    memset(result, 0, size * sizeof(int));

    if (result == NULL)
        return -3;

    for (int i = 0; i < size; i++) {
        result[array[i]]++;
    }

    int mode = -1;
    for (int i = 0; i < size; i++) {
        mode = (result[i] > mode) ? i : mode;
    }

    return mode;
}
