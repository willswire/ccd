# C Programming: Pass By Reference
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0050: Implement a function that doesn't return a value.
- S0051: Implement a function with pass by reference using the & reference operator.
- S0048: Implement a function that receives input parameters.
- S0097: Create and use pointers.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `refFunction` that manipulates values passed in by reference based on a specified mode.

**PARAMETERS:**
1. `first`: An int passed by reference that is one of the parameters that can be changed by the function
2. `second`: An int passed by reference that is one of the parameters that can be changed by the function
3. `action`: An int indicating an action to take on the values passed in `first` and `second` detailed below

**RETURN:** void

- Assume `first` and `second` are not null.
- The `action` variable should have either a 1, 2, or 3. 
  1. If `second` is smaller than `first`, then swap the values in `first` and `second`; otherwise, do nothing. For 
     example, if the function is called with `refFunction(8, 6, 1)`, when the function completes `first` will contain 6 
     and `second` will contain 8.
  2. If `first` is smaller than `second`, then swap the values in `first` and `second`, otherwise do nothing. For 
     example, if the function is called with `refFunction(4, 6, 2)`, when the function completes `first` will contain 6 
     and `second` will contain 4.
  3. Multiply the value inside of `first` and `second` each by two (2). For example, if the function is called with 
     `refFunction(5, 2, 3)`, when the function completes `first` will contain 10 and `second` will contain 4.
- If the `action` variable contains a value < 1 or > 3, assign 0 to both `first` and `second`.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
