#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "TestCode.h"

#define MAX_THREADS 10
#define PRIME_CAPACITY 10000

// THIS PROGRAM IS NOT MULTITHREADED YET!!!
// Refer to README.md for the problem instructions

int FindPrimes(const char *fname, int *primes, int numSize)
{
    if (fname == NULL || primes == NULL) {
        return 0;
    }

    FILE *file = fopen(fname, "r");
    if (file == NULL) {
        return 0;
    }

    const int MAX_SIZE = 4 * sizeof(char);
    char numberString[MAX_SIZE];
    int count = 0;
    while(fgets(numberString, MAX_SIZE, file)) {
        int factor = 2;
        int number = atoi(numberString);

        while (number % factor != 0) {
            factor++;
        }
        if (factor == number) {
            printf("%i\n", number);
            primes[count] = number;
            count++;
        }
    }

    fclose(file);
    return 1;
}
