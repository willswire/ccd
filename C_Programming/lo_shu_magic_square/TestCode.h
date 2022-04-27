#pragma once

#include <stdio.h>
// Global constants
#define ROWS 3  // The number of rows in the array
#define COLS 3  // The number of columns in the array
#define MIN 1  // The value of the smallest number
#define MAX 9  // The value of the largest number


#ifdef __cplusplus
extern "C" {
#endif
    // Task One
    int isMagicSquare(int values[][COLS]);

#ifdef __cplusplus
}
#endif