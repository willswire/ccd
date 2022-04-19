# Python: Count Time
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0037: Open and close an existing file.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0038: Read, parse, write (append, insert, modify) file data.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0080: Demonstrate the skill to implement exception handling.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0110: Implement error handling.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `find_culprits` that reads a log file and finds the 5 users with the most idle time. The file contains a list of user ids and number of minutes their login session has been idle. The top five users are stored in a list of lists with each inner list containing a user id and number of mins, as an integer, in that order.

**PARAMETERS:**
1. `fileName`: A string with the name of the log file to read

**RETURN:** A list of lists containing the 5 users with the most idle time in descending order, or `None` if the file 
cannot be opened

- Write no more than the top five users to the list.
- If there is a tie between values, any order between the ties is valid.
- The file can contain multiple session entries of the same user id.
- For this exercise all data in the file has valid format/content.
- The format of the file is: userid, mins.

Example:

```text
jschmo, 22
haaron, 12
haaron, 7
jschmo, 17
```

### Example
`[["jschmo",39],["haaron",19], ["jdoe", 17], ["ljenkins", 10], ["tbell", 7]]`

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
