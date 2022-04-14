#include <stdio.h>
#include <stdlib.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions


int arrayManipulate(int *arr, int size)
{
    if (arr == NULL || size < 2) {
        return -1;
    }

    int *ptr = arr;
    for (int i = 0; i < size; i++){
        int val = *ptr;

        if ((val % 2 == 0) && (val > 6)) {
            val = pow(val, 2);
        } else if ((val % 2 == 1) || (val > 2)) {
            val *= 2;
        }

        *(arr + i) = val;

        ptr++;
    }

    bubbleSort(arr, size);

    if (size % 2 == 0) {
        return (*(arr + (size / 2)) + *(arr + (size / 2) - 1));
    } else {
        return (*(arr + ((size - 1) / 2)));
    }
    return 0;
}

void swap(int *a, int *b) { 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
}  

void bubbleSort(int *arr, int n) { 
    int i, j; 
    for (i = 0; i < n-1; i++)       
    for (j = 0; j < n-i-1; j++) if (arr[j] > arr[j+1]) 
    swap(&arr[j], &arr[j+1]); 
}