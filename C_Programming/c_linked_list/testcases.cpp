#include <gmock/gmock.h>
#include "TestCode.h"
    

TEST(ProcessNames_Tests, normalCases)
{
    const char *names[] = { "Joe", "Ace", "Gene", "Paul", "Peter", "Hank", "Timmy", "Sarah", "Alice", "Carol" };
    const char *names2[] = { "Ace", "Alice", "Carol", "Gene", "Hank", "Joe", "Paul", "Peter", "Sarah", "Timmy" };
    struct nameNode *res = processNames(names);
    struct nameNode *head = res;
    int i = 0;
    while (res != NULL)
    {
        ASSERT_EQ(0, strcmp(res->name, names2[i]));
        res = res->next;
        i++;
    }
    ASSERT_EQ(sizeof(names2) / sizeof(*names2), i);
    freeMemory(head);

    const char *names3[] = {
        "Jon", "Arya", "Sansa", "Joffrey", "Gregor", "Cersei", "Jamie", "Brienne", "Daenerys", "Tyrion" 
    };
    const char *names4[] = {
        "Arya", "Brienne", "Cersei", "Daenerys", "Gregor", "Jamie", "Joffrey", "Jon", "Sansa", "Tyrion" 
    };
    res = processNames(names3);
    head = res;
    i = 0;
    while (res != NULL)
    {
        ASSERT_EQ(0, strcmp(res->name, names4[i]));
        res = res->next;
        i++;
    }
    ASSERT_EQ(sizeof(names4) / sizeof(*names4), i);
    freeMemory(head);
}

TEST(ProcessNames_Tests, cornerCases)
{
    const char *names[] = {"", "Fred", "Anne", "", "Thomas", "Bill", "Rick", "", "Porter", "Susan"};
    const char *namesSorted[] = {"Anne", "Bill", "Fred", "Porter", "Rick", "Susan", "Thomas"};
    struct nameNode *res = processNames(names);
    struct nameNode *head = res;
    int i = 0;
    while (res != NULL)
    {
        ASSERT_EQ(0, strcmp(res->name, namesSorted[i]));
        res = res->next;
        i++;
    }
    ASSERT_EQ(sizeof(namesSorted) / sizeof(*namesSorted), i);
    freeMemory(head);
}

TEST(ProcessNames_Tests, nullCases)
{
    const char *names1[] = {NULL};
    const char *names2[] = {"", "", "", "", "", "", "", "", "", ""};

    ASSERT_TRUE(NULL == processNames(NULL));
    ASSERT_TRUE(NULL == processNames(names1));
    ASSERT_TRUE(NULL == processNames(names2));
}
