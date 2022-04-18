# Python: Class
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0382: Create a class constructor or destructor
- S0026: Utilize standard library modules.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0082: Implement conditional control flow constructs.

## Tasks
In this question, you will create a Python class that handles a game character's movement and health.

### Task 1
Create a class Player which represents a paladin character in a game.

**ATTRIBUTES:** 
- `name`: string representing Player's name - required
- `health`: float, number of health (starts at default 100.0)
- `x_pos`: float x position on a grid (starts at default 0.0)
- `y_pos`: float y position on a grid (starts at default 0.0)
        
### Task 2
Create a method called `report_pos` that returns the player's current X and Y position.

**PARAMETERS:**
1. This function does not take any parameters

**RETURN**: a tuple containing the object's current x and y position: `(x, y)`

### Task 3
Create the method `reduce_health` that subtracts health from the player.

**PARAMETERS:**
1. `dmg`: a floating point value with how many health to remove from the player's health

**RETURN**: None

- Only apply half of the damage amount to the player's health. This is because paladins are "tanky" (they have a defensive advantage).
- A player's minimum health is `0.0`. If the damage reduces health below 0.0, set health to 0.0.

### Task 4
Create the method `move` that updates the character's position by a distance and calculates any damage taken 
from falling.

**PARAMETERS:**
1. `x_pos`: a floating point value of how far the character moves horizontally
1. `y_pos`: a floating point value of how far the character moves vertically

**RETURN**: a float of the remaining health

- If the character falls a distance of 5 or more, they should take damage equal to the distance traveled. 
  - Consider negative y values as falling.
  - Compute the distance by getting the square root of (x_pos \* x_pos + y_pos \* y_pos).
  - Use the `reduce_health` method to apply the damage calculated.
- If the movement reduced the health to 0, output the string `You are out of health!` to the console.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
