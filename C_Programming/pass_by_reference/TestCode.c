#include <stdio.h>
#include <stdlib.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

void refFunction(int *first, int *second, int action)
{
    switch (action)
    {
    case 1:
        if (*second < *first) {
            int temp = *first;
            *first = *second;
            *second = temp;
        }
        break;
    case 2:
        if (*first < *second) {
            int temp = *first;
            *first = *second;
            *second = temp;
        }
        break;
    case 3:
        *first *= 2;
        *second *= 2;
        break;
    default:
        *first = 0;
        *second = 0;
        break;
    }
}
