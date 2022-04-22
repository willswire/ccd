# C Programming: C Palindrome
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement a function `palindrome` that determines whether a string is a palindrome and returns a status code.

**PARAMETERS:**
1. `phrase`: a constant character pointer to a string containing a potential palindrome

**RETURN:** an int containing `1` if `phrase` is a palindrome, `0` if it's not a palindrome, or `-1` if it's null

## Palindrome
A palindrome is a text phrase (excluding punctuation, spaces, and capitalization/case) that reads the same backwards 
or forwards. For example each of the following are palindromes: 

```text
Able was I ere I saw Elba.
A nut for a jar of tuna
Taco cat
Was it a car or a cat I saw?
Ed, I saw Harpo Marx ram Oprah W. aside.
```

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
