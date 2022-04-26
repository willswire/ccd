#include "TestCode.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Refer to README.md for the problem instructions

int searchFile(const char *fname, const char *str)
{
    FILE *file = fopen(fname, "r");
    if (file == NULL || fname == NULL || strlen(fname) == 0)
        return -2;

    if (str == NULL || strlen(str) == 0)
        return -3;

    char tempWord[150];
    char currentChar = ' ';
    int wordLength = 0;
    int fileSize = -1;
    int occurances = 0;

    while (currentChar != EOF)
    {
        currentChar = fgetc(file);
        if (isalpha(currentChar) && strlen(str) != wordLength)
        {
            tempWord[wordLength] = currentChar;
            wordLength++;
        }
        else
        {
            if (wordLength > 0)
            {
                char candidate[wordLength + 1];
                candidate[wordLength] = '\0';
                strncpy(candidate, tempWord, wordLength);
                if (strcmp(candidate, str) == 0)
                {
                    occurances++;
                }
                memset(tempWord, 0, strlen(str) * sizeof(char));
                wordLength = 0;
            }
        }
        fileSize++;
    }

    if (fileSize <= 150)
        return -1;

    return occurances;
}
