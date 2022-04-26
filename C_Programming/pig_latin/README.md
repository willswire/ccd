# C Programming: Pig Latin
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0034: Declare and implement appropriate data types for program requirements.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0036: Declare and implement a char * array (string).
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0053: Implement a function that returns a memory reference.
- S0090: Allocate memory on the heap (malloc).
- S0097: Create and use pointers.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0160: Utilize the standard library.

## Tasks
Implement the function `encodePigLatinPhrase` that encodes English-language phrases into pig Latin. 

**PARAMETERS:**
1. `englishPhrase`: A char pointer to a string containing a normal english phrase

**RETURN:** A char pointer to a string containing the pig latin version of the provided english phrase

- Assume that the English phrase consists of words separated by blanks, there are no punctuation marks, and all words 
  have two or more letters.
- If the English phrase is just white space(s), the pig latin phrase is the empty string `""`.
- The pig latin phrase is of max length of 80 characters.

## Pig Latin
Pig Latin is a form of coded language often used for amusement. Many variations exist in the methods used to form 
pig-Latin phrases. For simplicity, use the following algorithm:

- To form a pig-Latin phrase from an English-language phrase:
  1. fragment the phrase into words.
  2. To translate each English word into a pig-Latin word, place the first letter of the English word at the end of the 
     English word and add the letters `ay`.

Thus the word `jump` becomes `umpjay`, the word `the` becomes `hetay` and the word `computer` becomes `omputercay`. 
Blanks between words remain as blanks.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
