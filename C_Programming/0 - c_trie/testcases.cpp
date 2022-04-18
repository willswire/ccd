#include <gmock/gmock.h>
#include <string.h>
#include "TestCode.h"

static struct Node *multiUseTrie;

TEST(TrieTest, PartialCases)
{
    struct Node *trie;
    const char *words[] = {"test", "testing", "bagel", "sandwich", "basket"};
    trie = buildTree(words, 5);

    ASSERT_EQ(0, findWord(trie, "sand"));
    ASSERT_EQ(1, findWord(trie, "bagel"));
    deleteTree(&trie);
}

TEST(TrieTest, smallCases)
{
    const char *word[] = {"test"};

    multiUseTrie = buildTree(word, 1);
}

TEST(TrieTest, deleteCases)
{
    deleteTree(&multiUseTrie);
}

TEST(TrieTest, normalCases)
{
    struct Node *trie;
    const char *words[] = {"test", "testing", "bagel", "sandwich", "basket"};

    trie = buildTree(words, 5);

    ASSERT_EQ(1, findWord(trie, "test"));

    ASSERT_EQ(0,findWord(trie, "tests"));
    addWord(trie,"tests");
    ASSERT_EQ(1,findWord(trie, "tests"));
    deleteTree(&trie);
    ASSERT_EQ(NULL, trie);
}

TEST(TrieTest, upperCases)
{
    struct Node *trie;
    const char *words[] = {"test", "tesTing", "baGeL", "sandwich", "basket"};

    trie = buildTree(words, 5);

    ASSERT_EQ(1, findWord(trie, "testing"));
    ASSERT_EQ(1, findWord(trie, "bagel"));
    ASSERT_EQ(1, findWord(trie, "bAgel"));
    ASSERT_EQ(1, findWord(trie, "baGel"));
    ASSERT_EQ(1, findWord(trie, "baGeL"));
    ASSERT_EQ(1, findWord(trie, "BAGEL"));

    addWord(trie,"PiZzA");
    ASSERT_EQ(1, findWord(trie, "pizza"));
    ASSERT_EQ(1, findWord(trie, "pizZa"));

    deleteTree(&trie);
    ASSERT_EQ(NULL, trie);
}