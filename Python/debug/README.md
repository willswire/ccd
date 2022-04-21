# Python: Debug
## KSAT List
- A0018: Analyze a problem to formulate a software solution.
- A0019: Integrate functionality between multiple software components.
- S0017: Debug a python script.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.

## Tasks
Debug the function `computeGPA` and remove all the errors (i.e. syntax, logic, etc.) so it executes properly.

**PARAMETERS:**
1. `scoreList`: a list of test scores

**RETURN:** Two values (the average GPA rounded to two decimal positions and the final grade) or a single value as 
described below

1. Compute a GPA for each test.
2. Throw out the two lowest GPAs.
3. Find the overall average GPA for all the GPAs.
4. Then, based on the overall GPA average, compute a final grade.
5. If any score in the list is less than 0 or greater than 100, the function returns a single value of "INVALID SCORE".

A school converts each test score grade to a GPA using the scale below. When the term is over they compute the average 
of all GPAs to determine an overall GPA and grade for the course.

| Grade  | Score   | GPA  |
| ---    | ---     | ---  |
| A      | 93-100  | 4    |
| A-     | 90-92   | 3.7  |
| B+     | 87-89   | 3.3  |
| B      | 83-86   | 3    |
| B-     | 80-82   | 2.7  |
| C+     | 77-79   | 2.3  |
| C      | 73-76   | 2    |
| C-     | 70-72   | 1.7  |
| D+     | 67-69   | 1.3  |
| D      | 65-66   | 1    |
| F      | < 65    | 0    |

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
