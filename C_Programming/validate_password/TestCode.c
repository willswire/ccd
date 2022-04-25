#include <stdio.h>
#include <string.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

int validatePassword(const char *password)
{
    if (password == NULL)
        return 0;

    int passwordLength = strlen(password);
    
    if (passwordLength < 8 || passwordLength > 16)
        return 0;
    
    int capReq = -1;
    int lowReq = -1;
    int digitReq = -1;
    int specReq = 0;
    int violation = 0;

    for (int i = 0; i < passwordLength; i++) {
        switch ((int) password[i])
        {
        case 65 ... 90:
            capReq++;
            break;
        case 97 ... 122:
            lowReq++;
            break;
        case 48 ... 57:
            digitReq++;
            break;
        case 33:
        case 35 ... 36:
            specReq++;
            break;
        default:
            violation++;
            break;
        }
    }

    return (capReq && lowReq && digitReq && specReq && !violation);
}
