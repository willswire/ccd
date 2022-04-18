# Python: Change for Snacks
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0047: Implement a function that returns multiple values.
- S0048: Implement a function that receives input parameters.
- S0082: Implement conditional control flow constructs.

## Tasks
Implement the function `computeChange` to compute the total amount of change and determine whether or not there is 
enough money to purchase items at a fast-food restaurant. When finished, `computeChange` returns the result as 
indicated below.

**PARAMETERS:**
1. `change`: a dict containing the following keys, where each value is an int of quantities of coins
   - `H` for a half dollar
   - `Q` for a quarter
   - `D` for a dime
   - `N` for a nickel
   - `P` for a penny

**RETURN:** a float, with two decimal places, containing the total and then a str indicating what can be purchased; or 
`0` if any given quantity is less than zero

### Fast-food Menu
The fast-food restaurant has the following items for sale. Sorry, but they're all out of other items due to product 
shortages.

| Item  | Cost  |
| ----  | ----  |
| Fries | $1.50 |
| Soda  | $1.00 |

When determining what can be purchased, `computeChange` should return one of the following strings.
- `BOTH` if there's enough to buy both items
- `FRIES` if there's enough to buy fries
- `SODA` if there's enough to buy soda
- `NOTHING` if there's not enough to buy anything

### Example
The function `computeChange` receives the dictionary `{'Q':3, 'D':7, 'P':14}` (3 quarters, 7 dimes, 14 pennies) so it 
returns `1.59` and the string `"FRIES"` respectively.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
