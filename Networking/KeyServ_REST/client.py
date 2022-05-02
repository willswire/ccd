#!/usr/bin/env python

import socket, http.client, re

http_string = "GET / HTTP/1.1\r\n\r\n"
portpair = ('127.0.0.1', 5000) # webserver is running on port 5000 of the grader

g_user_id = 'User1'

# Refer to README.md for the problem instructions

def do_key():
    s = socket.socket()
    host = socket.gethostname()
    port = 5055
    s.bind((host, port))
    s.connect(portpair)

    ## 1
    http_string = "KEY /user/" + g_user_id + "/ HTTP/1.1\r\n\r\n"
    s.send(http_string.encode('utf-8'))

    ## 2
    response = b""
    while True:
        chunk = s.recv(4096)
        if len(chunk) == 0:     # No more data received, quitting
            break
        response = response + chunk

    s.close()

    key = response[-128:]

    return key


def do_put(key_val) -> str:
    s = socket.socket()
    host = socket.gethostname()
    port = 5056
    s.bind((host, port))
    s.connect(portpair)

    ## 3
    http_string = "PUT /key/" + g_user_id + "/" + key_val.decode('utf-8') + "/ HTTP/1.1\r\n\r\n"
    s.send(http_string.encode('utf-8'))

    ## 4
    response = b""
    while True:
        chunk = s.recv(4096)
        if len(chunk) == 0:     # No more data received, quitting
            break
        response = response + chunk

    s.close()

    strRes = response.decode('utf-8')
    formattedResponse = strRes.split("\r\n\r\n")[-1]

    return formattedResponse
