# Python: Names To File
## KSAT List
This question is intended to evaluate the following topics:
- A0047: Implement file management operations.
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0037: Open and close an existing file.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0038: Read, parse, write (append, insert, modify) file data.
- S0039: Create and delete a file.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `create_file` to read a list of names, sort the names alphabetically by last name and write the 
names to a file. When the function is finished, it returns a status code.

**PARAMETERS:**
1. `names`: A list of names where each name is another list with elements for the first and last names

**RETURN:** A string containing: `SUCCESS` on success, `EMPTY_LIST` if `names` is an empty list, or `INVALID_NAME` if 
any of the list items in `names` have more or less than two items or have empty strings.

- Each list within the list has two strings representing a first and last name. 
- Each last name will be unique, you will not have to worry about two of the same last names. 
- Sort the names in alphabetical order by last name.
- Write the names to a file called `names.txt` in the format of Last, First with each name on a separate line.
- When writing to a file, ensure both first and last names are capitalized.

### **Example:**
```
[
    ["John","Hancock"], 
    ["George","Washington"]
]
```

`names.txt`:
```text
Hancock, John
Washington, George
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
