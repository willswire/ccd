# Python: Recursion
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0049: Implement a recursive function.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Sort an unsorted list and then use recursion to find a value in the sorted list.

### Task 1
Implement the function `createOrderedList` that sorts a list into a new list.

**PARAMETERS**
1. `uList`: a list that needs to be placed in sorted order

**RETURN:** a newly created version of the list sorted in ascending order or an empty list if `uList` is empty

- Assume there are no duplicate values in `uList`.
- The list must be sorted in ascending order.
- **DO NOT** use the sort function to sort the list.
- The list should be sorted as it's being built; that is, each item's place should be determined when it is the next 
  item in `uList`.

### Task 2
Implement the recursive function `binarySearch` that is used to find a value in a sorted list.

**PARAMETERS**
1. `lst`: an ordered list of integers
2. `start`: the starting index of the list
3. `end`: the last index of the list
4. `val`: a value to search for in the list

**RETURN:** the index of the list where the value was located, `-1` if the value was not found, or `-2` if `lst` is 
empty

- Assume there are no duplicate values in `lst`.
- The function must use a recursive binary search algorithm to find the value in the list.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
