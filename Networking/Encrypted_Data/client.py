#!/usr/bin/env python

import socket, struct
from cryptography.fernet import Fernet

# Refer to README.md for the problem instructions

dest = ('127.0.0.1', 1337)

cmd_list = {
    'key-request' : 0x800,
    'key-provide' : 0x801,
    'encrypted-message' : 0x802,
    'error' : 0x8FF
}

def pack(cmd, msgLength = 0):
    padLength = 0
    if msgLength < 44:
        padLength = 44 - msgLength
    else:
        padLength = 100 - msgLength
    formatStr = ">I" + str(padLength) + "x"
    packet = struct.pack(formatStr, cmd_list[cmd])
    return packet

def enc(msg, key):
    f = Fernet(key)
    return f.encrypt(msg)

#This function should return the server's final message as an actual Python 3 string,
#not as a byte sequence.
def get_message_using_encrypted_request_protocol():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.connect(dest)

    ## 1
    message = pack('key-request')
    print("Sending message: ", message)
    s.send(message)

    ## 2
    message = s.recv(44)
    print("Message received: ", message)
    key = message[4:]

    ## 3
    payload = enc("I challenge!", key)
    print("Encrypted payload: ", payload)

    s.close()
    return ""


if __name__ == "__main__":
    message = get_message_using_encrypted_request_protocol()
    print(message)
