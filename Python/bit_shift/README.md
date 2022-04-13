# Python: Bit Shift
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0030: Utilize bitwise operators to manipulate binary values.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `convertAndShift` so it converts a 16-character string of 1's and 0's to a base 10 integer value 
and then performs a binary algorithm, which is explained below, on the converted value. When complete, the function 
returns the computed value.

**PARAMETERS:**
1. `bStr`: a str representing a binary number of 1's and 0's

**RETURN:** an int containing the calculated value, the string `"INVALID_LENGTH"` if `bStr` is not 16 characters, or the string `"INVALID_VALUE"` if `bStr` contains anything other than `1` or `0`

### Binary Algorithm
After conversion to a base 10 integer, if the value is an even number, use the binary left shift operator to move the value's bits two positions. Otherwise, use the binary right shift operator to move the value's bits one position. If the resulting value of either of the shifts is greater than 200, apply the binary one's complement to the value. 

### Example
The function `convertAndShift` receives the string `"0000000010101010"`, converts it to `170` and returns `-171`.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
