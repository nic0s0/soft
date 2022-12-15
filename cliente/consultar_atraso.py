#se activa este cliente
#registrar "fecha_actual"
#enviar a servicio "consultar_fecha_devolucion" data: "rut", "id_libro"
#recibir "fecha_devolucion" desde servicio
#calcular atraso en "dias_atraso" y "monto_deuda" con "fecha_actual" y "fecha_devolucion"
import socket, pickle
import sys, json


def Consultar_atraso():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5002)
    #print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    usuario = input("Ingrese RUT: ")
    id = input("Ingrese ID del libro: ")

    post = str({'rut': usuario, 'id_libro': id}).replace("'",'"').encode()
    
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