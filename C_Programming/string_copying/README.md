# C Programming: String Copying
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
- S0050: Implement a function that doesn't return a value.
- S0048: Implement a function that receives input parameters.
- S0099: Use pointer arithmetic to traverse an array.
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.

## Tasks
These tasks focus on the difference between array index notation and pointer arithmetic.

### Task 1
Implement a function called `Copy1` that uses array index notation to copy the source string to the destination string.

**PARAMETERS:**
- `dest` a constant pointer to non-constant char where the correctly formatted paragraph is stored
- `src` a pointer to a constant char containing the paragraph for correction

**RETURN:** void

- Your function should enforce the ***principle of least privilege***, meaning it shouldn't modify `src`.
- Ensure to check for null input parameters.

### Task 2
Implement a function called `Copy2` that uses pointers and pointer arithmetic to copy the source string to the 
destination string.

**PARAMETERS:**
- `dest` a pointer to non-constant char where the correctly formatted paragraph is stored
- `src` a pointer to a constant char containing the paragraph for correction

**RETURN:** void

- Your function should enforce the ***principle of least privilege***, meaning it shouldn't modify `src`.
- Ensure to check for null input parameters.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
