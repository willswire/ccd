# C Programming: C Command Line
## KSAT List
This question is intended to evaluate the following topics:
- S0109: Implement a program that uses standard main() command line arguments.
- A0179: Implement file management operations.
- S0042: Open and close an existing file.
- S0044: Create and delete file.
- T0009: (U) Analyze, modify, develop, debug and document software and applications in C programming language.
- A0061: Create and implement functions to meet a requirement.
- S0081: Implement a looping construct.

## Tasks
Create a program that takes command line arguments and writes them to a file.

### Task 1
Create a function `fileDump` that writes words to a specific file and returns a status code.

**Parameters:**
1. `fname`: const char * that is the name of the file to write to
2. `words`: const char * array that contains the collection of words to write
3. `wordLen`: int that contains how many words are in the `words` array

**Return:** int containing: `1` for success, or `0` if `fname` or `words` are null

- `fileDump` will write the words to the specified file.
- If the words array is empty the file should still be created. 
- The words will be written to the file on separate lines, separated by a newline 

**Example:**

```
word1
word2
word3
```

etc.

### Task 2
The program `TestCode` will accept a list of words and write them to a file called `text.txt`. 
Implement an option, -f and --filename, which uses the next word as the file name that the words are written to.

- All words other than the program, option, and the following filename should be treated as words to write into the output file. 
- If the -f or --filename option is provided but does not contain a file name, use the default `text.txt` file name. 

**Example:**

Example 1
```text
TestCode -f examplefile.txt word1 word2 word3
```
output:

`examplefile.txt`
```
word1
word2
word3
```

Example 2

```text
TestCode word1 word2 --filename examplefile word3
```
output:

`examplefile`
```
word1
word2
word3
```

Example 3
```text
Testcode word1 word2 word3
```
output:

`text.txt`
```
word1
word2
word3
```

Example 4
```text
Testcode word1 word2 word3 -f
```
output:

`text.txt`
```
word1
word2
word3
```

### Unit Testing
The first series of unit tests checks the `fileDump` function to see if it operates as expected. These tests will 
allow you to step through your code and debug as you do in other questions. After the `fileDump` tests are complete, a 
series of `command-line` tests run using the compiled binary in a separate process. This separate process is passed 
input parameters as if someone were running it manually. Since the tests are run in a separate process, you will not 
be able to step through your code in `TestCode.c` when these unit test run; however, you can place breakpoints in 
`testcases.cpp`.

If you need to step through your main function for debugging purposes, you can do so on the first run of `main`, 
before `do_test` is called. If you want to pass input parameters to the first run of `main` for testing purposes, 
update the `.vscode/launch.json` file as follows. Be sure to restore `launch.json` to its original settings before 
moving on to another question.

- Look for the configuration named `Test C`
- Change the `Test C` input parameters by adding comma separated strings to the `args` attribute. Note, each space 
  separated parameter should be its own string.
  - Example 1
    ```json
    {
        "version": "0.1.0",
        "configurations": [
            {
                "name": "Test C",
                ...
                "args": ["-f", "somefile.txt", "word1", "word2"],
                ...
            },
            ...
        ]
    }
    ```
  - Example 2
    ```json
    {
        "version": "0.1.0",
        "configurations": [
            {
                "name": "Test C",
                ...
                "args": ["word1", "word2", "word3"],
                ...
            },
            ...
        ]
    }
    ```
  - Example 3
    ```json
    {
        "version": "0.1.0",
        "configurations": [
            {
                "name": "Test C",
                ...
                "args": ["word1", "-f", "anotherfile", "word2"],
                ...
            },
            ...
        ]
    }
    ```

#### NOTE
When you are done with this question, remove all strings from the `args` attribute. If this is not done then your 
other questions may not work properly. So the `args` line (should be around line 9) of `launch.json`, in the `Test C` 
configuration, should read `"args": [],`.

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
