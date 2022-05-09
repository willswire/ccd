#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Refer to README.md for the problem instructions

char **formatNums(const char **nums)
{
    int NUMS_COUNT = 10;
    char **newNums = malloc(sizeof(char *) * NUMS_COUNT);
    if (!newNums)
        return NULL;

    for (int i = 0; i < NUMS_COUNT; i++) {
        newNums[i] = malloc(sizeof(char) * 15);
        if (!newNums[i]) {
            free(newNums);
            return NULL;
        }

        char *currentNum = (char *) nums[i];
        char newNum[] = "(XXX) XXX-XXXX";
        for (int j = 0; j < strlen(currentNum); j++) {
            char currentDigit = currentNum[j];
            if (isdigit(currentDigit)) {
                char *replaceMe = strchr(newNum, 'X');
                if (!replaceMe) {
                    for (int k = 0; k <= i; k++){
                        free (newNums[k]);
                    }
                    free(newNums);
                    return NULL;
                }
                *replaceMe = currentDigit;
            }
        }
        strncpy(newNums[i], newNum, 15);
    }

    return newNums;
}
