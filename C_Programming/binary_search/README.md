# C Programming: Binary Search
## KSAT List
This question is intended to evaluate the following topics:
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `BSearch` that searches an array of integers, using a binary search algorithm, for a specified 
value and returns the position of the value found.

**PARAMETERS:**
1. `arr`: A sorted array of integers
2. `left`: an int representing the first index of the array that needs to be searched
3. `right`: an int representing the last index of the array that needs to be searched
4. `target`: an int representing the number to be searched

**RETURN:** an int that is the index of the search target in the given array, or -1 if target is not found

**NOTE: THE SOLUTION FOR THIS PROBLEM IS BASED ON A SPECIFICALLY DEFINED ALGORITHM EXPLAINED BELOW. ALTHOUGH THE**
**AUTOMATED TESTS MAY BE SUCCESSFUL, YOUR SOLUTION WILL RECEIVE A MANUAL REVIEW FOR FINAL DETERMINATION OF PASS/FAIL**

## Binary Search Algorithm
Binary Search: Search a ***sorted*** array by repeatedly dividing the search interval in half.

Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of 
the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the 
value is found or the interval is empty.

**Example:**

If searching for 23 in the 10- element array [2 5 8 12 16 23 38 56 72 91]:

1. Get the middle element, which is 16 (not our target)
2. Since 23 > 16, the new search will work on the right half of the array (i.e., 23 38 56 72 91)
3. Get the middle of the new working array, which is 56
4. Since 23 < 56, work on the left half of the array (i.e., 23 38)
5. Compute the middle, which is 23. The target found

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.

