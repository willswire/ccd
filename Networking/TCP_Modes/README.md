# Networking: TCP_Modes
## KSAT List
This question is intended to evaluate the following topics:
- A0019: Integrate functionality between multiple software components.
- A0018: Analyze a problem to formulate a software solution.
- K0091: Understand how to account for endianness between differing systems.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0094: Serialize and de-serialize variable sized data structures between systems of differing endianness.
- S0093: Serialize fixed size multi-byte types between systems of differing endianness.
- S0096: Utilize the Socket library.

## Tasks
Establish communication with a TCP server, running on port 1337 of the server, using a fictional protocol.

### Task 1
Implement the function `query_mode` that connects to the server from `accept_port_1`, in `client.py`; sends a request 
for the mode and returns the server's response.

**PARAMETERS:**
- This function has no parameters

**RETURN:** A UTF-8 string containing the server's response

- Send the `query_mode` command from the `cmd_list` dictionary.
- The communication should follow the [fictional protocol specification](#fictional-protocol-specification).
- The server communicates in network byte order.
- This function implements stages 1-2 of the communication map provided below.

### Task 2
Implement the function `get_key` that connects to the server from `accept_port_2`, in `client.py`; sends a request for 
the key and returns the server's response.

**PARAMETERS:**
1. `recv`: The mode returned from the `query_mode` function

**RETURN:** A UTF-8 string containing the server's response

- Send the `get_key` command from the `cmd_list` dictionary in `client.py`.
- The communication should follow the [fictional protocol specification](#fictional-protocol-specification).
- The server communicates in network byte order.
- This function implements stages 3-4 of the communication map.

## Fictional Protocol Specification
The following information documents the specification of our fictional protocol.

### Packet Structure
A packet of our fictional protocol is structured as depicted below.

```text
+ - - - - + - - - - +
|    1    |    2    |
+ - - - - + - - - - +
```

1. A 4-byte unsigned long command or response
2. A 4-byte unsigned long payload

### Supported Commands
The supported commands are listed in the command table below.

| Command | Meaning    | Payload |
| ------- | -------    | ------- |
| 0x802   | query mode | padding |
| 0x803   | get key    | mode    |

- The padding is created using zeros.

### Supported Responses
The supported responses are listed in the response table below.

| Response | Meaning | Payload |
| -------- | ------- | ------- |
| 0x800    | success | mode    |
| 0x801    | error   | data    |

The error response data will be:
- all 0's if an error occurred.
- all f's if the request cannot be processed.

### Get Key Response
If the get key command is successful, the response packet is structured as follows.
```text
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
|                              A key                              |
|                         32-byte string                          |
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
```



# Network Communication Map
1. CLIENT -----------> SERVER
   * Client sends first command to the server along with arguments
2. CLIENT <----------- SERVER
   * Server replies with 'success' on success
   * Server replies with 'error' followed by zeros on a generic error
   * Server replies with all f's if an exception occurred while processing request
3. CLIENT -----------> SERVER
   * Client sends second command to the server along with arguments
4. CLIENT <----------- SERVER
   * Server replies with a 32 byte string on success
   * Server replies with 'error' followed by zeros on a generic error
   * Server replies with all f's if an exception occurred while processing request

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
