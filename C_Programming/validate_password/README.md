# C Programming: Validate Password
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the `validatePassword` function that will validate whether or not a password is valid.

**PARAMETERS:**
1. `password`: A character pointer to a string containing a plaintext password

**RETURN:** An int containing 1 if the password is valid or 0 otherwise

- If `password` is null return 0.
- A valid password adheres to the following rules:
    1. must be at least 8 and no more than 16 chars long
    2. must contain at least two capital letters
    3. must contain at least two lower-case letter
    4. must contain at least two digits
    5. must contain at least one of the following special characters:  !, #, or $
    6. any other characters are not allowed

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
