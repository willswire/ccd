#include <gmock/gmock.h>
#include "TestCode.h"

TEST(Copy1_Tests, normalCases)
{
    char str_buff1[] = {'1', '1'};
    const char *string1 = "H";
    copy1(str_buff1, string1);
    ASSERT_EQ(0, strncmp(string1, str_buff1, 2));

    char str_buff2[] = {'1', '1', '1', '1', '1', '1'};
    const char *string2 = "Hello";
    copy1(str_buff2, string2);
    ASSERT_EQ(0, strncmp(string2, str_buff2, 6));
}

TEST(Copy1_Tests, nullCases)
{
    char str_buff[] = {'1', '1', '1', '1', '1', '1', '1', '1', '1', '1'};
    char expected[] = {'1', '1', '1', '1', '1', '1', '1', '1', '1', '1'};
    const char *string = "Null Test";
    copy1(NULL, string);
    copy1(str_buff, NULL);
    ASSERT_EQ(0, memcmp(expected, str_buff, 10));
}

TEST(Copy2_Tests, normalCases)
{
    char str_buff1[] = {'1', '1'};
    const char string1[] = "G";
    copy2(str_buff1, string1);
    ASSERT_EQ(0, strncmp(string1, str_buff1, 2));

    char str_buff2[] = {'1', '1', '1', '1', '1', '1', '1', '1', '1'};
    const char string2[] = "Good Bye";
    copy2(str_buff2, string2);
    ASSERT_EQ(0, strncmp(string2, str_buff2, 9));
}

TEST(Copy2_Tests, nullCases)
{
    char str_buff[] = {'1', '1', '1', '1', '1', '1', '1', '1', '1', '1'};
    char expected[] = {'1', '1', '1', '1', '1', '1', '1', '1', '1', '1'};
    const char string[] = "Null Test";
    copy2(NULL, string);
    copy2(str_buff, NULL);
    ASSERT_EQ(0, memcmp(expected, str_buff, 10));
}
