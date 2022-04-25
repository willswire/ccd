#pragma once

#include <stdio.h>


#ifdef __cplusplus
extern "C" {
#endif
    void copy1(char *const dest, const char *src);
    void copy2(char *dest, const char *src);
#ifdef __cplusplus
}
#endif