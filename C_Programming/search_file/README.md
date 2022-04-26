# KSAT List
This question is intended to evaluate the following topics:
- A0179: Implement file management operations.
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0042: Open and close an existing file.
- S0046: Determine location of content within a file.
- S0045: Determine the size of a file.
- S0043: Read, parse, write (append, insert, modify) file data.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0079: Validate expected input.
- S0097: Create and use pointers.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

# Tasks
Implement the function `searchFile` that counts the number of times a substring appears in a file and returns the 
determined count.

**PARAMETERS:**
1. `fname`: A char pointer representing a file name of a file to read
2. `str`: A char pointer representing a string to search for in the file

**RETURN:** An int that contains the number of times `str` appears in the file; `-1` if the file size is <= 150; `-2` 
if the file in `fname` does not exist, is NULL, or empty; or `-3` if the string in `str` is NULL or empty

- If the file size in bytes is > 150, the function will read through the file `fname` and find all occurrences of the 
  string in `str`. 

## Note
For this problem to work, the current directory should remain the folder with the text files (i.e. the root of the 
question's directory).

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
