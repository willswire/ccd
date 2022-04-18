#pragma once

#include <stdio.h>
#include <string.h>

#define ALPHA_LENGTH 26

struct Node                  
{
    struct Node *children[ALPHA_LENGTH];
    int endOfWord;
};

#ifdef __cplusplus
extern "C" {
#endif
    struct Node *buildTree(const char **,int);
    void addWord(struct Node *, const char *);
    int findWord(struct Node *, const char *);
    void deleteTree(struct Node **);
#ifdef __cplusplus
}
#endif
