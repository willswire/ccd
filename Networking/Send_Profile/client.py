import json
import pickle
import socket

# Refer to README.md for the problem instructions

host = "network-server"
port = 5000


def read_user_info(file_name):
    contents = ''
    try:
        with open(file_name) as f:
            contents = f.read()
    except:
        return "File does not exist"

    try:
        result = json.loads(contents)
        return result
    except:
        return "Invalid format"

def send_user_data(data):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 2555
    s.bind((host, port))
    s.connect(("127.0.0.1", 5000))

    if (data['usr_cred']):
        s.send(data['usr_cred'].encode())

    response = s.recv(1024).decode()

    if (response != 'Invalid credentials'):
        if (data['usr_cred']):
            data.pop('usr_cred')
        s.send(pickle.dumps(data))
        response = s.recv(1024).decode()

    s.close()
    return response


def logon(file_name):
    userData = read_user_info(file_name)
    if (userData == "File does not exist" or userData == "Invalid format"):
        return userData
    else:
        return send_user_data(userData)