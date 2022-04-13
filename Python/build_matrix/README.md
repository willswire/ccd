# Python: Build Matrix
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `buildMatrix` so it creates a two-dimensional array according to the algorithm explained below 
and then returns the array when finished.

**PARAMETERS:**
1. `rows`: an int containing the number of rows for the two-dimensional array
2. `cols`: an int containing the number of columns for the two-dimensional array

**RETURN:** a list of lists representing the two-dimensional array or an empty list if `rows` or `cols` is less than or 
equal to 1

### Two-dimensional Array Algorithm
Given two numbers for rows and columns, create a two-dimensional array of the provided sizes and populate each element with the product of each element's indices. For any perfectly square two-dimensional array that has an odd number of rows, set the center element to 1.

#### Example 1
The `buildMatrix` function is given 5 rows and 6 columns. So, it creates a 5 X 6 two-dimensional array (using a list of lists) and populates each element with the product of its indices. The two-dimensional array contains the following rows.

```text
[0, 0, 0,  0,  0,  0]
[0, 1, 2,  3,  4,  5]
[0, 2, 4,  6,  8, 10]
[0, 3, 6,  9, 12, 15]
[0, 4, 8, 12, 16, 20]
```

#### Example 2
The `buildMatrix` function is given 5 rows and 5 columns. So, it creates a 5 X 5 two-dimensional array and populates each element as explained in example 1 except the center element is set to 1. The two-dimensional array contains the following rows.

```text
[0, 0, 0,  0,  0]
[0, 1, 2,  3,  4]
[0, 2, `1`,  6,  8]
[0, 3, 6,  9, 12]
[0, 4, 8, 12, 16]
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
