# Python: Queue
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
- S0058: Create and destroy a Queue.
- S0071: Enqueue and dequeue a Queue.
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement a simple queue class using a list. 

### Task 1
Create a default constructor for the `queue` class.

**Attributes:**
1. `qList`: list representing the queue

- Each node in the queue contains an integer.

### Task 2
Implement the function `enqueue` that adds all elements in a list to the queue.

**PARAMETERS:**
1. `items`: a list of items to add into the queue

**RETURN:** `None`

- All items in the list need to be added to the end of the queue, in the order they appear in `items`.
- The function should iterate the list and add each number on to the queue as it's iterated.

### Task 3
Implement the function `dequeue` that removes a specified number of items from the front of the queue.

**PARAMETERS**
1. `numRemove`: the amount of items to remove from the front of the queue

**RETURN:** `None`

- If the integer passed is greater than the number of items in the queue, the function will not modify the queue.

### Task 4
Implement the function `emptyQueue` that removes all items in the queue.

**PARAMETERS**
- This function takes no parameters

**RETURN:** `None`

### Task 5
Implement the function `peek` that returns the front value in the queue without modifying the queue.

**PARAMETERS**
- This function takes no parameters

**RETURN:** the first object in the queue or `None` if the queue is empty
      
### Task 6
Implement the function `isEmpty` that checks if the queue is empty.

**PARAMETERS**
- This function takes no parameters

**RETURN** `True` if the queue has no elements or `False` if at least one element is in the queue

### Task 7
Implement the `size` function that returns the size of the queue.

**PARAMETERS**
- This function takes no parameters

**RETURN:** the number of items in the queue or `0` if the queue is empty

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
