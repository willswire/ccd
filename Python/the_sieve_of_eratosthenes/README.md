# Python: The Sieve of Eratosthenes
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0026: Utilize standard library modules.
- S0024: Declare and/or implement container data type.
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs."
  
## Tasks
Implement the `sieve_of_Eratosthenes` function and use it to find the prime numbers from 0 and 999 inclusive.

**PARAMETERS:**
- This function does not take in any parameters

**RETURN:** A list of all prime numbers from 0 to 999 inclusive

## Sieve of Eratosthenes
The Sieve of Eratosthenes is a method of finding prime numbers. A prime integer is any integer greater than 1 that is 
evenly divisible only by itself and 1. The algorithm operates as follows:

1. Create a list with all elements initialized to 1. 

2. Starting with index 2, every time an index is found whose element's value is 1 (which indicates the index is 
prime), loop through the remainder of the list and set every element whose list index is a multiple of the prime index 
to 0 (which indicates an index is _not_ prime). For example:

   - **List index 2:** all elements after 2, which is a prime number, in the list that have an index that is a 
     multiple of 2 will be set to zero (indices 4, 6, 8, 10, etc.)

   - **List index 3**: all elements after 3, which is a prime number, in the list that have an index that is a 
     multiple of 3 will be set to zero (indices 6, 9, 12, 15, etc.) 
    
   - **List index 4:** List index 4 will have a value of 0 (because it was a multiple of 2), so no values will be 
     changed.

   - and so on.

3. When this process is complete, the list elements that are still set to 1 indicate that the subscript is a prime 
   number. All other list elements will be set to zero.


## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
