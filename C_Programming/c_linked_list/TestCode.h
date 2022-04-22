#pragma once

#include <stdio.h>

struct nameNode
{
    char  *name;
    struct nameNode *next;
};


#ifdef __cplusplus
extern "C" {
#endif
    struct nameNode *processNames(const char **);
    void freeMemory(struct nameNode *);
#ifdef __cplusplus
}
#endif