#include <gmock/gmock.h>
#include "TestCode.h"


TEST(PackCharacters_Tests, cornerCases)
{

    ASSERT_EQ(0, packCharacters('\0', '\0', '\0', '\0'));
    ASSERT_EQ(32, packCharacters('\0', '\0', '\0', ' '));
    ASSERT_EQ(8224, packCharacters('\0', '\0', ' ', ' '));
    ASSERT_EQ(538976256, packCharacters(' ', ' ', ' ', '\0'));
    ASSERT_EQ(538976288, packCharacters(' ', ' ', ' ', ' '));
}

TEST(PackCharacters_Tests, normalCases)
{

    ASSERT_EQ(875770417, packCharacters('4', '3', '2', '1'));
    ASSERT_EQ(1684234849, packCharacters('d', 'c', 'b', 'a'));
    ASSERT_EQ(791293227, packCharacters('/', '*', '-', '+'));
}

TEST(UnpackCharacters_Tests, cornerCases)
{

    int numberList[] = { 32, 8224, 2105376, 538976288, 536870944 };
    char unPackedCharacters[6][4] = {
        { '\0', '\0', '\0', ' ' },
        { '\0', '\0', ' ', ' ' },
        { '\0', ' ', ' ', ' ' },
        { ' ', ' ', ' ', ' ' },
        { ' ', '\0', '\0', ' ' }
    };
    bool equalValues;
    char *resultArray;

    char *testVal = unpackCharacters(0);
    ASSERT_EQ(NULL, testVal);
    free(testVal);
    for (int i = 0; i<5; i++)
    {
        resultArray = unpackCharacters(numberList[i]);
        ASSERT_TRUE(resultArray);
        equalValues = true;

        for (int j = 0; j < 4; j++)
            if (unPackedCharacters[i][j] != resultArray[j])
            {
                equalValues = false;
                break;
            }
        free(resultArray);
        ASSERT_EQ(equalValues, true);
        
    }
}

TEST(UnpackCharacters_Tests, normalCases)
{

    int numberList[] = { 875770417, 1684234849, 791293227 };
    char unPackedCharacters[6][4] = {
        { '4', '3', '2', '1' },
        { 'd', 'c', 'b', 'a' },
        { '/', '*', '-', '+' }
    };
    bool equalValues;
    char *resultArray;


    for (int i = 0; i < 3; i++)
    {
        resultArray = unpackCharacters(numberList[i]);
        equalValues = true;

        ASSERT_TRUE(resultArray);
        for (int j = 0; j < 4; j++)
            if (unPackedCharacters[i][j] != resultArray[j])
            {
                equalValues = false;
                break;
            }
        free(resultArray);
        ASSERT_EQ(equalValues, true);
    }
}
