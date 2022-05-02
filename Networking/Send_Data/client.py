import socket
from student_helper import *

# Refer to README.md for the problem instructions

portpair = ('127.0.0.1', 5000) # webserver is running on port 5000 of the grader


def send_the_data():
    s = socket.socket()
    host = socket.gethostname()
    port = 5055
    s.bind((host, port))
    s.connect(portpair)

    data = serialize_dict_to_data(SCORES)
    s.sendall(data)

    response = s.recv(1024).decode()
    result = eval(response)

    s.close()

    return bytearray(result[0]).decode(), result[1]