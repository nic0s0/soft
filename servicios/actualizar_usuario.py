#esperar cliente, recibir data
#recibe datos: "rut", "meses"
#verifica si existe rut en bdd tabla "usuarios"
#si existe rut se agregan "meses" a "fecha_caducidad" || si no existe rut se agrega entrada a tabla "usuarios" con "rut" y "fecha_caducidad" segun "meses"
#retornar confirmacion de actualizacion

import socket, sys, json
from bdd import connectDb
from datetime import datetime

collection=connectDb()["usuarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5002)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096).decode()
            data = json.loads(data)
            print('received {!r}',data)
            #VER COMO SE MANEJA LA FECHA
            now = datetime.now()
            fecha = now.strftime("%Y-%m-%d")
            post = {"nombre":data["nombre"],"rut":data["rut"], "fecha":fecha, "meses":data["meses"]}
            collection.insert_one(post)            
            print('ESTES ES X: ',post)
            messs = '2'
            if post != None:
                print('sending data back to the client')
                connection.sendall(messs.encode())
                break
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()