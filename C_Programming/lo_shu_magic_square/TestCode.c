#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include"TestCode.h"

// Refer to README.md for the problem instructions

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int isMagicSquare(int values[][COLS])
{
    const int valid[9] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int test[9];

    int k = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            test[k] = values[i][j];
            k++;
        }
    }

    qsort(test, 9, sizeof(int), cmpfunc);

    int res = memcmp(valid, test, (sizeof(int) * 9));
    if (res != 0)
        return 0;

    // Horizonal sums
    int sumA = values[0][0] + values[0][1] + values[0][2];
    int sumB = values[1][0] + values[1][1] + values[1][2];
    int sumC = values[2][0] + values[2][1] + values[2][2];

    // Vertical sums
    int sumD = values[0][0] + values[1][0] + values[2][0];
    int sumE = values[0][1] + values[1][1] + values[2][1];
    int sumF = values[0][2] + values[1][2] + values[2][2];

    // Diagonal sums
    int sumG = values[0][0] + values[1][1] + values[2][2];
    int sumH = values[2][0] + values[1][1] + values[0][2];

    return !(sumA - sumB + sumC - sumD + sumE - sumF + sumG - sumH);
}


