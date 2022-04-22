#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Refer to README.md for the problem instructions

int palindrome(const char *phrase)
{
    if (phrase == NULL) {
        return -1;
    } else if (strcmp(phrase, "") == 0) {
        return 0;
    }

    char *formattedPhrase = calloc(sizeof(char), strlen(phrase) + 1);

    int formattedIndex = 0;
    for(int i = 0; i < strlen(phrase); i++){
        if (isalnum(phrase[i])) {
            formattedPhrase[formattedIndex] = tolower(phrase[i]);
            formattedIndex++;
        }
    }

    int l = 0;
    int r = strlen(formattedPhrase) - 1;
    while (formattedPhrase[l] == formattedPhrase[r] && l != r) {
        l++;
        r--;
        if (l == r) {
            free(formattedPhrase);
            return 1;
        }
    }
    
    free(formattedPhrase);
    return 0;
}
