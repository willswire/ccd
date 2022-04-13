# Python: 3 Card Guts
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
Implement the function `findGutsWinner` to determine which of two guts poker hands is the highest and return the list 
determined to be the winner (the highest hand).

**PARAMETERS:**
1. `hand1`: a list of numbers representing a players hand
2. `hand2`: a list of numbers representing a players hand

**RETURN:** the list determined to be the winner, or an empty list if any list has more or less than three elements

- Assume there are only two players in the game.
- Assume no two players will ever have the same pair or triplet (if there is a pair or triplet). 
- Assume no two players will ever have the same high card.
- Assume the numbers in the list are valid card numbers.
- Valid card numbers range from 2 - 14: 14 is the Ace, 13 is the king, etc.

## The Poker Game of Guts
In the poker game of guts, the highest card is an Ace and lowest is a 2. In guts, each player is given three cards and 
goes head to head with their opponents; the highest hand wins. The ranking of hands is in this order:

1. Highest three of a kind (if any)          Winner: 6,6,6        Not winner: 5,5,5
2. Highest two of a kind (if any)            Winner: 7,7,5        Not winner: 5,5,6
3. High card (person with highest card)      Winner: 11,7,5       Not winner: 10,4,2

### Example:
Given two players with the following guts poker hands:
- Player 1: [14,2,7]
- Player 2: [3,3,14]

Player 2 is the winner because the hand has a two of a kind, compared to Player 1's hand of three different cards.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
