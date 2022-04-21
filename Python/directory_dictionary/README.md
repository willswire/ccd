# Python: Directory Dictionary
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0026: Utilize standard library modules.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0037: Open and close an existing file.
- S0038: Read, parse, write (append, insert, modify) file data.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `dir_reader` to read all files in a directory and store the paths in a dictionary. When the 
function is finished, it returns the resulting dictionary object.

**PARAMETERS:**
1. `dir_path`: A string object containing the path of the directory in which to read files

**RETURN:** A dictionary containing the paths of each file as keys and their contents as values

- Add each file in the directory that ends with `.txt` to the dictionary.
- Use the file's path as the key. 
- Read the file and add the contents of the file as the value.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
