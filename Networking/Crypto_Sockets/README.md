# Networking: Crypto Sockets
## KSAT List
This question is intended to evaluate the following topics:
- A0018: Analyze a problem to formulate a software solution.
- A0019: Integrate functionality between multiple software components.
- S0007: Skill in writing code in a currently supported programming language (e.g., Java, C++).
- S0026: Utilize standard library modules.
- S0047: Implement a function that returns multiple values.
- S0096: Utilize the Socket library.
- S0110: Implement error handling.

## Tasks
You are communicating with a secret agent. In order to talk to the agent, they will send you a key. Using the key they 
sent and the cryptography library, create a Fernet key. In order for both of you to be confident in your communication, 
you need to verify their key by checking the signing key in the Fernet object. After confirming that both of you are 
trusted, you can start decrypting the secret agent's messages. Randomly, a malicious actor will contact you with an 
initial fake key. If you detect the fake key, close your socket immediately.

### Task 1
Create the function `create_fernet_and_find_sign_key` so it generates a Fernet key from an input master key, finds its 
signing key, and returns the Fernet and signing keys. This function should use the cryptography Python module for key 
generation.

**PARAMETERS:**
1. `master_key`: a bytes object representing the master key

**RETURN:** Two values: a Fernet Key and signing key respectively

- Hint, the debugger may be useful to find the signing key.
- If there is an error creating the Fernet object, this function should throw a ValueError.
  - Do not use `BaseException` or `Exception` when detecting errors.
  - Set the ValueError message to `'Potential Intrusion Event Detected.'` as a string object.
- This function is used in stage 3 of the communication map shown below.

### Task 2
Implement the function `dowork` so it uses TCP to communicate with your secret agent, decrypts your agent's message, 
and returns the decrypted message. In order to communicate with your secret agent, you both need some assurance of 
trustworthiness. Therefore, this function performs the verification/validation steps explained below to acheive trust.

**PARAMETERS:**
- This function has no parameters

**RETURN:** a bytes string representing the decrypted message or the `ValueError` message as a normal string if 
`create_fernet_and_find_sign_key` throws an error

- This function implements the entire communication map.

#### Communication Verification/Validation
Your secret agent sent you connection details in a previous communication, refer to the `host` and `port` variables in 
`client.py`. Connect to your agent, using TCP communication, so you can receive the master key to decrypt your agent's 
messages. Once you receive the master key, you'll want to verify the key's trustworthiness. After all, you never know 
who might be listening.
- Using `create_fernet_and_find_sign_key`, check the master key and, if valid, get the encryption and signing key.
  - If the `create_fernet_and_find_sign_key` function throws a ValueError, the socket will be closed and the error 
    message will be returned as a string.
- If valid, send the signing key back to the server to be verified.
  - If the signing key is valid, the server will send back a spy phrase.
  - If the signing key is invalid, the server will send "Wrong signing key".

#### Message Decryption and Confirmation
Once you and your agent establish trustworthiness, your agent needs assurance that you received the proper message.
- Use your fernet key to decrypt the spy phrase and send it back to the server to confirm.
- In response to the confirmation, the server will send you a final confirmation message.
- Print the decrypted message to the console.
- Return the decrypted message as a bytes object.

## Network Communication Map
Use this example for understanding the sequence that the Client/Server will communicate.

```text
1. CLIENT <------------- SERVER
- SERVER: Will send a key. 
  - ex: b'E80Map25lE-ExamPLE_eXamPle-x_EXAMPLE='

2. CLIENT -------------> SERVER
- CLIENT: 
  - Validate the key you received to ensure it's a valid Fernet key.
  - If valid, send the signing key from the Fernet object.
    - ex: b"K\xd5\xc7\x0f\xa0\xe2\\'\x8f-\xdbF\xff\x8aj\x81"
  - If invalid, close the connection to the SERVER.

3. CLIENT <------------- SERVER
- SERVER: Will send back one of two messages. 
  1. If you have the correct signing key, you will receive an encrypted message.
     - ex: b'gAAAAABeglwZ_McoAA-eFQyWi_zjzuuycblmQiXrpCfGPSUgU8HbfWIH0ael-rtGJQHlfDRTEL51H7KM-20VS7ivtQtFXl0lnpAaGlnlR0ls6DjGtiu_A6gDpbUli8kATCCbWWxN-PFd'
  2. If you have the incorrect signing key, you will receive b"Wrong signing key".

4. CLIENT -------------> SERVER
- CLIENT: You will decrypt the previous message using your Fernet object and send back the decrypted message to confirm.
  - ex: b"I need to return some video tapes."

5. CLIENT <------------- SERVER
- SERVER: Will send back one of two messages. 
  1. On success, you will receive "Success! Message confirmed:".
  2. Unsuccessful, you will receive "INVALID Message: ".
```

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
