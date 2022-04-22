#include <gmock/gmock.h>
#include "TestCode.h"

#define SIZE 10

TEST(Palindrome_Tests, normalCases)
{
    ASSERT_EQ(1, palindrome("Able was I ere I saw Elba."));
    ASSERT_EQ(1, palindrome("A nut for a jar of tuna"));
    ASSERT_EQ(1, palindrome("Taco cat"));
    ASSERT_EQ(1, palindrome("Was it a car or a cat I saw ?"));
    ASSERT_EQ(1, palindrome("Ed, I saw Harpo Marx ram Oprah W.aside."));
    ASSERT_EQ(1, palindrome("abcdcba"));
    ASSERT_EQ(0, palindrome("This is not a palindrome."));
    ASSERT_EQ(0, palindrome("abababababababab"));
}

TEST(Palindrome_Tests, nullCases)
{
    ASSERT_EQ(-1, palindrome(NULL));
    ASSERT_EQ(0, palindrome(""));
}
