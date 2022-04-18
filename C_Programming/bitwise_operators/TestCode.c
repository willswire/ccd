#include <stdio.h>
#include <string.h>
#include <math.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions


int bitwiseOps(const char *first, const char *second)
{
    // Check if either value is null
    if (first == NULL || second == NULL) {
        return -1;
    }

    int firstLen = strlen(first);
    int secondLen = strlen(second);
    // Check if the incoming value is not 16 characters
    if (firstLen != 16 || secondLen != 16) {
        return -1;
    }

    // Check if `first` contains characters not `1` and `0`
    for (int i = 0; i < firstLen; i++) {
        if (first[i] != '1' && first[i] != '0') {
            return -2;
        }
    }

    // Check if `second` contains characters not `1` and `0`
    for (int i = 0; i < secondLen; i++) {
        if (second[i] != '1' && second[i] != '0') {
            return -2;
        }
    }

    // Convert the numbers to integer value
    int firstInt = 0;
    for (int i = 0; i < firstLen; i++) {
        int val = first[i];
        if (val == '1') {
            firstInt += pow(2, (firstLen - i - 1));
        }
    }
    int secondInt = 0;
    for (int i = 0; i < secondLen; i++) {
        int val = second[i];
        if (val == '1') {
            secondInt += pow(2, (secondLen - i - 1));
        }
    }

    // Perform bitwise operations
    printf("The first int is %i\nThe second int is %i", firstInt, secondInt);
    if (firstInt % 2 == 0 && secondInt % 2 == 0) {
        return firstInt & secondInt;
    } else if (firstInt % 2 == 1 && secondInt % 2 == 1) {
        return firstInt | secondInt;
    } else if (firstInt > 255 && secondInt > 255) {
        return firstInt ^ secondInt;
    } else {
        return firstInt + secondInt;
    }
}