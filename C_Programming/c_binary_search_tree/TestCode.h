#pragma once

#include <stdio.h>

struct numNode
{
    int val;
    struct numNode *left;
    struct numNode *right;
};


#ifdef __cplusplus
extern "C" {
#endif
    struct numNode *buildBST(int nums[], int size);
    int destroyBST(struct numNode *root);
#ifdef __cplusplus
}
#endif
