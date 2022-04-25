#include <stdio.h>
#include <string.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

// copy s2 to s1 using array notation
void copy1(char *const dest, const char *src)
{
    if (dest == NULL || src == NULL)
        return;

    int len = strlen(src);
    int i = 0;
    for (; i < len; i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';
}

// copy s2 to s1 using pointer notation
void copy2(char *dest, const char *src)
{
    if (dest == NULL || src == NULL)
        return;

    int len = strlen(src);
    int i = 0;
    for (; i < len; i++) {
        *(dest + i) = *(src + i);
    }
    *(dest + i) = '\0';

}
