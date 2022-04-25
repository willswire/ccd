#include <gmock/gmock.h>
#include "TestCode.h"


TEST(EncryptVigenere_Tests, cornerCases)
{
    const char *plainTextList[] = {
        NULL,
        "",
        "~!$23#-=/*?, < >",
        " ",
        "attack them tomorrow",
        "ATTACK THEM TOMORROW"
    };

    const char *result1 = encryptVigenere(plainTextList[0], "key");
    ASSERT_EQ(NULL, result1);
    free((void *)result1);

    const char *result2 = encryptVigenere(plainTextList[1], "key");
    ASSERT_EQ(NULL, result2);
    free((void *)result2);

    const char *result3 = encryptVigenere(plainTextList[2], "key");
    ASSERT_EQ(0, strcmp("~!$23#-=/*?, < >", result3));
    free((void *)result3);

    const char *result4 = encryptVigenere(plainTextList[3], "key");
    ASSERT_EQ(0, strcmp(" ", result4));
    free((void *)result4);

    const char *result5 = encryptVigenere(plainTextList[4], "a");
    ASSERT_EQ(0, strcmp("attack them tomorrow", result5));
    free((void *)result5);

    const char *result6 = encryptVigenere(plainTextList[5], "a");
    ASSERT_EQ(0, strcmp("attack them tomorrow", result6));
    free((void *)result6);

    const char *result7 = encryptVigenere(plainTextList[4], "A");
    ASSERT_EQ(0, strcmp("attack them tomorrow", result7));
    free((void *)result7);

    const char *result8 = encryptVigenere(plainTextList[5], "A");
    ASSERT_EQ(0, strcmp("attack them tomorrow", result8));
    free((void *)result8);
}

TEST(EncryptVigenere_Tests, normalCases)
{
    const char *plainTextList[] = {
        "launch the rocket",
        " another secret message",
        "A Third Secret Message! ",
        "Message with number #123",
        "we are discovered save yourself"
    };

    const char *result1 = encryptVigenere(plainTextList[0], "IPSEC");
    ASSERT_EQ(0, strcmp("tpmrep izi twrciv", result1));
    free((void *)result1);

    const char *result2 = encryptVigenere(plainTextList[1], "ipsec");
    ASSERT_EQ(0, strcmp(" icgxjmg kieztl qgahskg", result2));
    free((void *)result2);

    const char *result3 = encryptVigenere(plainTextList[2], "IPsec");
    ASSERT_EQ(0, strcmp("i izmtl hwgtmi eiuapyi! ", result3));
    free((void *)result3);

    const char *result4 = encryptVigenere(plainTextList[3], "IpSec");
    ASSERT_EQ(0, strcmp("utkwcot omvp cmqdmg #123", result4));
    free((void *)result4);

    const char *result5 = encryptVigenere(plainTextList[4], "deceptive");
    ASSERT_EQ(0, strcmp("zi cvt wqngrzgvtw avzh cqyglmgj", result5));
    free((void *)result5);
}
