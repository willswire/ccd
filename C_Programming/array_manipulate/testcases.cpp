#include <gmock/gmock.h>
#include "TestCode.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


TEST(ArrayManipulate_Tests, normalCases)
{
    int size = 10;
    int x [] = {2, 5, 6, 7, 8, 9, 12, 3, 1, 18};
    int y [] = {2, 2, 6, 10, 12, 14, 18, 64, 144, 324};

    ASSERT_EQ(26, arrayManipulate(x, size));

    for (int i = 0; i < size; i++)
    {
        ASSERT_EQ(x[i], y[i]);
    }
}

TEST(ArrayManipulate_Tests, odd_array)
{
    int size = 9;
    int a [] = {22, 15, 6, 7, 8, 9, 12, 3, 18};
    int b [] = {6, 12, 14, 18, 30, 64, 144, 324, 484};

    ASSERT_EQ(30, arrayManipulate(a, size));

    for (int i = 0; i < size; i++)
    {
        ASSERT_EQ(a[i], b[i]);
    }
}

TEST(ArrayManipulate_Tests, small_array)
{
    int x [] = {2, 5, 6, 7, 8, 9, 12, 3, 1, 18};

    ASSERT_EQ(-1, arrayManipulate(x, 1));
    ASSERT_EQ(-1, arrayManipulate(x, 0));
    ASSERT_EQ(-1, arrayManipulate(x, -1));
}

TEST(ArrayManipulate_Tests, minimum_array)
{
    int size = 2;
    int c [] = {22, 0};
    int d [] = {0,484};

    ASSERT_EQ(484, arrayManipulate(c, size));

    for (int i = 0; i < size; i++)
    {
        ASSERT_EQ(c[i], d[i]);
    }
}

TEST(ArrayManipulate_Tests, nullCases)
{
    ASSERT_EQ(-1, arrayManipulate(NULL, 5)); // Force testing the array by itself
}
