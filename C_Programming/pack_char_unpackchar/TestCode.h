#pragma once

#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif
    unsigned int packCharacters(const char ch4, const char ch3, const char ch2, const char ch1);
    char *unpackCharacters(unsigned int pack);

#ifdef __cplusplus
}
#endif