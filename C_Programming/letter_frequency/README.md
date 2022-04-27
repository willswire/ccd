# C Programming: Letter Frequency
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
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the function `letterFrequency` that determines the total occurrences of each letter of the alphabet in a 
string and returns a status code.

**PARAMETERS:**
1. `sentence`: A character pointer to a string containing the letters to count
2. `frequencyTable`: A pointer to a 26 element integer array corresponding to each letter

**RETURN:** an int containing 1 for success, or 0 if `sentence` is null or has no letters

- Assume that `frequencyTable` is not null and has 26 elements.
- The indices of `frequencyTable` correspond to each letter in the alphabet in alphabetical order.
- Every time a letter is encountered increment its respective element.
- Case sensitivity is not an issue i.e. `A` and `a` are considered the same for this question. 
- If a non-alpha character is encountered it should be ignored, adding nothing to any count.


## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
