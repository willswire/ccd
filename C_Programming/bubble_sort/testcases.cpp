#include <gmock/gmock.h>
#include "TestCode.h"


TEST(BubbleSort_Tests, cornerCases)
{
    int unSortedArrays[4][5] = {
        {5, 7, 12, 23, 44},  //already in ascending order
        {44,23, 12, 7, 5},   //already in descending order  
        {70, 64, 30, 22, 15}, //already in descending order  
        {15, 22, 30, 64, 70}, //already in ascending order                                   
    };
    int sortedArrays[4][5] = {
        {5, 7, 12, 23, 44},
        {5, 7, 12, 23, 44},
        {70, 64, 30, 22, 15},
        {70, 64, 30, 22, 15},
    };
    int *resultArray;
    bool equalArrays;

    for (int i = 0; i < 2; i++)
    {
        resultArray = bubbleSort(unSortedArrays[i], 5, ascending); // ascending order
        equalArrays = true;
        for (int j = 0; j < 5; j++)
            if (sortedArrays[i][j] != resultArray[j])
            {
                equalArrays = false;
                break;
            }

        ASSERT_EQ(equalArrays, true);
    }

    for (int i = 2; i < 4; i++)
    {
        resultArray = bubbleSort(unSortedArrays[i], 5, descending); //descending order
        equalArrays = true;
        for (int j = 0; j < 5; j++)
            if (sortedArrays[i][j] != resultArray[j])
            {
                equalArrays = false;
                break;
            }

        ASSERT_EQ(equalArrays, true);
    }
}


TEST(BubbleSort_Tests, normalCases)
{
    int unSortedArrays[4][5] = {
        {7, 5, 12, 44, 23},
        {-3, -13, -1, -9, -4},
        {93,-5, 17, 0, 72},
        {15, 30, 22, 64, 70}
    };
    int sortedArrays[8][5] = {
        {5, 7, 12, 23, 44},
        {-13, -9, -4, -3, -1},
        {-5, 0, 17, 72, 93},
        {15, 22, 30, 64, 70},
        {44, 23, 12, 7, 5},
        {-1, -3, -4, -9, -13},
        {93, 72, 17, 0, -5},
        {70, 64, 30, 22, 15}
    };
    int *resultArray;
    bool equalArrays;

    for (int i = 0; i < 4; i++)
    {
        resultArray = bubbleSort(unSortedArrays[i], 5, ascending); // ascending order
        equalArrays = true;
        for (int j = 0; j < 5; j++)
            if (sortedArrays[i][j] != resultArray[j])
            {
                equalArrays = false;
                break;
            }

        ASSERT_EQ(equalArrays, true);
    }

    for (int i = 4; i < 8; i++)
    {
        resultArray = bubbleSort(unSortedArrays[i - 4], 5, descending); //descending order
        equalArrays = true;
        for (int j = 0; j < 5; j++)
            if (sortedArrays[i][j] != resultArray[j])
            {
                equalArrays = false;
                break;
            }

        ASSERT_EQ(equalArrays, true);
    }
}

TEST(Ascending_Tests, normalCases)
{
    ASSERT_TRUE(ascending(7, 1));
    ASSERT_FALSE(ascending(2, 4));
    ASSERT_FALSE(ascending(8, 8));
}

TEST(Descending_Tests, normalCases)
{
    ASSERT_TRUE(descending(1, 7));
    ASSERT_FALSE(descending(4, 2));
    ASSERT_FALSE(descending(8, 8));
}
