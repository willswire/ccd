#include <gmock/gmock.h>
#include "TestCode.h"


TEST(ValidatePassword_Tests, cornerCases)
{
    ASSERT_EQ(0, validatePassword(" 0nesPac3!nfronT"));
    ASSERT_EQ(0, validatePassword("0nesPac3!nbaCk# "));
    ASSERT_EQ(0, validatePassword(" sPac3$fR0ntBak "));
    ASSERT_EQ(0, validatePassword(" sPac3 a!L 0v3r "));
    ASSERT_EQ(1, validatePassword("#21OIuyd"));
    ASSERT_EQ(1, validatePassword("34eRdFa#"));
    ASSERT_EQ(1, validatePassword("#21OIuyda34RdFa#"));
    ASSERT_EQ(1, validatePassword("!56vwBVC"));
    ASSERT_EQ(1, validatePassword("vw56rBVC78ZXlkj!"));
    ASSERT_EQ(1, validatePassword("!78ZXlj!"));
    ASSERT_EQ(1, validatePassword("$90HGfds78trEWQ6"));
    ASSERT_EQ(1, validatePassword("EW78trQ$"));
    ASSERT_EQ(1, validatePassword("$78trEQ$"));
    ASSERT_EQ(0, validatePassword("1L7r$hT"));
    ASSERT_EQ(0, validatePassword("0ne!L3tTer$2#maNy"));
    ASSERT_EQ(0, validatePassword(" "));
    ASSERT_EQ(0, validatePassword("\n"));
    ASSERT_EQ(0, validatePassword("\t"));
}


TEST(ValidatePassword_Tests, normalCases)
{
    ASSERT_EQ(1, validatePassword("AAbb233!"));
    ASSERT_EQ(0, validatePassword("AAbb233"));
    ASSERT_EQ(1, validatePassword("1Wantt0G3tin!#"));
    ASSERT_EQ(0, validatePassword("1Wantt0G3tin"));
    ASSERT_EQ(0, validatePassword("1Wantt0G3tin!#abc123"));
    ASSERT_EQ(0, validatePassword("Aabb233!"));
    ASSERT_EQ(0, validatePassword("ABBb233!"));
    ASSERT_EQ(0, validatePassword("AAbbcc3!!!"));
    ASSERT_EQ(1, validatePassword("Th1s1sAt16Chars#"));
}

TEST(ValidatePassword_Tests, nullCases)
{
    ASSERT_EQ(0, validatePassword(NULL));
    ASSERT_EQ(0, validatePassword(""));
}