#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions


int bin_hex_StrToInt32(const char *s, int mode)
{
    if (confirmMode(s, mode)) {

    } else {
        return ERROR_INVALID_PARAMETER;
    }
}

int confirmMode(char *s, int mode) {
    int result = 0;

    int length = countLength(&s);
    printf("The string is %d characters long\n");

    for (int i = 0; i < length; i++) {
        printf("Checking for %c\n", s[i]);
        if (mode == 1) {
            if (s[i] != '0' || s[i] != '1') {
                return 0;
            }
        } else if (mode == 2) {
            if (s[i] != '0' || s[i] != '1' || s[i] != '2' || s[i] != '3' || s[i] != '4' || s[i] != '5' || s[i] != '6'  || s[i] != '7'
                || s[i] != '8' || s[i] != '9' || s[i] != 'A' || s[i] != 'B' || s[i] != 'C' || s[i] != 'D' || s[i] != 'D' || s[i] != 'F') {
                return 0;
            }
        } else {
            return 0;
        }
    }

    return mode;
}

int countLength(char *s) {
    int i = 0;
    if (s != NULL) {
        while (s[i] != '\0') {
            i++;
        }
    }
    return i;
}