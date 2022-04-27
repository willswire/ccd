# C Programming: Lo Shu Magic Square
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
Implement the function `isMagicSquare` that determines whether an array contains a Lo Shu Magic Square and returns a 
status code.

**PARAMETERS:**
1. `values`: a two-dimensional array of int

**RETURN:** an int of `1` if the array meets all the requirements of a magic square; otherwise, `0`

## Lo Shu Magic Square
The Lo Shu Magic Square is a grid with 3 rows and 3 columns like the example shown below:

```text
4 9 2
3 5 7
8 1 6
```

The Lo Shu Magic Square has the following properties:

1. The grid contains each of the numbers 1 through 9 exactly once.
2. The sum of each row, each column, and each diagonal all add up to the same number.
   - so, for the previous example, all rows, columns, and diagonals gives sum = 15

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
