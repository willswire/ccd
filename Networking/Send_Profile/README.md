# Networking: Send Profile
## KSAT List
- A0117: Develop client/server network programs.
- S0026: Utilize standard library modules.
- S0037: Open and close an existing file.
- S0038: Read, parse, write (append, insert, modify) file data.
- S0052: Implement a function that returns a single value.
- S0096: Utilize the Socket library.
- S0110: Implement error handling.

## Tasks
Implement a client that can read a user's data file and use it to login to a TCP server running on the provided port in 
`client.py`.

### Task 1
Implement the `read_user_info` function to open a json file, using the given file name, and return its contents.

**PARAMETERS:**
1. `file_name`: A string containing the name of the json file in which to read user data

**RETURN:** A dict containing the user's data, a string "File does not exist" if the file does not exist, or a string 
"Invalid format" if the file is not in valid json format

### Task 2
Implement the function `send_user_data` to connect to the provided host and port, and send the user's credentials 
(usr_cred) to the TCP server.

**PARAMETERS:**
1. `data`: the json formatted data to send to the server

**RETURN:** A string containing the server's response message

- Use UTF-8 encoding. 
- Connect to the server and send the user's credentials to log in.
- If you do not receive "Authentication successful" from the server, close the connection and return the server's response.
- Remove the user's credentials before sending the user data.
- Use the pickle module to pickle the user data before sending it to the server.
- This function should implement the entire Network Communication Map.

### Task 3
Implement the function `logon` that, given a file name, uses the previous tasks' functions to return the server's 
response from a logon attempt.

**PARAMETERS:**
1. `file_name`: A string containing the name of the json file in which to read user data

**RETURN:** A string containing the server's response message, "File does not exist" if the file does not exist, or 
"Invalid format" if the file is not in valid json format

- Use both the `read_user_info` and `send_user_data` functions in this function.

# Network Communication Map
```
CLIENT -------------> SERVER

After establishing a connection, the CLIENT sends the user's credential

CLIENT <------------- SERVER

The SERVER verifies the credentials

If correct the SERVER sends Authentication successful
If incorrect the SERVER sends Invalid credentials

CLIENT -------------> SERVER

Upon successful authentication, the CLIENT sends the remaining user data serialized

CLIENT <------------- SERVER

The SERVER sends a welcome message, ex: Welcome AcidBurn you have 220 posts.
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
