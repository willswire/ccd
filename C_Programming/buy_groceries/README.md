# C Programming: Buy Groceries
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement a function `buyGroceries` that calculates the cost of a grocery shopping list and returns the rounded total 
cost.

**PARAMETERS:**
1. `stuff`: an array of int containing paired values representing an item number and quantity respectively
2. `size`: an int representing the number of elements in the `stuff` array

**RETURN:** an int containing the cost of the groceries rounded to the nearest dollar; or `0` for one of the 
conditions below

- Assume there will be no duplicate entries for an item number.
- Assume the array is of the given size if a valid even number is passed in.
- If the size passed for the array is not an even number > 0, the function should return 0.
- If the array is NULL, the function should return 0.
- If any item number is not a 1, 2, 3, or 4, the function should return 0.
- If any quantity is 0 or less, the function should return 0.

There are four valid items.

| item # | item | Cost |
| --- | --- | --- |
| 1   | eggs   | 3.50 |
| 2   | milk   | 2.25 |
| 3   | bread  | 1.99 |
| 4   | sugar  | 4.15 |

Consider the following array declaration.

`int cart[] = {1, 5, 2, 3, 4, 4};`

The `cart` array item/quantity pairs are as follows: 1/5, 2/3, and 4/4. So, item 1 (eggs) with a quantity of 5, item 2 
(milk) with a quantity of 3, and item 4 (sugar) with a quantity of 4. This would total to 40.85 with a rounded 
total of 41. The cost of each item is seen in the table above by referencing the item number. 

The `buyGroceries` function will iterate the array and determine the total cost of groceries as a floating point 
number based on the item number, quantity of each item, and cost of each item. If there is a quantity of 5 or more for 
an item, a 5% discount is applied on those items; so, the above example would have a 5% discount applied to the eggs, 
changing the total to 39.3975 rounded to 40.

Once the total is computed, use a math library function to round the value to an integer and return it.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.

