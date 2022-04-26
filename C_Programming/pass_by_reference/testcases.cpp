#include <gmock/gmock.h>
#include "TestCode.h"


// This needs more test cases for the "otherwise" cases
TEST(RefFunction_Tests, normalCases)
{
    int val1 = 10, val2 = 20;
    refFunction(&val1, &val2, 2);
    ASSERT_EQ(20, val1);
    ASSERT_EQ(10, val2);
    refFunction(&val1, &val2, 2);
    ASSERT_EQ(20, val1);
    ASSERT_EQ(10, val2);
    refFunction(&val1, &val2, 1);
    ASSERT_EQ(10, val1);
    ASSERT_EQ(20, val2);
    refFunction(&val1, &val2, 1);
    ASSERT_EQ(10, val1);
    ASSERT_EQ(20, val2);
    refFunction(&val1, &val2, 3);
    ASSERT_EQ(20, val1);
    ASSERT_EQ(40, val2);
    refFunction(&val1, &val2, 4);
    ASSERT_EQ(0, val1);
    ASSERT_EQ(0, val2);
}
