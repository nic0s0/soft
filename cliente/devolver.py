#se activa este cliente
#enviar a servicio "eliminar_prestamo" data: "rut", "id_libro"
#recibir confirmacion de eliminacion de prestamo desde servicio
#retornar confirmacion
import socket
import sys, json

def Devolver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5006)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    
    print("Ingrese RUT")
    rut = input()
    print("Ingrese ID de libro")
    id_libro = input()

    post = str({'rut':rut, 'id_libro': id_libro}).replace("'", '"').encode()
    
    try:
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            amount_received += len(data)
            print('received {!r}'.format(data))
            return data.decode("utf-8")
    finally:
        print('closing socket')
        sock.close()
        