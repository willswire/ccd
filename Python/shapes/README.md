# KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.

# Tasks
Write a function `classify_shapes` that receives and processes a list of lists. Each list within the list contains 
three (3) numbers. The list represents the degree angles of a triangle.

Example  [[40,50,90],[60,70,80],[10,70,100]]

You are provided a dictionary with the following keys, whose values are all initialized to zero:

- `triRight`: represents a right triangle (having a 90 degree angle) - all angles added equal 180
- `triEquilateral`: represents a equilateral triangle (all angles are 60 degrees)
- `triOther`: any other triangle with all valid angles adding to 180 degrees.
- `triInvalid`: any 3 element list whose angles do not add up to 180
  - any angle less than or equal to zero (0)
  - any angle greater than or equal to 180

The function should process the list of lists, determining the type of triangle, and increment the associated value 
corresponding to the key in the dictionary. After processing the list, return the updated dictionary.

- If the overall list is empty or None, return the string `EMPTY_LIST`.
- If any of the lists inside the list are not 3 in length, return the string `INVALID_LIST`.
