#se activa este cliente
#registrar "fecha_actual"
#enviar a servicio "consultar_estado_suscripcion" data: "rut"
#recibir "fecha_caducidad" desde servicio
#calcular y retornar dias restantes de suscripcion
import socket, pickle
import sys, json


def Consultar_sus():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    usuario = input("Ingrese RUT: ")
    print(f"RUT: {usuario}")
    post = str({'rut': usuario}).replace("'",'"').encode()
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5009)
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