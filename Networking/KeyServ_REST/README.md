# Networking: Key Server REST
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- A0626: String-based Protocol
- A0117: Develop client/server network programs
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).

## Tasks
The objective of these tasks is to utilize a relatively simple REST API provided by a webserver running on port 5000 of 
the grader system to obtain a key. This problem may be accomplished using the socket or http Python module.

### Task 1
Implement the function `do_key` that uses a fictional HTTP "KEY" method, along with the `/user/<user_id>/` url, to 
request a key. When finished, this function returns the key received from the server.

**PARAMETERS:**
- This function has no parameters

**RETURN:** a bytes object representing the key or `None` if an error occurs

- This function implements stages 1 & 2 of the communication map below.

### Task 2
Implement the function `do_put` that sends the key returned from `do_key` to the server using an HTTP "PUT" method, 
along with the `/key/<user_id>/<key_val>/` url, for verification. When finished, this function will return the server's 
response.

**PARAMETERS**
- `key_val`: an object containing the key returned from `do_key` that has no default value

**RETURN:** a str object containing the server's response

- This function implements stages 3 & 4 of the communication map below.

## Network Communication Map
Use this example for understanding the sequence that the Client/Server will communicate.

```text
1. CLIENT ----------------------> SERVER
- The CLIENT sends a fictional HTTP "KEY" method using the provided URL. ex: KEY /user/\<user_id\>/ HTTP/1.1 

2. CLIENT <---------------------- SERVER
- The SERVER sends back one of two messages. 
  1. If successful, you will receive a 128 HEX key.
  2. If unsuccessful, you will receive either a 400, 404 or 405 and a message describing the error.

3. CLIENT ----------------------> SERVER
- The CLIENT sends a HTTP "PUT" method using the provided URL. ex: PUT /key/\<user_id\>/\<key_val\>/ HTTP/1.1 

4. CLIENT <---------------------- SERVER
- The SERVER sends back one of two messages. 
  1. If successful, you will receive a message indicating your success.
  2. If unsuccessful, you will receive a message indicating the problem.
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
