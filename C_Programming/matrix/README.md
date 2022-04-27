# C Programming: Matrix
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.

## Tasks
Write the `processMatrix` function that manipulates an n x 5 matrix and returns the sum of all numbers after 
manipulation.

**PARAMETERS:**
1. `matrix`: A two dimensional int array that represents a matrix
2. `rows`: An int containing how many rows the matrix has

**RETURN:** An int of all numbers in the matrix added together after all other operations are done

- Assume `matrix` will not be NULL.
- The size of the array will be such that the there are always 5 columns but the number of rows will vary.
- This function needs to iterate through the entire array and do the following:
  - If both indices of the array are even numbers [0][0], [2][2] etc, then the value stored at that index should be 
    multiplied by two and stored back into that index.
  - If both indices of the array are odd numbers [1][1], [3][3] etc, then the value stored at that index should be 
    divided by two and stored back into that index (take note this is integer division).
  - All other elements should be unchanged.
- All values in the array should be added together after the updates are made and the function should return the total.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
