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
    char temp[4];
    char d = pack >> BYTE;
    temp[3] = (char) d;
    char c = pack >> (2 * BYTE);
    temp[2] = (char) c;
    char b = pack >> (3 * BYTE);
    temp[1] = (char) b;
    char a = pack >> (4 * BYTE);
    temp[0] = (char) a;

    return temp;
}
