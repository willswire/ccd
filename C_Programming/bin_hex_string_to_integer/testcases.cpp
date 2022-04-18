#include <gmock/gmock.h>
#include "TestCode.h"

#define _SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING  1


TEST(Bin_hex_StrToInt32_Tests, cornerCases)
{                       
    const char *stringlist[] = {""," ", "00 11", ".0123", "0.", "+00", "0.1", "10+", "12fl", "abcdefg" };

    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[0], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[1], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[2], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[3], 2));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[4], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[5], 2));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[6], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[7], 2));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[8], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[9], 2));
}

TEST(Bin_hex_StrToInt32_Tests, normalCases)
{       
    const char *stringlist[] = {
                          "0", 
                          "0000",
                          "1",
                          "0001",
                          "101",
                          "1100",
                          "11100",
                          "10000000",
                          "11111001",
                          "0000111100001101",
                          "9",
                          "A",
                          "F",
                          "0123",
                          "abcdef",
                          "ABCDEF",
                          "abcDEF",
                          "aBcDeF",
                          "D1Ce",
                          "923FB5"
                         };

    ASSERT_EQ(0, bin_hex_StrToInt32(stringlist[0], 1));
    ASSERT_EQ(0, bin_hex_StrToInt32(stringlist[1], 1));
    ASSERT_EQ(1, bin_hex_StrToInt32(stringlist[2], 1));
    ASSERT_EQ(1, bin_hex_StrToInt32(stringlist[3], 1));
    ASSERT_EQ(5, bin_hex_StrToInt32(stringlist[4], 1));
    ASSERT_EQ(12, bin_hex_StrToInt32(stringlist[5], 1));
    ASSERT_EQ(28, bin_hex_StrToInt32(stringlist[6], 1));
    ASSERT_EQ(128, bin_hex_StrToInt32(stringlist[7], 1));
    ASSERT_EQ(249, bin_hex_StrToInt32(stringlist[8], 1));
    ASSERT_EQ(3853, bin_hex_StrToInt32(stringlist[9], 1));
    ASSERT_EQ(9, bin_hex_StrToInt32(stringlist[10], 2));
    ASSERT_EQ(10, bin_hex_StrToInt32(stringlist[11], 2));
    ASSERT_EQ(15, bin_hex_StrToInt32(stringlist[12], 2));
    ASSERT_EQ(291, bin_hex_StrToInt32(stringlist[13], 2));
    ASSERT_EQ(11259375, bin_hex_StrToInt32(stringlist[14], 2));
    ASSERT_EQ(11259375, bin_hex_StrToInt32(stringlist[15], 2));
    ASSERT_EQ(11259375, bin_hex_StrToInt32(stringlist[16], 2));
    ASSERT_EQ(11259375, bin_hex_StrToInt32(stringlist[17], 2));
    ASSERT_EQ(53710, bin_hex_StrToInt32(stringlist[18], 2));
    ASSERT_EQ(9584565, bin_hex_StrToInt32(stringlist[19], 2));
}

TEST(Bin_hex_StrToInt32_Tests, wrong_mode_test)
{
    const char *stringlist[] = {
                          "1100",
                          "ab10",
                          "10ae",
                          "abcd"};

    ASSERT_EQ(4352, bin_hex_StrToInt32(stringlist[0], 2));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[1], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[2], 1));
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(stringlist[3], 1));
}

TEST(Bin_hex_StrToInt32_Tests, nullCases)
{
    ASSERT_EQ(ERROR_INVALID_PARAMETER, bin_hex_StrToInt32(NULL, 0));
}
