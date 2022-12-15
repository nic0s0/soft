#se activa este cliente
#registrar "fecha_actual"
#enviar a servicio "consultar_estado_suscripcion" data: "rut"
#recibir "fecha_caducidad" desde servicio
#calcular y retornar dias restantes de suscripcion
import socket, pickle
import sys, json


def Consultar_sus():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5009)
    #print('\nconnecting to {} port {}\n'.format(*server_address))
    sock.connect(server_address)

    usuario = input("Ingrese RUT: ")

    post = str({'rut': usuario}).replace("'",'"').encode()
    
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