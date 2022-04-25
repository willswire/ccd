# C Programming: Vigenere Cipher
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0053: Implement a function that returns a memory reference.
- S0079: Validate expected input.
- S0090: Allocate memory on the heap (malloc).
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0110: Implement error handling.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the function `encryptVigenere` that encrypts a string of plain text with a key and returns the resulting 
encrypted string.

**PARAMETERS:**
1. `input`: A character pointer to the plaintext string to encrypt
2. `key`: A character pointer to a string that will be used as the cipher's key

**RETURN:** A character pointer to the allocated string containing the encrypted message, or `NULL` if `input` or `key` 
are `NULL` or zero length arrays

- You must convert all uppercase letters to lowercase letters.
- Use a Vigenere cipher, detailed below, to encrypt `input`.

### The Vigenere cipher
The Vigenere cipher is a method of encrypting alphabetic text. To encrypt a message, a key is needed that is as long 
as the message. Usually, the key is a ***repeating*** keyword. The encryption is done by adding a letter from the 
plain text to a letter of the key. Each letter in the alphabet is given an index:

- a = 0, b = 1, c = 2, d = 3, e = 4,........, w = 22, x = 23, y = 24, and z = 25

For example, if the keyword is `deceptive`, the message `we are discovered save yourself` is encrypted as:

```text
plaintext:    we are discovered save yourself
key:          de cep tivedecept ived eceptive
ciphertext:   zi cvt wqngrzgvtw avzh cqyglmgj
```

The cipher letter `z` is the result of `w` + `d`, which is 22 + 3 = 25. ***Note:*** that `y` + `e` = `c` because 
(24 + 4) mod 26 = 2, which is c. In general, the encryption is done as follows:

```text
Plaintext  P = (p0, p1, ...,pn-1)
Key        K = (k0, k1, ...,km-1)   ----> The original key length is m and the key will be repeated to match length of the plaintext
Ciphertext C = (c0, c1, ...,cn-1)
```

ENCRYPTION FORMULA: `ci = [pi + k(i mod m)] mod 26`

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
