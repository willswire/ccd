#include <gmock/gmock.h>
#include "TestCode.h"


TEST(BSearch_Tests, cornerCases)
{
    int searchArray[] = { 2, 5, 8, 12, 16, 23, 38, 56, 72, 91 };

    ASSERT_EQ(-1, BSearch(searchArray, 0, 9, 100));
    ASSERT_EQ(0, BSearch(searchArray, 0, 9, 2));
    ASSERT_EQ(4, BSearch(searchArray, 0, 9, 16));
    ASSERT_EQ(9, BSearch(searchArray, 0, 9, 91));
}

TEST(BSearch_Tests, normalCases)
{
    int searchArrays[3][10] = {
        { -30, -28, -25, -23,-18, -16, -14, -7, -2, -1 },
        { 15, 25, 37, 41, 48, 63, 78, 102, 124, 234 },
        { -5, -3, 22, 35, 48, 52, 61, 73, 83, 96 }
    };

    ASSERT_EQ(-1, BSearch(searchArrays[0], 0, 9, 0));
    ASSERT_EQ(3, BSearch(searchArrays[0], 0, 9, -23));
    ASSERT_EQ(-1, BSearch(searchArrays[1], 0, 9, 14));
    ASSERT_EQ(5, BSearch(searchArrays[1], 0, 9, 63));
    ASSERT_EQ(-1, BSearch(searchArrays[2], 0, 9, 20));
    ASSERT_EQ(8, BSearch(searchArrays[2],  0, 9, 83));
}