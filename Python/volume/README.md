# Python: Volume
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0026: Utilize standard library modules.
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
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the `computeVolume` function that will compute the volume of a cuboid and a sphere and return the total 
volume of those items.

**PARAMETERS**
- `item1`: An integer that represents a radius of a sphere
- `item2`: a three item list of whole number containing a length, width, and height: represents a cuboid

**RETURN:** two variables, the volume of the sphere and the volume of the cuboid, or 'INVALID' if any parameter value 
is 0 or negative, or the list is not 3 items long

- Assume all values in the list are whole numbers.
- The function must be able to handle the parameters being passed in either order.
- make sure that one parameter is an integer and the other a list.
- make sure the list is exactly 3 in length.
- make sure all whole number are > 0.
- The formula for a sphere is 4/3 * PI * radius^3.
- The formula for a cuboid is length * width * height.
- Ensure you utilize the proper python modules for PI.
- After computing the volume of the sphere, round the result to a whole number.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
