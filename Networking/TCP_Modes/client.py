#!/usr/bin/env python
# Refer to README.md for the problem instructions

import socket, struct

dest = ('127.0.0.1', 1337)
accept_port_1 = 12345
accept_port_2 = 54321

cmd_list = {
    'success' : 0x800,
    'error' : 0x801,
    'query_mode' : 0x802,
    'get_key' : 0x803,
}

padding = 0x0000

def query_mode():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", accept_port_1))
    s.connect(dest)

    packet = struct.pack(">L4x", cmd_list['query_mode'])
    print("Sending packet: ", packet)
    s.send(packet)

    packet = s.recv(8)
    print("Received packet: ", packet)
    reply = struct.unpack(">2L", packet)
    print("Cmd: ", hex(reply[0]), "Payload: ", hex(reply[1]))

    s.close()
    return reply

def get_key(recv):
    mode = query_mode()[1]

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", accept_port_2))
    s.connect(dest)

    packet = struct.pack(">LL", cmd_list['get_key'], mode)
    print("Sending packet: ", packet)
    s.send(packet)

    packet = s.recv(32)
    print("Received key: ", packet)
    key = packet.decode()

    return key


