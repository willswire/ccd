# C Programming: Binary/Hex String to Integer
## KSAT List
This question is intended to evaluate the following topics:
- A0018: Analyze a problem to formulate a software solution.
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
Implement a function `bin_hex_StrToInt32` that converts a string, containing either a hexadecimal or binary number, 
into the string's integer value (base 10) and returns the converted value.

**PARAMETERS:**
1. `s`: a const char pointer representing a string containing either a binary or hexadecimal number.
2. `mode`: an int representing the conversion mode: 1 is for binary and 2 is for hexadecimal.

**RETURN:** an int containing the base 10 value of the hex or binary string; or `ERROR_INVALID_PARAMETER` if the input 
parameter is null, empty, or an invalid mode

- Assume a mode value other than 1 or 2 is invalid.

**Note:** Do not call built-in library functions that accomplish these tasks automatically.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
