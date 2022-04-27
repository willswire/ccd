#include <gmock/gmock.h>
#include "TestCode.h"


TEST(isMagicSquareTest, default_case)
{
    int square1[ROWS][COLS] = { { 4, 9, 2 },
                                { 3, 5, 7 },
                                { 8, 1, 6 } };

    int square2[ROWS][COLS] = { { 8, 3, 4 },
                                { 1, 5, 9 },
                                { 6, 7, 2 } };

    int square3[ROWS][COLS] = { { 6, 1, 8 },
                                { 7, 5, 3 },
                                { 2, 9, 4 } };

    ASSERT_EQ(true, isMagicSquare(square1));
    ASSERT_EQ(true, isMagicSquare(square2));
    ASSERT_EQ(true, isMagicSquare(square3));
}

TEST(isMagicSquareTest, same_case)
{
    int square4[ROWS][COLS] = { { 0, 0, 0 },
                                { 0, 0, 0 },
                                { 0, 0, 0 } };

    int square5[ROWS][COLS] = { { 1, 1, 1 },
                                { 1, 1, 1 },
                                { 1, 1, 1 } };

    ASSERT_EQ(false, isMagicSquare(square4));
    ASSERT_EQ(false, isMagicSquare(square5));
}

TEST(isMagicSquareTest, diagonal_case)
{
    int square6[ROWS][COLS] = { { 1, 0, 0 },
                                { 0, 1, 0 },
                                { 0, 0, 1 } };

    ASSERT_EQ(false, isMagicSquare(square6));
}

TEST(isMagicSquareTest, invalid_val_case)
{
    int square7[ROWS][COLS] = { { 10, 2, 3 },
                                { 4, 15, 6 },
                                { 7, 8, -8 } };

    ASSERT_EQ(false, isMagicSquare(square7));
}

TEST(isMagicSquareTest, sum_case)
{
    int square8[ROWS][COLS] = { { 5, 5, 5 },
                                { 5, 5, 5 },
                                { 5, 5, 5 } };

    ASSERT_EQ(false, isMagicSquare(square8));
}

TEST(isMagicSquareTest, uniqueness_and_range)
{
    int square9[ROWS][COLS] = { { 6, 3, 6 },
                                { 5, 5, 5 },
                                { 4, 7, 4 } };

    ASSERT_EQ(false, isMagicSquare(square9));
}

TEST(isMagicSquareTest, unique_but_bad_sums_case)
{
    int square10[ROWS][COLS] = { { 9, 5, 2 },
                                { 3, 4, 7 },
                                { 8, 1, 6 } };

    ASSERT_EQ(false, isMagicSquare(square10));
}
