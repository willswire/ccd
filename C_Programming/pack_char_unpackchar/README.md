# C Programming: Pack Character and Unpack Character
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0030: Utilize bitwise operators to manipulate binary values.
- S0034: Declare and implement appropriate data types for program requirements.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0053: Implement a function that returns a memory reference.
- S0048: Implement a function that receives input parameters.
- S0090: Allocate memory on the heap (malloc).
- S0097: Create and use pointers.
- S0160: Utilize the standard library.

## Tasks
### Task 1
Implement the function `packCharacters` that packs four character values into a four-byte unsigned integer variable and 
returns the packed integer. 

**PARAMETERS:**
1. `ch4`: A char that contains the leftmost byte
2. `ch3`: A char that contains the second leftmost byte
3. `ch2`: A char that contains the second rightmost byte
4. `ch1`: A char that contains the rightmost byte

**RETURN:** An int containing all 4 bytes packed together

- The first character will be placed in the first byte of the int variable.
- The second character will be in the second byte.
- The third character will be in the third byte.
- The fourth character will be in the fourth byte. 

### Example
For ch4=a, ch3=b, ch2=c, and ch1=d 

Returning int = abcd.

### Task 2
Implement the function `unpackCharacters` that unpacks characters from a four-byte unsigned int and returns the bytes 
in an array. 

**PARAMETERS:**
1. `pack` An int that contains the 4 bytes that need to be unpacked

**RETURN:** An array of char containing the individual bytes

### example
For int pack = abcd

Returning char * = {d,c,b,a}.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
