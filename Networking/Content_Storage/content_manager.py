import socket

# Refer to README.md for the problem instructions

host = "127.0.0.1"
port = 5000
srv_port = 1337

# Stage 1: run remote server with ./run_server_debian

def contact_clients():
    s = socket.socket()
    s.connect((host, port))
    s.send(str(srv_port).encode("utf-8"))
    s.close()   

def serve_clients():
    # Stage 2: listen on port 1337
    s = socket.socket()
    s.bind((host, srv_port))
    s.listen(5)

    # Stage 3: inform remote server of com port
    contact_clients()

    requestCount = 0
    while requestCount < 2:
        res = None
        # Stage 4: listen for remote server info
        while (res == None):
            c, _ = s.accept()
            res = c.recv(1024).decode("utf-8")

            # Stage 5: stops listening
            c.close()
        
        splitRes = res.splitlines()

        with open(splitRes[0], 'w') as f:
            for entry in splitRes[1:]:
                f.write(entry)
                f.write('\n')

        requestCount += 1
    s.close()
