#include <stdio.h>
#include <string.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

#define COLS 5

int processMatrix(int matrix[][COLS], int rows)
{
    int sum = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < COLS; j++) {
            int k = (i % 2) + (j % 2);
            switch (k)
            {
            case 0:
                /* Even */
                matrix[i][j] *= 2;
                break;
            case 2:
                /* Odd */
                matrix[i][j] /= 2;
                break;
            default:
                break;
            }
            sum +=  matrix[i][j];
        }
    }
    return sum;
}
