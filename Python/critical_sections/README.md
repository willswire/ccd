# Python: Critical Sections
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- A0564: Multi-threading
- S0382: Create a class constructor or destructor
- S0026: Utilize standard library modules.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).

## Tasks
Write a multi-threaded program that demonstrates ***RLock***. 

### Task 1
Implement the class `AddThread` that increments the global `number` variable, sleeps for a random time, and then 
increments again.

**METHODS:**
1. `__init__`: set up the thread and lock
2. `run`: this function will be called automatically and increment `number` as stated above

- Sleep from between 1 to 3 seconds.
- Protect the `number` with a lock.
- After the thread terminates, print the final value of the shared variable.

### Task 2
Implement the class `MultiplyThread` that doubles the global `number` variable, sleeps for a random time and doubles 
the `number` variable again. 

**METHODS:**
1. `__init__`: set up the tread and lock
2. `run`: this function will be called automatically and double `number` as stated above

- Sleep from between 1 to 3 seconds.
- Protect `number` with a lock.
- After the thread terminates, print the final value of the shared variable.

## NOTE
THE SOLUTION FOR THIS PROBLEM IS BASED ON A SPECIFICALLY DEFINED ALGORITHM. ALTHOUGH THE AUTOMATED TESTS MAY BE 
SUCCESSFUL, YOUR SOLUTION WILL RECEIVE A MANUAL REVIEW FOR FINAL DETERMINATION OF PASS/FAIL.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
