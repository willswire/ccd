#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

int writeNames(const char **fnames, const char **lnames, int sz, const char *fileName)
{
    if (sz <= 0 || fnames == NULL || lnames == NULL || fileName == NULL)
        return 0;

    FILE *file = fopen(fileName, "w+");
    if (file == NULL)
        return 0;
    
    for (int i = 0; i < sz; i++) {
        char *fname = strdup(*(fnames + i));
        char *lname = strdup(*(lnames + i));

        if (strlen(fname) == 0 || strlen(lname) == 0) {
            free(fname);
            free(lname);
            fclose(file);
            remove(fileName);
            file = NULL;
            return 0;
        }
        
        fname[0] = toupper(fname[0]);
        lname[0] = toupper(lname[0]);

        fputs(lname, file);
        fputs(", ", file);
        fputs(fname, file);
        if (i != (sz -1))
            fputc('\n', file);

        free(fname);
        free(lname);
    }

    fclose(file);

    return 1;
}
