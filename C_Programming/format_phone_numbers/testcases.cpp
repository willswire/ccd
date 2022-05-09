#include <gmock/gmock.h>
#include "TestCode.h"

    
#define SIZE 10

TEST(testFormatNums, simple_case)
{
    const char *nums[10] = { "(210)3157904","2103157904","1031376904","(210) 3157904",
                             "7210313704","210-315-7904","210 315 7904","(210) 315-7904",
                             "8888675309","2103157904" };

    const char *check[10] = { "(210) 315-7904","(210) 315-7904","(103) 137-6904","(210) 315-7904",
                              "(721) 031-3704","(210) 315-7904","(210) 315-7904","(210) 315-7904",
                              "(888) 867-5309","(210) 315-7904" };

    char **res = formatNums(nums);

    if (res == NULL)
    {
        FAIL() << "formatNums returned a NULL pointer";
    }

    for (int i = 0; i < 10; i++)
    {
        ASSERT_EQ(0, strcmp(res[i], check[i]));
        free(res[i]);
        res[i] = NULL;
    }

    free(res);
    res = NULL;
}
TEST(testFormatNums, bad_sizes)
{
    const char *nums2[10] = { "(210)3137904","21031376904","1031376904","(210) 3137904",
                              "7210313704","210-313-7904","210 313 7904","(210) 313-7904",
                              "8888675309","2103137904" };

    ASSERT_EQ(NULL, formatNums(nums2));
}

TEST(testFormatNums, edge_cases)
{

    const char *nums3[10] = { "(210)--333--7999","210--388--7904","103  1376  904","(210)(313)8282",
                              "-721,-031 3704","200 303 7904","210#313#7500","(3333) 23-3404",
                              "888867 5309","   1213337999 " };

    const char *check2[10] = { "(210) 333-7999","(210) 388-7904","(103) 137-6904","(210) 313-8282",
                               "(721) 031-3704","(200) 303-7904","(210) 313-7500","(333) 323-3404",
                               "(888) 867-5309","(121) 333-7999" };

    char **res = formatNums(nums3);

    if (res == NULL)
    {
        ASSERT_EQ(1, 0);
    }

    for (int i = 0; i < 10; i++)
    {
        ASSERT_EQ(0, strcmp(res[i], check2[i]));
        free(res[i]);
        res[i] = NULL;
    }

    free(res);
    res = NULL;
}
