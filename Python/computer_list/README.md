# Python: Computer List
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
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0048: Implement a function that receives input parameters.
- S0080: Demonstrate the skill to implement exception handling.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Write the function `create_computer_objects` that will read data from a file to create one or more computer objects 
and store one or more of these objects in a list. 

**PARAMETERS:**
1. `filename`: a string of the name of the file to read

**RETURN:** a list of Computer objects

- You will need to add an import statement in your code for the unit tests to work.
- Each valid object will be stored in the list in the order the data is read from the file. 
- The Computer class used to create the objects is defined in the `supportClass.py` file. 
- Objects should be created with cost as a float, and ramGB/storageGB as an integer.
- If the file cannot be opened, raise a file not found error with the message `"FILE CORRUPTED"`.
- Raise a value error with the message `"INVALID DATA"` if:
  - any of the cost, ram, or storage are invalid numbers, or
  - any line in the file contains less or more than the five required items.

### Format
Each line in the file will be in the format of: 
- brand, model, cost, ram, storage. 

Note: there will never be a comma in the brand or model name itself
**Example:**
- Lenovo, Super Duper, 795.95, 16, 512. 
 
Only the following computers should have objects created and stored in the list:
- all brands except "Asus" and cost within $500 - $1000 (exclusive)
- 8 or more GB of ram.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
