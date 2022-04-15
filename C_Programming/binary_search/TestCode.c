#include <stdio.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions


int BSearch(int arr[], int left, int right, int target)
{
    int middle = getMiddle(left, right);
    printf("The middle element is %i\n", arr[middle]);

    if (arr[middle] == target) {
        return middle;
    } else if (target > arr[middle] && target <= arr[right]) {
        left = middle + 1;
        BSearch(arr, left, right, target);
    } else if (target < arr[middle] && target >= arr[left]) {
        right = middle - 1;
        BSearch(arr, left, right, target);
    } else {
        return -1;
    }
}

int getMiddle(int left, int right) {
    int length = (right - left) + 1;
    if (length % 2 == 0) {
        return left + (length / 2) - 1;
    } else {
        return left + (length - 1) / 2;
    }
}