#esperar cliente, recibir data
#recibe datos: "rut", "meses"
#verifica si existe rut en bdd tabla "usuarios"
#si existe rut se agregan "meses" a "fecha_caducidad" || si no existe rut se agrega entrada a tabla "usuarios" con "rut" y "fecha_caducidad" segun "meses"
#retornar confirmacion de actualizacion

import socket, sys, json
from bdd import connectDb
from datetime import datetime
from dateutil.relativedelta import relativedelta

def actualizar_usuario(data):
    if collection.find_one({"rut":data["rut"]}) != None:
        print('usuario existe')
        fecha = collection.find_one({"rut":data["rut"]})["fecha_caducidad"]
        fecha = fecha + relativedelta(months=int(data["meses"]))
        collection.update_one({"rut":data["rut"]},{"$set":{"fecha_caducidad":fecha}})
        post = collection.find_one({"rut":data["rut"]})
        return post
    else:
        now = datetime.now()
        fecha = now + relativedelta(months=int(data["meses"]))
        post = {"nombre":data["nombre"],"rut":data["rut"], "fecha_caducidad":fecha}
        collection.insert_one(post)
        return post

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
                        
            post = actualizar_usuario(data)
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