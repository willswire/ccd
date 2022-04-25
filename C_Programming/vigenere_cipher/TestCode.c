#include <stdlib.h>
#include <string.h>
#include <ctype.h> 
#include "TestCode.h"

// Refer to README.md for the problem instructions

const char *encryptVigenere(const char *input, const char *key)
{
    if (input == NULL || strlen(input) == 0)
        return NULL;
    if (key == NULL || strlen(key) == 0)
        return NULL;

    
    char *cipherText = calloc((strlen(input) + 1), sizeof(char));
    int m = strlen(key);

    int keyIndex = 0;
    for (int i = 0; i < strlen(input); i++) {
        if (isalpha(input[i])) {
            char p = tolower(input[i]);
            int pi = ((int) p) - 'a';
            char k = tolower(key[keyIndex % m]);
            int ki = ((int) k) - 'a';
            cipherText[i] = ((pi + ki) % 26) + 'a';
            keyIndex++;
        } else {
            cipherText[i] = input[i];
        }
    }
    
    return cipherText;
}
