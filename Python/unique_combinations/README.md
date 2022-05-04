# Python: Unique Combinations
## KSAT List
This question is intended to evaluate the following topics:
- A0061: Create and implement functions to meet a requirement.
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0026: Utilize standard library modules.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.

## Tasks
Implement the function `count_unique_permutations` that will return a count of the unique permutations of the
characters in a string.

**PARAMETERS**
1. `input_str`: A string to calculate permutations of its contents

**RETURN:** An int containing the total number of permutations in which the letters in the string can be arranged

## Note
You may not use any mathematical formula to calculate the result. You may not use the in-built 
`itertools.permutations` function to generate your permutations.

### Example
- The only permutation of 'aaaa' is 'aaaa', so the function would return 1.
- Permutations of 'aaab' are ''aaab', 'aaba', 'abaa', and 'baaa', so the function will return 4.
- A string containing 'abc' would have 6.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
