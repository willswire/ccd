# Python: Counting Pieces
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0026: Utilize standard library modules.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.

## Tasks
Implement the function `count_pieces` that counts the number of digits, non-digit characters (excluding white spaces), 
whitespace characters and words in a string.

**PARAMETERS:**
1. `testString`: a string needing statistical data on its characters and words

**RETURN:** a list of integers that represents the various character and word counts

### Example
For the string `We have 8 digits.`, the output list will be [1, 13, 3, 4].

- 1: digits (ONLY 8)
- 13: non-digit characters (excluding white spaces)
- 3: white spaces
- 4: words

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
