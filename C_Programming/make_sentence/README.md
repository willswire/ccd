# C Programming: Make Sentence
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0053: Implement a function that returns a memory reference.
- S0048: Implement a function that receives input parameters.
- S0090: Allocate memory on the heap (malloc).
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the function `makeSentence` that splits up a long string of letters into words and returns a new string with the 
words separated.

**PARAMETERS:**
1. `str`: An array of char pointers that contain no spaces

**RETURN:** A new char pointer with spaces in between each word with only the first word capitalized

- Capital letters in the string of characters represents a start of a word.
- The string returned should be a newly allocated array. 
- The string will represent a sentence and therefore needs to end with a period.
- If the first word of the sentence begins with the words Who, What, Where, When, Why, or How the sentence should end 
  with a question mark.
- Assume that the provided string contains no spaces.

### Example
```text
ILikeCheese   should result in:  I like cheese.
WhereAreYou   should result in:  Where are you?
```

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
