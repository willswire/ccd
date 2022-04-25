#pragma once

#include <stdio.h>


#ifdef __cplusplus
extern "C" {
#endif
    const char *encryptVigenere(const char *input, const char *key);
#ifdef __cplusplus
}
#endif