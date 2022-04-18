#include <gmock/gmock.h>
#include "TestCode.h"


TEST(BuyGroceries_Tests, cornerCases)
{
    int edge[] = { 0 };
    ASSERT_EQ(0, buyGroceries(edge, 0));
    ASSERT_EQ(0, buyGroceries(edge, 1));
    ASSERT_EQ(0, buyGroceries(edge, 9));

    int stuff[] = { 1, 1, 2, 0 };
    ASSERT_EQ(0, buyGroceries(stuff, 4));

    int stuff2[] = { 1, 1, 0, 6 };
    ASSERT_EQ(0, buyGroceries(stuff2, 4));

    int stuff3[] = { 1, 1, 5, 1 };
    ASSERT_EQ(0, buyGroceries(stuff3, 4));
}


TEST(BuyGroceries_Tests, normalCases)
{
    int stuff[] = { 1, 3, 2, 5, 4, 4 };
    ASSERT_EQ(38, buyGroceries(stuff, 6));

    int stuff2[] = { 1, 5, 2, 5, 4, 5, 3, 5 };
    ASSERT_EQ(56, buyGroceries(stuff2, 8));

    int stuff3[] = { 1, 1, 2, 1, 3, 1, 4, 1 };
    ASSERT_EQ(12, buyGroceries(stuff3, 8));

    int stuff4[] = { 1, 6, 2, 7, 3, 8, 4, 15 };
    ASSERT_EQ(109, buyGroceries(stuff4, 8));
}

TEST(BuyGroceries_Tests, nullCases)
{
    ASSERT_EQ(0, buyGroceries(NULL, 1)); // Force checking NULL by itself
}
