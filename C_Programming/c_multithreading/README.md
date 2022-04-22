# C Programming: C Multithreading
## KSAT List
This question is intended to evaluate the following topics:
- A0179: Implement file management operations.
- K0178: Understand how to exit a thread in multi-threading programs.
- K0182: Understand how to handle race conditions in multi-threading programs.
- K0174: Understand how to implement a pthread in multi-threading programs.
- K0176: Understand how to implement a join in multi-threading programs.
- K0180: Understand how to implement a mutex in multi-threading programs.
- K0173: Understand how to implement a thread in multi-threading programs.
- K0746: Understand how to open and close an existing file.
- K0747: Understand how to read, parse write file data.
- S0042: Open and close an existing file.
- S0043: Read, parse, write (append, insert, modify) file data.
- S0146: Utilize mutexes in a multithreaded program.
- S0144: Utilize threads in a multi-threaded program.

## Tasks
Implement a function `FindPrimes` that uses multithreading techniques to determine the prime numbers in a file and 
returns a status code.

**PARAMETERS:**
1. `fname`: a constant character pointer to the filename to read
2. `primes`: a pointer to an array of integers that will contain the prime numbers found
3. `numSize`: an int representing the length of the `primes` array

**RETURN:** an int containing `1` on success, or `0` if `fname` couldn't be opened or an input parameter is null

- Using multithreading, create 10 threads that will share the work of calculating which numbers in the file specified 
are prime.
- Properly protect resources shared by threads
- After all prime numbers are found, return the prime numbers via the primes parameter passed to FindPrimes
- You may modify the header file if needed.

## Prime Numbers
A prime number is any positive integer that has two factors, 1, and the number itself. e.g.: 2, 3, 5, 7, 11,...

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
