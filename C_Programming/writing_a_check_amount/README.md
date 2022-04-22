# C Programming: Writing a Check Amount
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0053: Implement a function that returns a memory reference.
- S0048: Implement a function that receives input parameters.
- S0090: Allocate memory on the heap (malloc).
- S0097: Create and use pointers.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the `checkAmount` function that writes the word equivalent of a numeric check amount (with values up to 
$99.99) to a string that is returned.

**PARAMETERS:**
1. `amount`: a double containing the numeric amount of the check

**RETURN:** A char pointer to a string containing the word equivalent of `amount` or `NULL` if the check amount is <= 0 
or >= 100

- Dynamically allocate the string that is returned.

### Example
For example, the amount 52.43 should be written as FIFTY TWO and 43/100. The amount 0.52 should be written as 
ZERO and 52/100.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
