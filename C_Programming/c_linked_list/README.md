# C Programming: C Linked List
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0066: Add and remove nodes from a Linked List.
- S0065: Find an item in a Linked List.
- S0055: Create and destroy a Linked List.
- S0053: Implement a function that returns a memory reference.
- S0048: Implement a function that receives input parameters.
- S0090: Allocate memory on the heap (malloc).
- S0097: Create and use pointers.
- S0091: Unallocating memory from the heap (free).
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0156: Utilize a struct composite data type.
- S0160: Utilize the standard library.

## Tasks
These tasks allow you to create and work with a linked list.

### Task 1
Implement the function `processNames` that creates a linked list of names using the `nameNode` struct defined in 
`TestCode.h` and returns the head of the list.

**Parameters:**
1. `names`: a pointer to a 10 element array of strings (char *)

**Return:** struct `nameNode` pointer to the head node of the linked list, or `null` if `names` is null or contains null 
elements

- The array contains a list of peoples' first names.
- Iterate the array and insert the names into nodes so they are in ascending (alphabetical) order in the linked list.
- Empty strings should be ignored.

### Task 2
Implement the function `freeMemory` that safely deletes a linked list.

**Parameters:**
1. `head`: a pointer to the first node in the linked list to be deleted

**Return:** void

- iterate over the linked list and free all allocated memory.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
