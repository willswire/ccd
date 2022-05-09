# C Programming: Format Phone Numbers
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0053: Implement a function that returns a memory reference.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0110: Implement error handling.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the function `formatNums` that reads a series of numbers, formats them into phone numbers, and returns a 
formatted phone number.

**PARAMETERS:**
1. `nums`: a pointer to a a 10-element array of character pointers containing strings of numbers

**RETURN:** a pointer to an array of character pointers containing the formatted phone numbers or NULL if a provided 
number does not have exactly 10 digits.

- Each element in the array passed contains a string of characters representing a phone number.
- Each received phone number may be in formats such as: 
  - `999-999-9999`
  - `9999999999`
  - `(999) 9999999`
  - `999,999,9999`
  - or any other format. The important thing is that each provided string should have 10 digits and only 10 digits.
- The proper output format required is: `(999) 999-9999`.
- The function should create a new 10-element array of char * and convert each provided phone number to the proper 
  format and place in the new array.
- If any provided phone number contains more or less than 10 digits, the function should free up allocated memory 
  before returning NULL.

### Example
```text
Input: { "(210)3157904","2103157904","1031376904","(210) 3157904",
         "7210313704","210-315-7904","210 315 7904","(210) 315-7904",
         "8888675309","2103157904" }

Proper return: { "(210) 315-7904","(210) 315-7904","(103) 137-6904","(210) 315-7904",
                 "(721) 031-3704","(210) 315-7904","(210) 315-7904","(210) 315-7904",
                 "(888) 867-5309","(210) 315-7904" }
```
## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
