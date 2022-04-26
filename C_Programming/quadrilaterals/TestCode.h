#pragma once

#include <stdio.h>


struct QuadStruct {
    int rect;
    int para;
    int quad;
    int invalid;
};


#ifdef __cplusplus
extern "C" {
#endif
    void classify_quads(int quads[][4], int rows, struct QuadStruct *qds);
#ifdef __cplusplus
}
#endif
