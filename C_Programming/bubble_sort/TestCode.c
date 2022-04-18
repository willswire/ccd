#include <stdio.h>

// Refer to README.md for the problem instructions

/*
The function bubbleSort receives a pointer to a function, which performs either ascending or descending sorting; an 
integer array; and the size of the array as input arguments. The parameter `compare` is a pointer to the comparison 
function that determines the sorting order. The function returns an integer pointer to the sorted array.
*/

int *bubbleSort(int elements[], size_t length, int(*compare)(int a, int b))
{
    int i, j; 
    for (i = 0; i < length-1; i++) {     
        for (j = 0; j < length-i-1; j++) {
            if (compare(elements[j], elements[j + 1])) {
                int temp = elements[j + 1]; 
                elements[j + 1] = elements[j];
                elements[j] = temp;
            }
        }
    }

    return elements;
}


// @brief Determine whether elements are out of order for an ascending order sort
// @return Boolean indicating whether the two elements should be swapped
int ascending(int a, int b)
{
    return a > b;         
}

// @brief Determine whether elements are out of order for a descending order sort
// @return Boolean indicating whether the two elements should be swapped
int descending(int a, int b)
{
    return a < b;      
}