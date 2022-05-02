#!/usr/bin/env python

import socket, struct, base64
from cryptography.fernet import Fernet

# Refer to README.md for the problem instructions

dest = ('127.0.0.1', 1337)

cmd_list = {
    'key-request' : 0x800,
    'key-provide' : 0x801,
    'encrypted-message' : 0x802,
    'error' : 0x8FF
}

def enc(msg, key):
    f = Fernet(key)
    return f.encrypt(msg.encode('utf-8'))

def dec(msg, key):
    f = Fernet(key)
    return f.decrypt(msg)

#This function should return the server's final message as an actual Python 3 string,
#not as a byte sequence.
def get_message_using_encrypted_request_protocol():
    s = socket.socket()
    host = socket.gethostname()
    port = 7777
    s.bind((host, port))
    s.connect(dest)

    ## 1
    message = struct.pack(">I44x", cmd_list['key-request'])
    print("Sending message: ", message)
    s.send(message)

    ## 2
    message = s.recv(48)
    print("Message received: ", message)
    key = message[4:]

    ## 3
    payload = enc("I challenge!", key)
    message = struct.pack(">I", cmd_list['encrypted-message']) + payload
    print("Sending message: ", message)
    s.send(message)

    ## 4
    message = s.recv(104)
    print("Message received: ", message)
    text = dec(message, key).decode('utf-8')
    s.close()

    return text


if __name__ == "__main__":
    message = get_message_using_encrypted_request_protocol()
    print(message)

