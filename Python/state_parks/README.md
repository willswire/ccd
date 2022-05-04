# KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0080: Demonstrate the skill to implement exception handling.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0110: Implement error handling.
- S0082: Implement conditional control flow constructs.

# Tasks
Write a function `find_parks` that takes a list of dictionaries and a string that represents a state name. The state 
name may or may not be capitalized but should match regardless. The list contains a collection of dictionaries that 
represent state parks. The dictionaries each contain a state name, park name, and cost of camping at the park. The 
dictionary's keys are `state`, `park`, and `cost`. 

**Example:**
```python
[
    {"state":"Texas", "park":"Guadalupe", "cost": 12.50},
    {"state":"Michigan", "park":"Sterling", "cost": 8.50},
    {"state":"Texas", "park":"Pedernales", "cost": 13.50}
]
```

The state name may or may not be capitalized but should match regardless when compared to the state name being 
searched. The function should iterate through the list of dictionaries and find all parks that reside in the state 
name passed to the function and has a cost of less than 15 dollars. If a match is found, store the park name as a 
string in a python set. If the list or state name passed to the function is empty or None, return `INVALID_DATA`.

The minimum cost for a state park is $8. For any park listed with a cost lower than 8, the function should return 
`INVALID_DATA`. If any key errors are encountered with the dictionary, the function should return the string 
`KEY_ERROR`. The function will return the set when the list is successfully iterated; return an empty set if no parks 
are found.
