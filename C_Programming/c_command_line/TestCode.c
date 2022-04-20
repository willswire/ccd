#include <stdio.h>
#include <string.h>
#include "testcases.h"
#include "TestCode.h"

// Refer to README.md for the problem instructions

int fileDump(const char *fname, const char *words[], int wordLen) {

    if (fname == NULL || words == NULL) {
        return 0;
    }

    FILE *file = fopen(fname, "w");

    for (int i = 0; i < wordLen; i++) {
        fprintf(file, "%s\n", words[i]);
    }

    fclose(file);

    return 1;
}

int main(int argc, char *argv[])
{
    char *defaultFname = "text.txt";
    char *customFname = "text.txt";
    char *shortOption = "-f";
    char *longOption = "--filename";

    FILE *file = fopen(defaultFname, "w");

    for (int i = 1; i < argc; i++) {
        printf("Argument %i is: %s\n", i, argv[i]);

        if (strcmp(argv[i],shortOption) == 0 || strcmp(argv[i],longOption) == 0) {
            char *passedName = argv[i + 1];
            if (passedName != NULL) {
                customFname = passedName;
                printf("The filename is: %s\n", customFname);
                i++;
            }
        } else {
            fprintf(file, "%s\n", argv[i]);
        }
    }

    fclose(file);

    if (strcmp(defaultFname, customFname) != 0) {
        rename(defaultFname, customFname);
    }

    /* DO NOT MOVE OR MODIFY THE FOLLOWING CODE*/
    /* YOUR SOLUTION SHOULD BE CONTAINED ABOVE THIS POINT*/
    if (getenv("CCOMMANDLINETEST") == NULL)
    {
        doTest(argv[0]);
    }

    return 0;
}
