#esperar cliente, recibir data
#recibe datos: "rut", "id_libro"
#consultar a bdd tabla "prestamos" la "fecha_devolucion"
#retornar "fecha_devolucion" a cliente
import socket, sys, json
import os
from bdd import connectDb
from datetime import datetime

def calculo_estado(fecha_caducidad):
    fecha_caducidad = datetime.strptime(fecha_caducidad, "%Y-%m-%d")
    now = datetime.now()

    fecha_actual = now.strftime("%Y-%m-%d")
    fecha_actual = datetime.strptime(fecha_actual, "%Y-%m-%d")

    if fecha_actual > fecha_caducidad:
        messs = ["Vencida", str(fecha_caducidad)]
        return messs
    else:
        messs = ["Activa", str(fecha_caducidad)]
        return messs

collection=connectDb()["usuarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5009)
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
            post = {"rut":data["rut"]}
            query = collection.find_one(post)
            estado = None
            if query:
                print('ESTES ES X: ', query)
                estado = calculo_estado(query["fecha_caducidad"])
                if estado[0] == "Vencida":
                    messs = "Suscripcion vencida el " + estado[1]
                elif estado[0] == "Activa":
                    messs = "Suscripcion activa hasta el " + estado[1]
            else:
                messs = 'Usuario no registrado en el sistema'

            if post != None:
                print('sending data back to the client')
                print(messs)
                connection.sendall(messs.encode())
                break
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()