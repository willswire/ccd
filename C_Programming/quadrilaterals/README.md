# C Programming: Quadrilaterals
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0034: Declare and implement appropriate data types for program requirements.
- S0035: Declare and/or implement of arrays and multi-dimensional arrays.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0050: Implement a function that doesn't return a value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0108: Utilize post and pre increment/decrement operators.
- S0082: Implement conditional control flow constructs.
- S0156: Utilize a struct composite data type.

## Tasks
Implement the function `classify_quads` that classifies quadrilaterals to specific shapes and saves the results in the 
output parameter `qds`.

**PARAMETERS:**
1. `quads`: a two-dimensional array of integers representing quadrilateral angles
2. `rows`: an int representing the number of rows
3. `qds`: a pointer to a `QuadStruct` struct (defined in TestCode.h) that receives the output data

**RETURN:** void

- The function should initialize all members of the `QuadStruct` structure to zero.
- Then, iterate through the two-dimensional array and process each row to determine the type of quadrilateral 
  represented in each row.
- Next, increment the appropriate variable inside the struct representing the type of quadrilateral. 
  - For example, if the angles represent a rectangle with all 90 degrees, the `rect` member will be incremented by 1.

### QuadStruct
Each row in the array represents the degree angles of a quadrilateral (four-side shape). Where indices 0 and 2 are 
opposite angles, and 1 and 3 are opposite angles as depicted in diagram below.

```text
        0___________________________________1
        /                                  /
       /                                  /
     3/__________________________________/2
```

A valid quadrilateral's angles add up to 360.

### Example
```text
{{90, 90, 90, 90},
 {160, 70, 30, 100},
 {110, 70, 10, 170}}
```

You are provided a `QuadStruct` struct, in `TestCode.h`, with the following integer variables:

- `rect`: represents a rectangle (having all 90 degree angles) 
- `para`: represents a parallelogram where both opposite angles are equal and is not a rect.
- `quad`: represents a valid quadrilateral that's not a rect or para
- `invalid`:
  - any row whose angles do not add up to 360
  - any angle less than or equal to zero (0)
  - any angle greater than or equal to 360

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
