#include <gmock/gmock.h>
#include "TestCode.h"

const int SIZE = 15;

TEST(getModeTest, standardCase)
{
    int *arr = new int[SIZE] { 1, 3, 3, 3, 2, 2, 1, 3, 4, 5, 8, 8, 9, 3, 2 };
    ASSERT_EQ(3, getMode(arr, SIZE));
    delete []arr;
    arr = NULL;

    arr = new int[SIZE] { 1, 4, 2, 6, 7, 2, 4, 3, 4, 5, 4, 4, 9, 3, 4 };
    ASSERT_EQ(4, getMode(arr, SIZE));
    delete []arr;
    arr = NULL;
}

TEST(getModeTest, allSameCase)
{
    int *arr = new int[SIZE] { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
    ASSERT_EQ(1, getMode(arr, SIZE));
    delete []arr;
    arr = NULL;
}

TEST(getModeTest, noModeCase)
{
    int *arr = new int[SIZE] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
    ASSERT_EQ(-1, getMode(arr, SIZE));
    delete []arr;
    arr = NULL;
}

TEST(getModeTest, manyModesCase)
{
    int *arr = new int[SIZE] { 2, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 11, 13, 14, 15 };
    int mode5 = getMode(arr, SIZE);
    delete []arr;
    arr = NULL;

    std::array<int, 3> modeArr = {2, 8, 11};
    EXPECT_THAT(modeArr, ::testing::Contains(mode5));
}

TEST(getModeTest, nullInputCases)
{
    ASSERT_EQ(-2, getMode(NULL, 0));
}
