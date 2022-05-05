# Python: Stack
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0382: Create a class constructor or destructor
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0078: Push and pop a Stack.
- S0062: Create and destroy a Stack.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement a simple stack class using a linked list and the `numNode` class defined in `testfile.py` to facilitate the 
creation of a stack. Each node in the stack should contain an integer.

### Task 1
Create a default constructor for the `stack` class.

**Attributes:**
1. `top`: a reference to the top of the stack
2. `size`: the number of items in the stack

### Task 2
Implement the function `pushStack` that adds a list of items to the stack.

**PARAMETERS**
1. `items`: a list of numbers to push on the stack

**RETURN:** `None`

- Each element in `items` must be added to the stack in Last In First Out order (LIFO).
- Increase the size counter for each element added.

### Task 3
Implement the function `popStack` that removes the topmost item from the stack and returns it.

**PARAMETERS**
1. `numPops`: the number of items to remove from the top of the stack

**RETURN:** A list of the items popped from the stack or `STACK TOO SMALL` if there are not enough items in the stack

- If `numPops` is greater than the number of items in the stack, the function will not modify the stack.
- The list that is returned must have the items in the order they were removed.
- Decrement the size of the stack for each item that is popped.

### Task 4
Implement the function `emptyStack` that removes all items in the stack.

**PARAMETERS**
- This function takes no parameters

**RETURN:** `None`

- `top` should be set to `None`
- `size` should be set to 0

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
