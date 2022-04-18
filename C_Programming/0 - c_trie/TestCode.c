#include "TestCode.h"

// Refer to README.md for the problem instructions

// Converts key current character into index
// use only 'a' through 'z' and lower case
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')

void addWord(struct Node *root, const char *word)
{
    return;
}

int findWord(struct Node *root, const char *word)
{
    return 0;
}

struct Node *buildTree(const char *wordList[], int length)
{
    struct Node *root;

    // For each word in the list...
    for (int i = 0; i < length; i++) {
        char *word = wordList[i];
        int wordLen = strlen(word);

        for (int level = 0; i < wordLen; level++) {
            int index = CHAR_TO_INDEX(word[level]);
            
        }
    }
    return NULL;
}

void deleteTree(struct Node **root)
{
    return;
}
