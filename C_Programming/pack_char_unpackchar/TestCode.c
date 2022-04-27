#include <stdio.h>
#include <stdlib.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions
const int BYTE = 8;

unsigned int packCharacters(char ch4, char ch3, char ch2, char ch1)
{
    int i = 0;
    i += (int)ch4;
    i <<= BYTE;
    i += (int)ch3;
    i <<= BYTE;
    i += (int)ch2;
    i <<= BYTE;
    i += (int)ch1;

    return i;
}

char *unpackCharacters(unsigned int pack)
{
    char *temp = NULL;
    if (pack != 0) {
        temp = malloc(4 * sizeof(char));
        *(temp + 3) = pack;
        *(temp + 2) = pack >> BYTE;
        *(temp + 1) = pack >> (BYTE * 2);
        *(temp) = pack >> (BYTE * 3);
    }
    return temp;
}
