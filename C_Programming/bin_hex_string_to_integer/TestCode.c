#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions


int bin_hex_StrToInt32(const char *s, int mode)
{
    // Check for NULL
    if (s == NULL || mode == NULL) {
        return ERROR_INVALID_PARAMETER;
    }

    int length = strlen(s);

    // Check the string length
    if (!(length > 0)) {
        return ERROR_INVALID_PARAMETER;
    }

    int integer = 0;
    
    // Iterate through array
    if (mode == 1) {
        for (int i = 0; i < length; i++) {
            switch (s[i])
            {
            case '0':
                break;
            case '1':
                integer += pow(2, length - i - 1);
                break;
            default:
                return ERROR_INVALID_PARAMETER;
            }
        }
    } else if (mode == 2) {
        for (int i = 0; i < length; i++) {
            switch (s[i])
            {
            case '0':
                break;
            case '1':
                integer += pow(16, length - i - 1);
                break;
            case '2':
                integer += 2 * pow(16, length - i - 1);
                break;
            case '3':
                integer += 3 * pow(16, length - i - 1);
                break;
            case '4':
                integer += 4 * pow(16, length - i - 1);
                break;
            case '5':
                integer += 5 * pow(16, length - i - 1);
                break;
            case '6':
                integer += 6 * pow(16, length - i - 1);
                break;
            case '7':
                integer += 7 * pow(16, length - i - 1);
                break;
            case '8':
                integer += 8 * pow(16, length - i - 1);
                break;
            case '9':
                integer += 9 * pow(16, length - i - 1);
                break;
            case 'A':
            case 'a':
                integer += 10 * pow(16, length - i - 1);
                break;
            case 'B':
            case 'b':
                integer += 11 * pow(16, length - i - 1);
                break;
            case 'C':
            case 'c':
                integer += 12 * pow(16, length - i - 1);
                break;
            case 'D':
            case 'd':
                integer += 13 * pow(16, length - i - 1);
                break;
            case 'E':
            case 'e':
                integer += 14 * pow(16, length - i - 1);
                break;
            case 'F':
            case 'f':
                integer += 15 * pow(16, length - i - 1);
                break;
            default:
                return ERROR_INVALID_PARAMETER;
            }
        }
    }
    else {
        return ERROR_INVALID_PARAMETER;
    }
    
    return integer;
}
