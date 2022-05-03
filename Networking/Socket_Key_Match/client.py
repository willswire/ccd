import socket
import random
from random import randint

# Refer to README.md for the problem instructions

serverName = "network-server"
serverPort = 5000

session_keys = ["aa072fbbf5f408d81c78033dd560d4f6",
                "bb072fbbf5f408d81c78033dd560f6d4",
                "f5072fbbf5f408d81c78033dd5f6d460",
                "408df5072fbbf5f81c3dd5f6d4607803",
                "dd5f408df5072fbbfc36d46078035f81",
                "c36d408df5072fbbf46078035f81dd5f",
                "35f8c36df5072fbbf4607801dd5fd408",
                "2f07aaf408d81c78033dd560d4f6bbf5",
                "80332ff408d81c7dd560d4f6bbf507aa",
                "560d4f8033281c7dd6bbf507aaff408d",
               ]


def match_keys():
    k2 = ""
    reply = ""
    kIndex = 0

    while ("Success" not in reply):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 2525 + kIndex))
        s.connect(("127.0.0.1", 5000))
        
        message = s.recv(1024).decode()
        print("Received message: ", message)

        k1 = ""
        if (message == "SERVER>>> Connection successful"):
            k1 = s.recv(1024).decode()
            print("Key from server: ", k1, "\n")

        k2 = "0x" + session_keys[kIndex]
        print("Key to test: ", k2)

        k3 = hex(int(k1, 16) ^ int(k2, 16))
        print("XOR Key result: ", k3)

        s.send(k3.encode())
        reply = s.recv(1024).decode()
        print("Server reply: ", reply)

        kIndex += 1
        s.close()

    return reply.encode(), k2[2:]
