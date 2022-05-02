# Networking: Send Data
## KSAT List
This question is intended to evaluate the following topics:
- A0117: Develop client/server network programs.
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- A0626: String-based Protocol
- S0096: Utilize the Socket library.

## Tasks
Implement the function `send_the_data` so it sets up TCP communication using the python socket module; sends serialized 
scores to the provided host and port; and splits the server's response into a string and an int. When the function is finished, it 
returns the server's string and int response respectively.

**PARAMETERS:**
- This function has no parameters

**RETURN:** a string and int, respectively, containing the server's response

- Use the `serialize_dict_to_data` function and `SCORES` dict in `student_helper.py` to serialize the provided scores.
- Send the serialized scores to the server in order to receive a decrypted response.
- Split the server's response into two values, a string and an int, and return these two values respectively.

**Example:**
- After `send_the_data` sends the serialized scores, the server's response of `b'(b"TEST WORDS PLS IGNORE", 64)'` 
  should cause this function to return a string of `TEST WORDS PLS IGNORE` and an int of 64.

# Network Communication Map
```text
CLIENT ----> SERVER

CLIENT sends the serialized string

CLIENT <---- SERVER

SERVER returns the response string

Connection ends
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
