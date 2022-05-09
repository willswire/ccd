#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "TestCode.h"

// Refer to README.md for the problem instructions

struct nameNode *processNames(const char **names)
{
    // Check for NULL input
    if (names == NULL)
    {
        return NULL;
    }

    int namesLength = 10;
    struct nameNode *head = NULL;
    for (int i = 0; i < namesLength; i++)
    {
        if (names[i] == NULL)
        {
            return NULL;
        }
        else if (strlen(names[i]) != 0)
        {
            struct nameNode *newNode = malloc(sizeof(struct nameNode));
            newNode->name = (char *)names[i];
            newNode->next = NULL;

            if (head == NULL || (strcmp(head->name, newNode->name) > 0))
            {
                newNode->next = head;
                head = newNode;
            }
            else
            {
                struct nameNode *currentNode = head;
                while (currentNode->next != NULL && (strcmp(currentNode->next->name, newNode->name) < 0))
                {
                    currentNode = currentNode->next;
                }
                newNode->next = currentNode->next;
                currentNode->next = newNode;
            }
        }
    }

    return head;
}

void freeMemory(struct nameNode *head)
{
    struct nameNode *tmp;

    while (head != NULL)
    {
        tmp = head;
        head = head->next;
        free(tmp);
    }
}
