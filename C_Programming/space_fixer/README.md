# C Programming: Space Fixer
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0031: Utilize logical operators to formulate boolean expressions.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0053: Implement a function that returns a memory reference.
- S0048: Implement a function that receives input parameters.
- S0079: Validate expected input.
- S0090: Allocate memory on the heap (malloc).
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0110: Implement error handling.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement a function `spaceFixer` that builds a new paragraph, ensuring there are exactly two (2) spaces after each period or question mark, and returns the correctly formatted paragraph.

**PARAMETERS:**
- `text` a constant char pointer representing a paragraph with invalid spacing between sentences

**RETURN:** a char pointer to the newly formatted paragraph or `null` if `text` is empty or null

- Assume all paragraphs are no more than 200 characters.
- Assume there are no leading spaces before the paragraph's starting word.
- Assume each sentence ends in a period or question mark.
- There could be zero to many spaces between sentences.
- The last period/question mark in the paragraph should not have spaces after it.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
