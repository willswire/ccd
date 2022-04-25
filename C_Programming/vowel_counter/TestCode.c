#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

int countVowels(const char *text, struct Vowels *v)
{
    if (text == NULL || strlen(text) == 0)
        return ERROR_EMPTY;

    for (int i = 0; i < strlen(text); i++) {
        switch (text[i])
        {
        case 'a':
        case 'A':
            v->aCount += 1;
            break;
        case 'e':
        case 'E':
            v->eCount += 1;
            break; 
        case 'i':
        case 'I':
            v->iCount += 1;
            break; 
        case 'o':
        case 'O':
            v->oCount += 1;
            break; 
        case 'u':
        case 'U':
            v->uCount += 1;
            break; 
        case 'y':
            if (text[i-1] != ' ')
                v->yCount += 1;
            break; 
        default:
            break;
        }
    }   

    int res = v->aCount + v->eCount + v->iCount + v->oCount + v->uCount + v->yCount;

    return res;
}
