import socket
import re
import binascii
from cryptography.fernet import Fernet

# Refer to README.md for the problem instructions

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 5000 # The port used by the server

def create_fernet_and_find_sign_key(master_key):
    try:
        f = Fernet(master_key)
    except ValueError:
        raise ValueError('Potential Intrusion Event Detected.')
    
    return (f, f._signing_key)

def dowork():
    s = socket.socket()         # Create a socket object
    s.connect((HOST, PORT))     # Connect to the specified server

    ## 1
    response = s.recv(1024).decode("utf-8")  # Recieve the data
    try:
        f, skey = create_fernet_and_find_sign_key(response)
        print("The key is: ", skey)
    except ValueError as e:
        s.close()
        return str(e)

    ## 2
    s.send(skey)
    
    ## 3
    encryptedMessage = s.recv(1024)
    print("The encrypted message is: ", encryptedMessage)

    ## 4
    decryptedMessage = f.decrypt(encryptedMessage)
    print("The decrypted message is: ", decryptedMessage)
    s.send(decryptedMessage)
    
    ## 5
    status = s.recv(1024).decode("utf-8")
    s.close()

    if (status == "Success! Message confirmed\n"):
        return decryptedMessage
    else:
        return


def main():
    dowork()


if __name__ == '__main__':
    main()
