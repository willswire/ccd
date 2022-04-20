#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

struct numNode *buildBST(int nums[], int size)
{
    struct numNode* root = malloc(sizeof(struct numNode));
    root->val = nums[0];
    root->right = NULL;
    root->left = NULL;

    for (int i = 1; i < size; i++) {

        struct numNode* currentNode = root;
        struct numNode* parentNode = NULL;

        int dup = 0;
        while (currentNode != NULL && !dup) {
            parentNode = currentNode;
            if (nums[i] < currentNode->val)
                currentNode = currentNode->left;
            else if (nums[i] > currentNode->val)
                currentNode = currentNode->right;
            else
                dup = 1;
        }

        if (!dup) {
            struct numNode* newNode = malloc(sizeof(struct numNode));
            newNode->val = nums[i];
            newNode->right = NULL;
            newNode->left = NULL;
        
            if (newNode->val < parentNode->val)
                parentNode->left = newNode;
        
            else if (newNode->val > parentNode->val)
                parentNode->right = newNode;
        }
    }

    return root;
}


int destroyBST(struct numNode *root)
{
    int freeNodeCount = 1;

    if (root->left != NULL) {
        freeNodeCount += destroyBST(root->left);
    }
    
    if (root->right != NULL) {
        freeNodeCount += destroyBST(root->right);
    }

    free(root);

    return freeNodeCount;
}
