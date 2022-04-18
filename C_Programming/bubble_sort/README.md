# C Programming Bubble Sort
## KSAT List
This question is intended to evaluate the following topics:
- A0087: Create and implement a sort routine.
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0098: Implement a function pointer to call another function.

## Tasks
Implement two compare functions, named `ascending` and `descending`, that determine if two values should be swapped. 
Then, implement a function `bubbleSort` that implements the Bubble Sort algorithm and uses the `ascending` and 
`descending` functions for sorting.

### Task 1

The function `ascending` takes in the two parameters below and returns 1 for true or 0 for false. The function should 
return true if `a` is bigger than `b`.

**PARAMETERS:**
1. `a`: an int to be compared
2. `b`: an int to be compared

**RETURN:** an int with the value 1 if the first parameter is larger than the second and 0 otherwise

### Task 2

The function `descending` takes in two parameters and returns 1 for true or 0 for false. The function should return 
true if `a` is smaller than `b`.

**PARAMETERS:**
1. `a`: an int to be compared
2. `b`: an int to be compared

**RETURN:** an int with the value 1 if the first parameter is smaller than the second and 0 otherwise

### Task 3
The function `bubbleSort` takes in three parameters and returns a pointer to the sorted array.

**PARAMETERS:**
1. `elements`: an array of int to be sorted
2. `length`: a size_t representing the number of items in the `elements` array
3. `compare`: a pointer to a function, with two int input parameters, that returns an int

**RETURN:** int pointer to the sorted array

**NOTE: THE SOLUTION FOR THIS PROBLEM IS BASED ON A SPECIFICALLY DEFINED ALGORITHM EXPLAINED BELOW. ALTHOUGH THE**
**AUTOMATED TESTS MAY BE SUCCESSFUL, YOUR SOLUTION WILL RECEIVE A MANUAL REVIEW FOR FINAL DETERMINATION OF PASS/FAIL**

## Bubble Sort Algorithm
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in 
the wrong order.

**Example:**
```text
First Pass:
( `5` `1` 4 2 8 ) -> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 `5` `4` 2 8 ) ->  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 `5` `2` 8 ) ->  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 `5` `8` ) -> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( `1` `4` 2 5 8 ) -> ( 1 4 2 5 8 ), No swap since 1 < 4
( 1 `4` `2` 5 8 ) -> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 `4` `5` 8 ) -> ( 1 2 4 5 8 ), No swap since 4 < 5
( 1 2 4 `5` `8` ) ->  ( 1 2 4 5 8 ), No swap since 5 < 8

Third Pass:
( `1` `2` 4 5 8 ) -> ( 1 2 4 5 8 )
( 1 `2` `4` 5 8 ) -> ( 1 2 4 5 8 )
( 1 2 `4` `5` 8 ) -> ( 1 2 4 5 8 )
( 1 2 4 `5` `8` ) -> ( 1 2 4 5 8 ), When no swapping occurs, sorting is finished
```

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.

