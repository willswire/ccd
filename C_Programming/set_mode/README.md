# C Programming: Set Mode
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0099: Use pointer arithmetic to traverse an array.
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
In statistics, the mode of a set of values is the value that occurs most often or with the greatest frequency. 
Implement the function `getMode` that determines an input array's mode by finding the most frequent value and returns 
the discovered mode.

- **IMPORTANT:** In this function, **use pointer notation** instead of array notation
  - See KSAT S0099 above

**PARAMETERS:**
- `array`: An int pointer that points to an array of integers
- `size`: An int that indicates the number of elements in the array

**RETURN:** An int: >= 0 representing the mode, -1 if none of the values occur more than once, -2 if `array` is null, or 
-3 if memory is unavailable

- Assume the array will always contain nonnegative values.
- If there are ties select any mathematically correct option.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
