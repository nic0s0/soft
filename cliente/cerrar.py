import socket, pickle
import sys, json

def Cerrar():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    post = str({'cerrar': "1"}).replace("'",'"').encode()
    
    # Connect the socket to the port where the server is listening
    puertos = [5001, 5002, 5003, 5004, 5005, 5006]
    server_address = ('localhost', 5002)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            amount_received += len(data)
            print('received {!r}'.format(data))
            return data.decode("utf-8"), usuario
    finally:
        print('closing socket')
        sock.close()