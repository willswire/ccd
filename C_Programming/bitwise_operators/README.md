# C Programming: Bitwise Operators
## KSAT List
This question is intended to evaluate the following topics:
- A0018: Analyze a problem to formulate a software solution.
- S0030: Utilize bitwise operators to manipulate binary values.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `bitwiseOps` that performs a series of bitwise operations on a binary value and returns the 
resulting bitwise calculation.

**PARAMETERS:**
1. `first`: a const char pointer representing a binary number
2. `second`: a const char pointer representing a binary number

**RETURN:** an int containing the result of the bitwise calculation; `-1` if `first` or `second` is null or not 16 characters; or `-2` if any 
characters in `first` or `second` are not `1` or `0`

The `bitwiseOps` function will convert each binary representation to its equivalent integer value. So, for example, if 
the string passed is '0000000000001111', this will be converted to 15. After each string is converted, the function 
will do the following:

1. If both values are even numbers, use the bitwise 'and' operator to 'and' the values together and return the results.
2. If instead both values are odd numbers, use the bitwise 'or' operator to 'or' the values together and return the 
   results.
3. If the previous two conditions are not met, and both values are > 255 then use the bitwise 'xor' operator to 'xor' 
  the values together and return the results.
4. Otherwise, if none of the above apply, add the two values together and return the results.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.

