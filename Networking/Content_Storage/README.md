# Networking: Content Storage
## KSAT List
This question is intended to evaluate the following topics:
- A0117: Develop client/server network programs.
- S0026: Utilize standard library modules.
- S0037: Open and close an existing file.
- S0038: Read, parse, write (append, insert, modify) file data.
- S0050: Implement a function that doesn't return a value.
- S0096: Utilize the Socket library.

## Tasks
You have been tasked with creating a server that triggers clients to send data to it and then saves that data as it is 
received.

### Task 1
Implement the function `contact_clients` that contacts a remote server (the client), using the host and port variables 
in `content_manager.py`, and sends the server the port identified in the `srv_port` variable. The `srv_port` variable 
contains the listening port of your server.

**PARAMETERS:**
- This function has no parameters

**RETURN:** None

- This task implements stage 3 of the communication map below.

### Task 2
Implement the function `serve_clients` that listens on the port identified in `srv_port` and calls the function 
`contact_clients` to signal clients to communicate with it. Save incoming data as a file using the name and data sent 
by the client. Refer to the Network Communication Map section below for a detailed description of the communication.

**PARAMETERS:**
- This function has no parameters

**RETURN:** None

- The client's message uses the following format: `file name\nfile contents`.
- After handling 2 requests the function will clean up and return.
- This task implements stages 2, 4, and 5 of the communication map below and calls `contact_clients()` for stage 3.

#### Example:
The REMOTE SERVER sends you the message below.
```text
example.txt\na,b,c\n1,2,3\n
```

The message above would be saved as a file named `example.txt` with the following contents:
```text
a,b,c
1,2,3
```

## Network Communication Map
```text
In this problem there are technically 2 programs that act as servers: your content_manager.py, and a remote server 
waiting to be told to connect to your content_manager.py server.  We refer to the remote server as REMOTE SERVER, and 
your program as CONTENT MANAGER.

1. REMOTE SERVER
- Listens on port 5000   

2. CONTENT MANAGER (your code)
- Listens on port 1337

3. CONTENT MANAGER (you) -------------> REMOTE SERVER
- After establishing a connection to port 5000, content manager informs the remote server of the port it should use for 
  communication (1337), and then closes the connection.

4. CONTENT MANAGER (you) <------------- REMOTE SERVER
- After establishing a connection to content manager's port 1337, the remote server sends over the file name and file 
  contents to be written to disk, then closes the connection.  (Note this step will occur twice.)

5. CONTENT MANAGER (you)
- Stops listening
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
