#se activa este cliente
#enviar a servicio "consultar_estado_suscripcion" data: "rut", "meses"
#recibir "fecha_caducidad" desde servicio
#calcular y retornar dias restantes de suscripcion
import socket
import sys, json

def Activar():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5004)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    
    rut = input("Ingrese RUT: ")
    meses = input("Ingrese meses de suscripción: ")

    post = str({'rut':rut, 'meses': meses}).replace("'", '"').encode()
    
    try:
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            amount_received += len(data)
            print('\n{!r}\n'.format(data))
            return data.decode("utf-8")
    finally:
        sock.close()
        