# Refer to README.md for the problem instructions


def sieve_of_Eratosthenes():
    UPPER_BOUND = 999
    i = 1
    primes = [i] * UPPER_BOUND

    index = 2
    while index < UPPER_BOUND:
        if primes[index]:
            subIndex = index * 2
            while subIndex < UPPER_BOUND:
                primes[subIndex] = 0
                subIndex += index
        index += 1

    primeNums = []
    for p in range(2, UPPER_BOUND):
        if primes[p]:
            primeNums.append(p)

    return primeNums
