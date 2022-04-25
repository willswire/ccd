# C Programming: Write Names To File
## KSAT List
This question is intended to evaluate the following topics:
- A0179: Implement file management operations.
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0042: Open and close an existing file.
- S0043: Read, parse, write (append, insert, modify) file data.
- S0044: Create and delete file.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0077: Add and remove items from a Hash Table.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the function `writeNames` that writes a series of names to a file and returns a status code.

**PARAMETERS:**
1. `fnames`: A const char pointer to an array that contains people's first names
2. `lnames`: A const char pointer to an array that contains people's last names
3. `sz`: An int containing the size of both arrays 
4. `fileName`: A const char pointer representing the name of the file to write data to

**RETURN:** An int containing 1 on success; return 0 if `sz` is 0 or less, the length of any of the names are 0, or 
any of the pointer input parameters are NULL

- Assume that both arrays will be the same length.
- Process the arrays and write each person's last name and first name to the file name passed.
- Each line of the file should contain a person's last name, followed by a comma and a space, then the first name.
- The first names and last names align to the same index in each array.
  - For example, a person's first name will be in `fnames[0]` and their last name in `lnames[0]`. 
- Ensure when you write the names out to the files, the first letter of each name is capitalized like the example below.
- Ensure that the last line of the file does NOT contain a newline char (\n) at the end.

### Example

```text
Smith, John\n
Jones, Sally\n
Adams, Becky(EOF)
```

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
