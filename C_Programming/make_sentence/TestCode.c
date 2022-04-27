#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Refer to README.md for the problem instructions

char *makeSentence(const char *str)
{
    char *newSentence = malloc(sizeof(char) * strlen(str) * 2);
    int i = 1;
    int v = 1;
    newSentence[i - 1] = str[v - 1];
    while (str[i] != '\0')
    {
        switch ((int)str[i])
        {
        case 65 ... 90:
            newSentence[v] = ' ';
            v++;
            newSentence[v] = tolower(str[i]);
            break;
        default:
            newSentence[v] = str[i];
            break;
        }
        v++;
        i++;
    }

    if (strncmp("Who", newSentence, 3) &&
        strncmp("What", newSentence, 4) &&
        strncmp("Where", newSentence, 5) &&
        strncmp("When", newSentence, 4) &&
        strncmp("Why", newSentence, 3) &&
        strncmp("How", newSentence, 3))
    {
        newSentence[v] = '.';
    }
    else
    {
        newSentence[v] = '?';
    }

    newSentence[v + 1] = '\0';

    return newSentence;
}
