#include <gmock/gmock.h>
#include "TestCode.h"

TEST(SearchFile_Tests, normalCases)
{
    int res = searchFile("test.txt", "test");
    ASSERT_EQ(5, res);

    res = searchFile("test6.txt", "house");
    ASSERT_EQ(1, res);
}

TEST(SearchFile_Tests, noExistCases)
{
    int res = searchFile("test3.txt", "test"); //file doesn't exist
    ASSERT_EQ(-2, res);

    res = searchFile("test4.txt", "house"); //no instances of 'house'
    ASSERT_EQ(0, res);
}

TEST(SearchFile_Tests, tooSmallCases)
{
    int res = searchFile("test2.txt", "test"); // file file <= 150
    ASSERT_EQ(-1, res);

    res = searchFile("test5.txt", "house");  // file <= 150
    ASSERT_EQ(-1, res);
}

TEST(SearchFile_Tests, nullCases)
{
    int res = searchFile(NULL, "matches");
    ASSERT_EQ(-2, res);

    res = searchFile("", "matches");
    ASSERT_EQ(-2, res);

    res = searchFile("test4.txt", NULL);
    ASSERT_EQ(-3, res);

    res = searchFile("test4.txt", "");
    ASSERT_EQ(-3, res);
}