# Python: Linked List
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- A0561: Demonstrate the ability to create, reuse and import modules
- S0382: Create a class constructor or destructor
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0066: Add and remove nodes from a Linked List.
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.
- S0055: Create and destroy a Linked List.

## Tasks
Implement a `SingleList` class that inserts and removes names to a singly linked list.

Note: You will only need to implement the create portion of KSAT S0055 for this question.

### Task 1
Implement the constructor for the `SingleList` class that initializes the linked list with names from an 
optional list of names.

**PARAMETERS:**
1. `namelist`: An optional list of names to create the list with

**ATTRIBUTES:**
1. `head`: The first node of the list
2. `tail`: The last node of the list

- If a list of names is provided, the resulting linked list should have the names in the same order.
- Create an empty linked list if no name list is provided.
- If the list is empty the `head` and `tail` should be None.

### Task 2
Implement the `insert` function that will insert a name to the end of the list with the ability to insert it to a 
specific location in the list.

**PARAMETERS:**
1. `name`: A string with the name to insert to the list
2. `position`: An optional integer with the position to add the name before

- If no position is specified then add the name to the end of the list
- If a position is specified then add the name before the node at that position with the first item being position 0

### Task 3
Implement the `remove` function that will remove a name from the linked list.

**PARAMETERS:**
1. `name`: A string with the name to remove from the list

**RETURN:** A string with the name removed from the list or None if it was not found

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
