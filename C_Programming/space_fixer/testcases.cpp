#include <gmock/gmock.h>
#include "TestCode.h"


TEST(SpaceFixer_Tests, cornerCases)
{
    const char *sentence = "";
    char *result = spaceFixer(sentence);
    EXPECT_STREQ(NULL, spaceFixer(result));
    if (result != NULL)
        free(result);

    sentence = NULL;
    result = spaceFixer(result);
    EXPECT_STREQ(NULL, spaceFixer(sentence));
    if (result != NULL)
        free(result);
}


TEST(SpaceFixer_Tests, normalCases)
{
    const char *sentence = "Yesterday, all my trouble seemed so far away.Now they are here to stay.      Do I "
                           "believe in yesterday? Suddenly, yes.   ";
    const char *fixed = "Yesterday, all my trouble seemed so far away.  Now they are here to stay.  Do I believe in "
                        "yesterday?  Suddenly, yes.";
    char *result = spaceFixer(sentence);
    EXPECT_STREQ(fixed, result);
    if (result != NULL)
        free(result);

    const char *sentence2 = "This long paragraph has exactly 200 characters.      If you don't allocate memory "
                            "correctly then you'll get a buffer overflow.     Buffer overflows can be caused if you "
                            "go beyond the last index of the array.";
    const char *fixed2 = "This long paragraph has exactly 200 characters.  If you don't allocate memory correctly "
                         "then you'll get a buffer overflow.  Buffer overflows can be caused if you go beyond the "
                         "last index of the array.";
    result = spaceFixer(sentence2);
    EXPECT_STREQ(fixed2, result);
    if (result != NULL)
        free(result);
}
