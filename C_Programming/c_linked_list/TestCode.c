#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions
const int NAMES_LENGTH = 10;

struct nameNode *processNames(const char **names)
{
    // Check if `names` is null
    if (names == NULL) {
        return NULL;
    }

    struct nameNode *head;

    struct nameNode *temp;
    for (int i = NAMES_LENGTH - 1; i <= 0; i--) {
        char *currentName = (char *) names[i];
        if (currentName != "") {
        }
    }

    // int firstNameValue = __INT_MAX__;
    // char *firstName;

    // // For each name in names...
    // for (int i = 0; i < NAMES_LENGTH; i++) {

    //     // Check if the value is NULL
    //     if (names[i] == NULL) {
    //         return NULL;
    //     }

    //     // Get the value of the name
    //     int nameValue = 0;
    //     for (int j = 0; j < strlen(names[i]); j++) {
    //         nameValue += (int) names[i][j];
    //     }

    //     // If it is less than the current name
    //     // set a new firstName
    //     if (nameValue < firstNameValue) {
    //         firstNameValue = nameValue;
    //         firstName = (char *) names[i];
    //     }
    // }
    // printf("The first name in the list is %s", firstName);
    
    return head;
}

void freeMemory(struct nameNode *head)
{

}
