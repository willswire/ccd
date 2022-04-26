#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

char *encodePigLatinPhrase(const char *englishPhrase)
{
    if (*englishPhrase =='\0')
        return strdup("");

    int isWhiteSpace = 0;
    for (int i = 0; i < strlen(englishPhrase); i++)
        isWhiteSpace += isspace(englishPhrase[i]);
    if (isWhiteSpace)
        return strdup("");
    
    char *pigLatinPhrase = malloc(sizeof(char) * 81);

    printf("\nOUTPUT: %s\n", pigLatinPhrase);
    return pigLatinPhrase;
}
