#esperar cliente, recibir data
#recibe datos: "rut", "meses"
#verifica si existe rut en bdd tabla "usuarios"
#si existe rut se agregan "meses" a "fecha_caducidad" || si no existe rut se agrega entrada a tabla "usuarios" con "rut" y "fecha_caducidad" segun "meses"
#retornar confirmacion de actualizacion
import socket, sys, json
import os
from bdd import connectDb
from datetime import date, timedelta, datetime

collection = connectDb()["usuarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5004)
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
            meses = int(data["meses"])
            documento = collection.find_one({"rut":data["rut"]})
            if documento != None:
                fecha_registrada = str(documento["fecha_caducidad"])
                fecha_caducidad1 = datetime.strptime(fecha_registrada, '%Y-%m-%d').date()
                fecha_caducidad2 = str(fecha_caducidad1 + timedelta(days=(meses*30)))         
                collection.update_one({"rut":data["rut"]},{"$set": {"fecha_caducidad":fecha_caducidad2}})
                post = {"rut":data["rut"], "fecha_caducidad":fecha_caducidad2}
                messs = 'Usuario '+data["rut"]+' actualizado hasta '+fecha_caducidad2
            else:
                fecha_caducidad = str(date.today() + timedelta(days=(meses*30)))
                post = {"rut":data["rut"], "fecha_caducidad":fecha_caducidad}
                collection.insert_one(post)            
                messs = 'Usuario '+data["rut"]+' actualizado hasta '+fecha_caducidad
            print('ESTES ES X: ', post)
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