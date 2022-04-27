#include <gmock/gmock.h>
#include "TestCode.h"


TEST(LetterFrequency_Tests, cornerCases)
{
    int frequencyTable[26] = { 0 };
    int equalTables;
    const char *stringlist[] = {
        NULL,
        "",
        "~!$23#-=/*?, < >",
        " ",
    };


    ASSERT_EQ(0, letterFrequency(stringlist[0], frequencyTable));
    ASSERT_EQ(0, letterFrequency(stringlist[1], frequencyTable));

    (void)letterFrequency(stringlist[2], frequencyTable);
    equalTables = 1;
    for (int i = 0; i < 26; i++)
        if (frequencyTable[i] != 0)
        {
            equalTables = 0;
            break;
        }

    ASSERT_EQ(equalTables, 1);

    (void)letterFrequency(stringlist[3], frequencyTable);
    equalTables = 1;
    for (int i = 0; i < 26; i++)
        if (frequencyTable[i] != 0)
        {
            equalTables = 0;
            break;
        }

    ASSERT_EQ(equalTables, 1);

}

TEST(LetterFrequency_Tests, normalSentences)
{
    const char *stringlist[] = {
        " all lower case!",
        "ALL UPPER CASE ",
        "aaa",
        "THIS IS A SENTENCE IN UPPER CASE. this is another sentence in lower case!"
    };
    int frequencyTables[4][26] = {
        { 2, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0 },
        { 2, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0 },
        { 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
        { 4, 0, 4, 0, 11, 0, 0, 3, 6, 0, 0, 1, 0, 7, 2, 2, 0, 3, 8, 5, 1, 0, 1, 0, 0, 0 }
    };
    int equalTables;

    for (int i = 0; i < 4; i++)
    {
        int resultTable[26] = { 0 };

        (void)letterFrequency(stringlist[i], resultTable);
        equalTables = 1;
        for (int j = 0; j < 26; j++)
            if (frequencyTables[i][j] != resultTable[j])
            {
                equalTables = 0;
                break;
            }

        ASSERT_EQ(equalTables, 1);
    }
}
