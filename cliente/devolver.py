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
    #print('\nconnecting to {} port {}\n'.format(*server_address))
    sock.connect(server_address)
    
    rut = input("Ingrese RUT: ")
    id_libro = input("Ingrese ID del libro: ")

    post = str({'rut':rut, 'id_libro': id_libro}).replace("'", '"').encode()
    
    try:
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            amount_received += len(data)
            print('\n'+data.decode("utf-8")+'\n')
            return data.decode("utf-8")
    finally:
        sock.close()
        