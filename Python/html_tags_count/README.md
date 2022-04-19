# Python: HTML Tag Count
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `HTML_count_tags` that receives a string containing HTML as input and outputs the the number of 
tags at each level. 

**PARAMETERS:**
1. `hString`: A string that may contain multiple HTML tag pairings

**RETURN:** A list with each index indicating the nesting level of a tag and the value at that index indicating the 
number of tags in that level

- Assume that `hString` is not empty.
- Each opening tag will have an equivalent ending tag.

### Example
The HTML `<p><strong>hi</strong> <small> this is a test </small></p>` has a `<p>` tag at level 0, 
a `<strong>` tag at level 1, and a `<small>` tag at level 1. That means we have 2 tags at level 1. So, the final 
output is a list containing [1, 2] (1 tag at level zero and two tags at level 1).

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).