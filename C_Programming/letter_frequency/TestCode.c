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

    int table[26] = { 0 };
    frequencyTable = table;
    for (int i = 0; i < strlen(sentence); i++) {
        switch (sentence[i])
        {
        case 'A':
        case 'a':
            frequencyTable[0]++;
            break;
        case 'B':
        case 'b':
            frequencyTable[1]++;
            break;
        case 'C':
        case 'c':
            frequencyTable[2]++;
            break;
        case 'D':
        case 'd':
            frequencyTable[3]++;
            break;
        case 'E':
        case 'e':
            frequencyTable[4]++;
            break;
        case 'F':
        case 'f':
            frequencyTable[5]++;
            break;
        case 'G':
        case 'g':
            frequencyTable[6]++;
            break;
        case 'H':
        case 'h':
            frequencyTable[7]++;
            break;
        case 'I':
        case 'i':
            frequencyTable[8]++;
            break;
        case 'J':
        case 'j':
            frequencyTable[9]++;
            break;
        case 'K':
        case 'k':
            frequencyTable[10]++;
            break;
        case 'L':
        case 'l':
            frequencyTable[11]++;
            break;
        case 'M':
        case 'm':
            frequencyTable[12]++;
            break;
        case 'N':
        case 'n':
            frequencyTable[13]++;
            break;
        case 'O':
        case 'o':
            frequencyTable[14]++;
            break;
        case 'P':
        case 'p':
            frequencyTable[15]++;
            break;
        case 'Q':
        case 'q':
            frequencyTable[16]++;
            break;
        case 'R':
        case 'r':
            frequencyTable[17]++;
            break;
        case 'S':
        case 's':
            frequencyTable[18]++;
            break;
        case 'T':
        case 't':
            frequencyTable[19]++;
            break;
        case 'U':
        case 'u':
            frequencyTable[20]++;
            break;
        case 'V':
        case 'v':
            frequencyTable[21]++;
            break;
        case 'W':
        case 'w':
            frequencyTable[22]++;
            break;
        case 'X':
        case 'x':
            frequencyTable[23]++;
            break;
        case 'Y':
        case 'y':
            frequencyTable[24]++;
            break;
        case 'Z':
        case 'z':
            frequencyTable[25]++;
            break;
        default:
            break;
        }
        i++;
    }

    return 1;
}
