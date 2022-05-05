# Python: Rational Number
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- S0382: Create a class constructor or destructor
- S0023: Declare and implement data types.
- S0029: Utilize arithmetic operators (PEMDAS +, -, *, /, %) in mathematical equations.
- S0032: Utilize relational operators to formulate boolean expressions.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0110: Implement error handling.
- S0082: Implement conditional control flow constructs.

## Tasks
**Do not use a module instead of implementing the following features.**

Create a class called `RationalNumber` for performing arithmetic with fractions.

### Task 1
Implement a constructor function for the `RationalNumber`.

**PARAMETERS**
1. `top` The numerator of the rational number
2. `bottom` The denominator of the rational number

**ATTRIBUTES**
1. `numerator`: The top part of the rational number stored as an Int
2. `denominator`: The bottom part of the rational number stored as an Int

- If `bottom` is 0, raise a value error.
- Reduce the numerator and denominator to their simplest form (they share no factors other than 1).
  - The fraction 2/4 would be stored in the object as 1/2.
- If the function is not called with both parameters, `top` should default to 0 and `bottom` should default to 1.

### Task 2
Implement the class function `add` that adds another `RationalNumber` to this one and saves the result in a new 
`RationalNumber`.

**PARAMETERS**
1. `number`: The `RationalNumber` to add to this one

**RETURN:** A new `RationalNumber` that contains the result of adding both `RationalNumber` objects

- The result needs to be a new `RationalNumber` object.
- Ensure the result is in its reduced form.

### Task 3
Implement the class function `subtract` that subtracts another `RationalNumber` from this one and saves the result in a 
new `RationalNumber`.

**PARAMETERS**
1. `number`: The `RationalNumber` to subtract from this one

**RETURN:** A new `RationalNumber` that contains the result of subtracting both `RationalNumber` objects

- The result needs to be a new `RationalNumber` object.
- Ensure the result is in its reduced form.

### Task 4
Implement the class function `multiply` that multiplies another `RationalNumber` with this one and saves the result in 
a new `RationalNumber`.

**PARAMETERS**
1. `number`: The `RationalNumber` to multiply to this one

**RETURN:** A new `RationalNumber` that contains the result of multiplying both `RationalNumber` values

- The result needs to be a new `RationalNumber` object.
- Ensure the result is in its reduced form.

### Task 5
Implement the class function `divide` that divides the `RationalNumber` by another and saves the result in a new 
`RationalNumber`.

**PARAMETERS**
1. `number`: The `RationalNumber` to divide

**RETURN:** A new `RationalNumber` that contains the result of dividing both `RationalNumber` values

- The result needs to be a new `RationalNumber` object.
- Ensure the result is in its reduced form.

### Task 6
Implement the function `printFraction` that returns a text representation of the fraction.

**PARAMETERS** 
- This function takes no parameters

**RETURN:** a string representation of the fraction in the format `"a/b"` where `a` is the numerator and `b` is the 
denominator, i.e. "1/2" or "11/25".

### Task 7
Implement the function `printDecimal` that converts the Rational number to decimal format.

**PARAMETERS**
- This function takes no parameters

**RETURN:** the rational number as a floating point number rounded to 2 decimal places

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
