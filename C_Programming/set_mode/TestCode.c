#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

int getMode(int *array, int size)
{
    if (array == NULL)
        return -2;

    int result[size + 1];
    memset(result, 0, (size + 1) * sizeof(int));

    if (result == NULL)
        return -3;

    for (int i = 0; i < size; i++) {
        int num = *(array + i);
        *(result + num) += 1;
    }

    int mode = -1;
    int modeCount = 0;
    for (int i = 0; i < size; i++) {
        if (*(result + i) > mode) {
            mode = i;
            modeCount = *(result + i);
        }
    }

    if (modeCount == 1)
        return -1;

    return mode;
}
