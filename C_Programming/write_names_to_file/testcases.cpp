#include <gmock/gmock.h>
#include "TestCode.h"


TEST(WriteNames_Tests, normalCases)
{
    const char *fnames[] = {"george", "john", "millard", "Theodore"};
    const char *lnames[] = {"Washington", "adams", "Filmore", "roosevelt"};
    ASSERT_EQ(1, writeNames(fnames, lnames, sizeof(fnames) / sizeof(*fnames), "names.txt"));
    FILE *fp = fopen("names.txt", "r");
    ASSERT_FALSE(fp == NULL); // The file should exist

    const char *names[] = {"Washington, George\n","Adams, John\n","Filmore, Millard\n","Roosevelt, Theodore"};
    int count = 0;
    char tempBuff[150] = { 0 };
    char *tempReturn = tempBuff;
    
    while ((tempReturn = fgets(tempBuff, 150, fp)))
    {
        if (tempReturn)
        {
            ASSERT_EQ(strcmp(names[count],tempReturn), 0);
        }
        count++;
    }
    fclose(fp);
}

TEST(WriteNames_Tests, edgeCases)
{
    const char *fnames[] = {"george", "john", "millard", "Theodore"};
    const char *lnames[] = {"Washington", "adams", "Filmore", "roosevelt"};
    ASSERT_EQ(0, writeNames(fnames, lnames, 0, "sizeZero.txt"));
    FILE *fp = fopen("sizeZero.txt", "r");
    ASSERT_TRUE(fp == NULL); // file should not exist

    ASSERT_EQ(0, writeNames(fnames, lnames, -2, "neg.txt"));
    fp = fopen("neg.txt", "r");
    ASSERT_TRUE(fp == NULL); // file should not exist

    const char *fnames2[] = {"", "green", "Red", "Brown"};
    ASSERT_EQ(0, writeNames(fnames2, lnames, 4, "noFirst.txt"));
    fp = fopen("noFirst.txt", "r");
    ASSERT_TRUE(fp == NULL); // file should not exist

    const char *lnames2[] = {"bonnet", "eyes", "Rocket", ""};
    ASSERT_EQ(0, writeNames(fnames, lnames2, 4, "noLast.txt"));
    fp = fopen("noLast.txt", "r");
    ASSERT_TRUE(fp == NULL); // file should not exist
}

TEST(WriteNames_Tests, nullCases)
{
    const char *fnames[] = {"george", "john", "millard", "Theodore"};
    const char *lnames[] = {"Washington", "adams", "Filmore", "roosevelt"};
    const char *fileName = "nulltest.txt";

    ASSERT_EQ(0, writeNames(NULL, lnames, 4, fileName));
    FILE *fp = fopen(fileName, "r");
    ASSERT_TRUE(fp == NULL); // file should not exist

    ASSERT_EQ(0, writeNames(fnames, NULL, 4, fileName));
    fp = fopen(fileName, "r");
    ASSERT_TRUE(fp == NULL); // file should not exist

    ASSERT_EQ(0, writeNames(fnames, lnames, 4, NULL));
}
