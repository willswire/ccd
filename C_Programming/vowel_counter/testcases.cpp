#include <gmock/gmock.h>
#include "TestCode.h"


TEST(CountVowels_Tests, cornerCases)
{
    struct Vowels v = { 0,0,0,0,0,0 };
    ASSERT_EQ(ERROR_EMPTY, countVowels("", &v));
    ASSERT_EQ(ERROR_EMPTY, countVowels(NULL, &v));
}

TEST(CountVowels_Tests, normalCases)
{
    struct Vowels v = { 0,0,0,0,0,0 };
    const char *sentence = "Yesterday, all my trouble seemed so far away.";

    ASSERT_EQ(17, countVowels(sentence, &v));
    ASSERT_EQ(5, v.aCount);
    ASSERT_EQ(6, v.eCount);
    ASSERT_EQ(0, v.iCount);
    ASSERT_EQ(2, v.oCount);
    ASSERT_EQ(1, v.uCount);
    ASSERT_EQ(3, v.yCount);

    struct Vowels v2 = { 0,0,0,0,0,0 };
    const char *sentence2 = "Why is it that C programming taxes your brain so much? You can spend hours looking at it "
                            "and you end up with a long cry.";

    ASSERT_EQ(35, countVowels(sentence2, &v2));
    ASSERT_EQ(8, v2.aCount);
    ASSERT_EQ(3, v2.eCount);
    ASSERT_EQ(7, v2.iCount);
    ASSERT_EQ(9, v2.oCount);
    ASSERT_EQ(6, v2.uCount);
    ASSERT_EQ(2, v2.yCount);
    
    struct Vowels v3 = { 0,0,0,0,0,0 };
    const char *sentence3 = "You like candy.";

    ASSERT_EQ(6, countVowels(sentence3, &v3));
    ASSERT_EQ(1, v3.aCount);
    ASSERT_EQ(1, v3.eCount);
    ASSERT_EQ(1, v3.iCount);
    ASSERT_EQ(1, v3.oCount);
    ASSERT_EQ(1, v3.uCount);
    ASSERT_EQ(1, v3.yCount);
}
