#pragma once

#include <stdio.h>

#define ERROR_INVALID_PARAMETER 87

#ifdef __cplusplus
extern "C" {
#endif
    int bin_hex_StrToInt32(const char *s, int mode);

#ifdef __cplusplus
}
#endif
