#include <stdlib.h>
#include <gtest/gtest.h>
#include "testcases.h"
#include "TestCode.h"
#include <stdio.h>
#include <stddef.h>

const char *testCodePath;
const char *memAllocError = "TEST COULD NOT ALLOCATE MEMORY; STOPPING TESTS.\n";

char *buildCommand(const char *commandFmt, const char *outFileName)
{
    int sz_command = 0;
    if (commandFmt == NULL || strncmp(commandFmt, "", 1) == 0)
    {
        printf("The command format string cannot be null\n");
        return NULL;
    }
    if (outFileName == NULL || strncmp(outFileName, "", 1) == 0)
    {
        sz_command = snprintf(NULL, 0, commandFmt, testCodePath) + 1;
    }
    else
    {
        sz_command = snprintf(NULL, 0, commandFmt, testCodePath, outFileName) + 1;
    }
    char *command = (char *) calloc(sz_command, sizeof(char));
    if (command != NULL)
    {
        if (outFileName == NULL || strncmp(outFileName, "", 1) == 0)
        {
            snprintf(command, sz_command, commandFmt, testCodePath);
        }
        else
        {
            snprintf(command, sz_command, commandFmt, testCodePath, outFileName);
        }
    }
    return command;
}

void checkFile(const char *fname, const char *words[], int wordslen)
{
    FILE *fp;
    int buflen = 128;
    char buf[buflen];
    int i = 0;
    int cmp;
    fp = fopen(fname, "r");
    ASSERT_FALSE(fname == NULL);
    ASSERT_FALSE(words == NULL);
    ASSERT_FALSE(fp == NULL);
    while(fgets(buf, buflen, fp))
    {
        buf[strcspn(buf, "\n")] = '\0';
        cmp = strcmp(words[i], buf);
        if(cmp)
        {
            printf("words[i]: %s\n buf: %s\n", words[i], buf);
        }
        ASSERT_EQ(0, cmp);
        i++;
    }
}

TEST(FileDumpTests, validInfo)
{
    const char *fname = "fileDumpTest.txt";
    const char *words[] = {"apple", "bagel", "cranberry", "donut"};

    remove(fname); // In case it wasn't removed
    int numWords = 4;
    fileDump(fname, words, numWords);

    checkFile(fname, words, numWords);
    // Cleanup files
    remove(fname);
}

TEST(FileDumpTests, NoArgs)
{
    const char *fname = "noArgs.txt";
    const char *words[] = {};
    int numWords = 0;

    remove(fname); // In case it wasn't removed
    int status = fileDump(fname, words, numWords);

    ASSERT_TRUE(status);
    checkFile(fname, words, numWords);
    // Cleanup files
    remove(fname);
}

TEST(FileDumpTests, nullFname)
{
    const char *fname = NULL;
    const char *words[] = {};
    int numWords = 0;
    int status = fileDump(fname, words, numWords);

    ASSERT_FALSE(status);
}

TEST(FileDumpTests, nullWords)
{
    const char *fname = "nullArgs.txt";
    const char **words = NULL;
    int numWords = 0;

    remove(fname); // In case it wasn't removed
    int status = fileDump(fname, words, numWords);

    ASSERT_FALSE(status);
    ASSERT_TRUE(fopen(fname, "r") == NULL);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests, normalUse)
{
    const char *fname = "testresults.txt";
    const char *words[] = {"apple", "bagel", "cranberry", "donut"};
    const char *commandFmt = "%s -f %s apple bagel cranberry donut";
    char *command = buildCommand(commandFmt, fname);
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 4);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests, longOption)
{
    const char *fname = "testresults.txt";
    const char *words[] = {"apple", "bagel", "cranberry", "donut"};
    const char *commandFmt = "%s --filename %s apple bagel cranberry donut";
    char *command = buildCommand(commandFmt, fname);
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 4);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests, defaultFile)
{
    const char *fname = "text.txt";
    const char *words[] = {"apple", "bagel", "cranberry", "donut"};
    const char *commandFmt = "%s apple bagel cranberry donut";
    char *command = buildCommand(commandFmt, "");
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 4);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests, fileNameIsParam)
{
    const char *fname = "apple";
    const char *words[] = {"bagel", "cranberry", "donut"};
    const char *commandFmt = "%s -f apple bagel cranberry donut";
    char *command = buildCommand(commandFmt, ""); // We technically didn't specify a file name
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 3);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests, fileNameIsParamLong)
{
    const char *fname = "apple";
    const char *words[] = {"bagel", "cranberry", "donut"};
    const char *commandFmt = "%s --filename apple bagel cranberry donut";
    char *command = buildCommand(commandFmt, ""); // We technically didn't specify a file name
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 3);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests, paramsWithNoFileName)
{
    const char *fname = "text.txt";
    const char *words[] = {"apple", "bagel", "cranberry", "donut"};
    const char *commandFmt = "%s apple bagel cranberry donut -f";
    char *command = buildCommand(commandFmt, "");
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 4);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests, NoArgs)
{
    const char *fname = "text.txt";
    const char *words[] = {"", "", "", ""};
    const char *commandFmt = "%s";
    char *command = buildCommand(commandFmt, "");
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 4);
    // Cleanup files
    remove(fname);
}

TEST(CommandlineTests,fileNoArgs)
{
    const char *fname = "testNoArg.txt";
    const char *words[] = {"", "", "", ""};
    const char *commandFmt = "%s -f %s";
    char *command = buildCommand(commandFmt, fname);
    if (command == NULL)
    {
        FAIL() << memAllocError;
        return;
    }

    remove(fname); // In case it wasn't removed
    int status = system(command);
    free(command);
    command = NULL;
    ASSERT_EQ(0, status);
    checkFile(fname, words, 4);
    // Cleanup files
    remove(fname);
}

int doTest(const char *binPath)
{
    int status = 0;
    char envVar[] = "CCOMMANDLINETEST= Running";
    const char *envVarName = "CCOMMANDLINETEST";
    ::testing::InitGoogleTest();

    // Set this so we only call the tests once
    putenv(envVar);
    
    testCodePath = binPath;

    status = RUN_ALL_TESTS();

    // Ensure the custom variable is removed before exiting
    unsetenv(envVarName);

    return status;
}
