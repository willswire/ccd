#include <gmock/gmock.h>
#include "TestCode.h"

#define SIZE 10

TEST(checkAmountTests, invalid_cases)
{
    char *wordsCheckValue = checkAmount(0.0);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(-23.0);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(-77.34);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(-0.01);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(-0.99);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(100.0);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(132.07);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(354);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(2345.67);
    EXPECT_TRUE(wordsCheckValue == NULL);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}

TEST(checkAmountTests, lessThanDollar_cases)
{
    char *wordsCheckValue = checkAmount(0.52);
    EXPECT_STREQ("ZERO and 52/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(0.01);
    EXPECT_STREQ("ZERO and 1/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(0.99);
    EXPECT_STREQ("ZERO and 99/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}

TEST(checkAmountTests, evenDollarLessThanTen_cases)
{
    char *wordsCheckValue = checkAmount(7);
    EXPECT_STREQ("SEVEN and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(1.0);
    EXPECT_STREQ("ONE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(3);
    EXPECT_STREQ("THREE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(5.0);
    EXPECT_STREQ("FIVE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(9);
    EXPECT_STREQ("NINE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}

TEST(checkAmountTests, unevenDollarLessThanTen_cases)
{
    char *wordsCheckValue = checkAmount(8.28);
    EXPECT_STREQ("EIGHT and 28/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(1.01);
    EXPECT_STREQ("ONE and 1/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(2.84);
    EXPECT_STREQ("TWO and 84/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(4.33);
    EXPECT_STREQ("FOUR and 33/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(6.66);
    EXPECT_STREQ("SIX and 66/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(9.99);
    EXPECT_STREQ("NINE and 99/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}

TEST(checkAmountTests, evenDollarTenToNineteen_cases)
{
    char *wordsCheckValue = checkAmount(10);
    EXPECT_STREQ("TEN and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(12.0);
    EXPECT_STREQ("TWELVE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(13.0);
    EXPECT_STREQ("THIRTEEN and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(15);
    EXPECT_STREQ("FIFTEEN and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(17.00);
    EXPECT_STREQ("SEVENTEEN and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(19);
    EXPECT_STREQ("NINETEEN and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}

TEST(checkAmountTests, unevenDollarTenToNineteen_cases)
{
    char *wordsCheckValue = checkAmount(10.01);
    EXPECT_STREQ("TEN and 1/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(11.44);
    EXPECT_STREQ("ELEVEN and 44/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(14.67);
    EXPECT_STREQ("FOURTEEN and 67/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(16.50);
    EXPECT_STREQ("SIXTEEN and 50/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(18.05);
    EXPECT_STREQ("EIGHTEEN and 5/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(19.99);
    EXPECT_STREQ("NINETEEN and 99/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}

TEST(checkAmountTests, evenDollarGreaterThanTwenty_cases)
{
    char *wordsCheckValue = checkAmount(20.00);
    EXPECT_STREQ("TWENTY and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(33.00);
    EXPECT_STREQ("THIRTY THREE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(55);
    EXPECT_STREQ("FIFTY FIVE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(78);
    EXPECT_STREQ("SEVENTY EIGHT and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(80);
    EXPECT_STREQ("EIGHTY and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(99.0);
    EXPECT_STREQ("NINETY NINE and 0/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}

TEST(checkAmountTests, unevenDollarGreaterThanTwenty_cases)
{
    char *wordsCheckValue = checkAmount(20.01);
    EXPECT_STREQ("TWENTY and 1/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(24.80);
    EXPECT_STREQ("TWENTY FOUR and 80/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(47.69);
    EXPECT_STREQ("FORTY SEVEN and 69/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(52.43);
    EXPECT_STREQ("FIFTY TWO and 43/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(61.14);
    EXPECT_STREQ("SIXTY ONE and 14/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(87.41);
    EXPECT_STREQ("EIGHTY SEVEN and 41/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);

    wordsCheckValue = checkAmount(99.99);
    EXPECT_STREQ("NINETY NINE and 99/100", wordsCheckValue);
    if (wordsCheckValue != NULL)
        free(wordsCheckValue);
}
