#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/*
 * Refer to README.md for the problem instructions
 *
 * @param sentence          The input string to process
 * @param frequencyTable    An already allocated buffer in which to place the output
 *
 * Expected Return Values:
 *    - The task is successful: 1
 *    - Bad input is provided: 0
 */

int letterFrequency(const char *sentence, int *frequencyTable)
{
    if (sentence == NULL || strlen(sentence) == 0) {
        return 0;
    }

    int alphaCount = 0;
    for (int i = 0; i < strlen(sentence); i++) {
        char c = (int) sentence[i];
        for (int k = 0; k < 26; k++) {
            if (c == (65 + k) || c == (97 + k)) {
                frequencyTable[k]++;
                alphaCount++;
            }
        }
    }

    return (alphaCount > 0);
}
