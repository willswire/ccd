#include <gmock/gmock.h>
#include "TestCode.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


TEST(BSTTests, LeftRightNoDuplicateCase)
{
    int nums[] = {7, 3, 8, 9, 2, 6};
    struct numNode *root = buildBST(nums, sizeof(nums) / sizeof(*nums));
    EXPECT_EQ(7, root->val);
    EXPECT_EQ(8, root->right->val);
    EXPECT_EQ(9, root->right->right->val);
    EXPECT_EQ(NULL, root->right->left);
    EXPECT_EQ(NULL, root->right->right->right);
    EXPECT_EQ(NULL, root->right->right->left);
    EXPECT_EQ(3, root->left->val);
    EXPECT_EQ(6, root->left->right->val);
    EXPECT_EQ(2, root->left->left->val);
    EXPECT_EQ(NULL, root->left->right->right);
    EXPECT_EQ(NULL, root->left->right->left);
    EXPECT_EQ(NULL, root->left->left->right);
    EXPECT_EQ(NULL, root->left->left->left);
    EXPECT_EQ(6, destroyBST(root));
    root = NULL;
}

TEST(BSTTests, RightDuplicateCase)
{
    int nums[] = {1, 2, 3, 4, 7, 5, 4, 6, 9, 11, 10};
    struct numNode *root = buildBST(nums, sizeof(nums) / sizeof(*nums));    
    EXPECT_EQ(1, root->val);
    EXPECT_EQ(2, root->right->val);
    EXPECT_EQ(NULL, root->left);
    EXPECT_EQ(3, root->right->right->val);
    EXPECT_EQ(NULL, root->right->left);
    EXPECT_EQ(4, root->right->right->right->val);
    EXPECT_EQ(NULL, root->right->right->left);
    EXPECT_EQ(7, root->right->right->right->right->val);
    EXPECT_EQ(9, root->right->right->right->right->right->val);
    EXPECT_EQ(NULL, root->right->right->right->right->right->left);
    EXPECT_EQ(11, root->right->right->right->right->right->right->val);
    EXPECT_EQ(NULL, root->right->right->right->right->right->right->right);
    EXPECT_EQ(10, root->right->right->right->right->right->right->left->val);
    EXPECT_EQ(NULL, root->right->right->right->right->right->right->left->right);
    EXPECT_EQ(NULL, root->right->right->right->right->right->right->left->left);
    EXPECT_EQ(5, root->right->right->right->right->left->val);
    EXPECT_EQ(6, root->right->right->right->right->left->right->val);
    EXPECT_EQ(NULL, root->right->right->right->right->left->right->right);
    EXPECT_EQ(NULL, root->right->right->right->right->left->right->left);
    EXPECT_EQ(NULL, root->right->right->right->right->left->left);
    EXPECT_EQ(10, destroyBST(root));
    root = NULL;
}

TEST(BSTTests, LeftDuplicateCase)
{
    int nums[] = {11, 10, 6, 9, 4, 5, 7, 3, 3, 2, 6, 1};
    struct numNode *root = buildBST(nums, sizeof(nums) / sizeof(*nums));    
    EXPECT_EQ(11, root->val);
    EXPECT_EQ(NULL, root->right);
    EXPECT_EQ(10, root->left->val);
    EXPECT_EQ(NULL, root->left->right);
    EXPECT_EQ(6, root->left->left->val);
    EXPECT_EQ(9, root->left->left->right->val);
    EXPECT_EQ(NULL, root->left->left->right->right);
    EXPECT_EQ(7, root->left->left->right->left->val);
    EXPECT_EQ(NULL, root->left->left->right->left->right);
    EXPECT_EQ(NULL, root->left->left->right->left->left);
    EXPECT_EQ(4, root->left->left->left->val);
    EXPECT_EQ(5, root->left->left->left->right->val);
    EXPECT_EQ(NULL, root->left->left->left->right->right);
    EXPECT_EQ(NULL, root->left->left->left->right->left);
    EXPECT_EQ(3, root->left->left->left->left->val);
    EXPECT_EQ(NULL, root->left->left->left->left->right);
    EXPECT_EQ(2, root->left->left->left->left->left->val);
    EXPECT_EQ(NULL, root->left->left->left->left->left->right);
    EXPECT_EQ(1, root->left->left->left->left->left->left->val);
    EXPECT_EQ(NULL, root->left->left->left->left->left->left->right);
    EXPECT_EQ(NULL, root->left->left->left->left->left->left->left);
    EXPECT_EQ(10, destroyBST(root));
    root = NULL;
}
