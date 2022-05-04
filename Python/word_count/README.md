# Python: Word Count
## KSAT List
This question is intended to evaluate the following topics:
- S0033: Utilize assignment operators to update a variable.
- S0048: Implement a function that receives input parameters.
- S0110: Implement error handling.
- S0037: Open and close an existing file.
- S0038: Read, parse, write (append, insert, modify) file data.
- S0047: Implement a function that returns multiple values.
- S0080: Demonstrate the skill to implement exception handling.

## Tasks
Implement the function `word_count` that counts each of the words in a file and keeps track of how many times each word
appears. 

**PARAMETERS**
1. `fname`: A name of a file to count the words within

**RETURN:** Three values: a dictionary containing each word as a key and the number of times that word appears in the 
file; the word that appears the most; and the total number of words in the file

- Account for punctuation and whitespace e.g. `ipset` and `ipset.` would both count as the same word. 
- If a file contains no words, is empty, or can not be found then return None.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
