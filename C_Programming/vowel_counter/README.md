# C Programming: Vowel Counter
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0079: Validate expected input.
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0156: Utilize a struct composite data type.

## Tasks
Implement a function `countVowels` that computes the total number of vowels in a sentence and return the total.

**PARAMETERS:**
1. `text`: a char pointer to a string containing a sentence
2. `v`: A pointer to a `vowels` struct (defined in `TestCode.h`) that will be used to pass the total number of each 
   vowel

**RETURN:** An int containing the total number of vowels in the string; if `text` is empty or NULL, return `ERROR_EMPTY`

- Count the number of individual vowels in the sentence and increment the associated counter in the struct.
  - `aCount` for 'a' or 'A' etc.
- y is considered a vowel if it does **not** start a word.
- If a y is anywhere else in a word it is considered a vowel.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
