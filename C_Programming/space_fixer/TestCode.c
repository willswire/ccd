#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

char *spaceFixer(const char *text)
{
    if (text == NULL || strlen(text) == 0)
        return NULL;

    char *para = calloc(202, sizeof(char));

    int wi = 0;
    for (int i = 0; i < strlen(text); i++) {
        para[wi] = text[i];
        
        if (text[i] == '.' || text[i] == '?') {
            para[wi + 1] = ' ';
            para[wi + 2] = ' ';
            wi += 2;

            while(text[i + 1] == ' ') {
                i++;
            }
        }
        
        wi++;
    }

    para[wi - 2] = '\0';

    return para;
}
