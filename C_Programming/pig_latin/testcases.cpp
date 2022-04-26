#include <gmock/gmock.h>
#include "TestCode.h"


TEST(EncodePigLatinPhrase_Tests, cornerCases)
{
    const char *englishPhrase = "";
    char *pigLatinPhrase = encodePigLatinPhrase(englishPhrase);
    ASSERT_EQ(0, strcmp("", pigLatinPhrase));
    free(pigLatinPhrase);
    pigLatinPhrase = NULL;

    const char *englishPhrase2 = " ";
    pigLatinPhrase = encodePigLatinPhrase(englishPhrase2);
    ASSERT_EQ(0, strcmp("", pigLatinPhrase));
    free(pigLatinPhrase);
    pigLatinPhrase = NULL;

    const char *englishPhrase3 = "       ";
    pigLatinPhrase = encodePigLatinPhrase(englishPhrase3);
    ASSERT_EQ(0, strcmp("", pigLatinPhrase));
    free(pigLatinPhrase);
    pigLatinPhrase = NULL;

    const char *englishPhrase4 = "word";
    pigLatinPhrase = encodePigLatinPhrase(englishPhrase4);
    ASSERT_EQ(0, strcmp("ordway", pigLatinPhrase));
    free(pigLatinPhrase);
    pigLatinPhrase = NULL;
}

TEST(EncodePigLatinPhrase_Tests, normalCases)
{
    const char *englishPhrase = "I study computer science";
    char *pigLatinPhrase = encodePigLatinPhrase(englishPhrase);
    ASSERT_EQ(0, strcmp("Iay tudysay omputercay ciencesay", pigLatinPhrase));
    free(pigLatinPhrase);
    pigLatinPhrase = NULL;
}
