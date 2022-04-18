# C Programming: C Trie
## KSAT List
This question is intended to evaluate the following topics:
- S0059: Create and destroy a Tree.
- S0072: Find an item in a Tree.
- S0073: Add and remove nodes from a Tree.
- A0018: Analyze a problem to formulate a software solution.
- S0024: Declare and/or implement container data type.
- S0033: Utilize assignment operators to update a variable.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0052: Implement a function that returns a single value.
- S0048: Implement a function that receives input parameters.
- S0081: Implement a looping construct.
- S0082: Implement conditional control flow constructs.
- S0034: Declare and implement appropriate data types for program requirements.

## Tasks
Implement a tree, also known as trie, that contains words with the links between nodes being the individual characters 
in each word.
Note: this question only tests the add a node portion of the KSAT S0073. 

### Task 1
Implement a function `buildTree` that uses words in an array to create a trie and returns the root of the trie. The 
links between nodes are the individual characters in each word (see diagram below).

**PARAMETERS:**
1. `wordList`: a pointer to an array of words 
2. `length`: an int of the length of the array.

**RETURN:** `struct Node` pointer to the root of the trie

- Each node needs to indicate if it can be the end of a word in the tree by setting the `endOfWord` attribute in the 
  `Node` struct to `1`. 
- Uppercase and lowercase characters should be treated equally when adding words to the tree.
- Assume there are no numbers or whitespace or punctuation in the words.

### Task 2
Implement a function `addNode` that adds a word to the Trie.

**PARAMETERS:**
1. `root`: a `Node` pointer to the root of a trie 
2. `word`: a pointer to a character array of the word to add to the trie.

**RETURN:** void

- If the added word is contained entirely within another word then indicate that node as a potential end of word 
  by setting the `endOfWord` attribute to `1`.

### Task 3
Implement a function `findWord` that searches a trie for a word and returns a status code.

1. `root`: a `Node` pointer to the root of a trie
2. `word`: a pointer to a character array of the word to search for in the trie.

**RETURN:** an integer of: 1 - the word was in the trie, or 0 - the word was not in the trie.

- Uppercase and lowercase characters should be treated equally when searching for them in the tree.

### Task 4
Implement a function `deleteTree` that deletes a trie and all nodes in it.

**PARAMETERS:**
1. `root` a `Node` pointer to the root of a trie

**RETURN:** void

- Free each node within the tree and the root node.
- The `root` pointer should be NULL after the function returns.

## Trie
Diagram:
```
      root
     /    \
    f      c
   /      / \
  o      o   a
 / \    /   / \
x.  o  l   r.  t.
     \  \   \
      t. d.  e.
```
Note: letters in the above diagram with a period (.) following it indicate that the letter is the end of a word 
(e.g. `car` is contained within `care`).

## Building and Testing
To build and test your code, follow the [compile instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).

Be sure to check your compiler warnings and errors. Warnings often let you know when something you're doing may not be
what you intend.
