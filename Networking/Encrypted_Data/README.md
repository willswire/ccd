# Networking: Encrypted Data
## KSAT List
This question is intended to evaluate the following topics:
- A0018: Analyze a problem to formulate a software solution.
- A0019: Integrate functionality between multiple software components.
- A0117: Develop client/server network programs.
- A0627: Bitwise Protocol    
- K0610: Understand how to utilize ports and protocols in network programming.    
- K0705: Demonstrate understanding of pervasive cryptographic primitives.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0026: Utilize standard library modules.
- S0093: Serialize fixed size multi-byte types between systems of differing endianness.
- S0094: Serialize and de-serialize variable sized data structures between systems of differing endianness.
- T0011: Analyze, modify, develop, debug and document software and applications utilizing
         standard, non-standard, specialized, and/or unique network communication protocols.
- T0028: Apply cryptography primitives to protect the confidentiality and integrity of sensitive data

## Tasks
You are going to work with a crypto server using TCP communication. Implement the function 
`get_message_using_encrypted_request_protocol` so it requests an encryption key from the crypto server and uses this 
key to encode and decode further communication. To communicate, this function sends/receives binary data packets 
to/from the crypto server in network byte order. Any necessary cryptographic processing is done using the Python 
cryptography module's Fernet symmetric-key encryption feature.

**PARAMETERS:**
- This function has no parameters

**RETURN:** a str object containing a plain text string received in stage 4 of the communication map below

- Note, encrypted messages are self-contained in Fernet tokens, including timestamps and message lengths, all of which 
  are automatically handled by the Fernet implementation.
- This function implements the entire communication map.

## Message Types and Payload Characteristics
Here are the different message types and their payload characteristics:

| Msg* type | Meaning       | Payload length | Payload meaning                     |
| --------- | -------       | -------------- | ---------------                     |
| 0x800     | key-request   | 44             | ignored                             |
| 0x801     | key-provide   | 44             | key (in Fernet bytearray format)    |
| 0x802     | encrypted msg | 100            | encrypted message (as Fernet token) |
| 0x8FF     | error         | 44             | may contain elaboration on error    |
  
**NOTE:** `Msg` stands for "message"

## Packet Details
Each packet contains the message type (a 32 bit unsigned int in network byte order) and a payload which contains the 
message text, if any. The payload will be 44 or 100 bytes depending on the message type, meaning that packets will be 
48 or 104 bytes in total. Some message types will require the message text to be encrypted before placing it in the 
payload. If the message to be sent does not fill the entire specified payload, it must be padded with null bytes. 
Strings inside Fernet tokens or error message payloads use UTF-8 format. Here is what a packet looks like.

```text
   Type                        Payload/key
+--------+-----------------------------------------------+
| 0x800  |    44 bytes - null padded if less than 44     |
|        |    100 bytes - null padded if less than 100   |
+--------+-----------------------------------------------+     
```

- Total length = 48 or 104 bytes.
- Note that Fernet uses 16 byte blocks. So a message 16 bytes or less will encode to a 100-byte token, but a 17 byte 
  message will encode to a longer token. For simplicity, we keep all messages under 16 bytes in length in this problem.
- This is not secure, most obviously because an attacker could sniff the key. A real key-exchange protocol like Diffie 
  Hellman is significantly more complex.

## Network Communication Map
```text
1. CLIENT -------------> SERVER
- After establishing a connection, the CLIENT sends a "key-request" message with a 44 byte payload (empty, all null).

2. CLIENT <------------- SERVER
- The SERVER sends a "key-provide" message, with the payload being the key (44 bytes, null-padded if needed).

3. CLIENT -------------> SERVER
- Client sends an "encrypted-message" of 100 bytes with the text "I challenge!" (encrypted as a Fernet token).

4. CLIENT <------------- SERVER
- The server sends a response as an `encrypted-message`, 100 byte payload (encrypted as a Fernet token). 
- Your function will return the text of this message, formatted as an ordinary Python string.
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
