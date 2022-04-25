#pragma once

#include <stdio.h>

#define ERROR_EMPTY 4306

struct Vowels {
    int aCount;
    int eCount;
    int iCount;
    int oCount;
    int uCount;
    int yCount;

};

#ifdef __cplusplus
extern "C" {
#endif
    // Task One
    int countVowels(const char *text, struct Vowels *v);

#ifdef __cplusplus
}
#endif