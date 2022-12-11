#esperar cliente, recibir data
#recibe datos: "rut", "id_libro"
#consultar a bdd tabla "prestamos" la "fecha_devolucion"
#retornar "fecha_devolucion" a cliente

import socket, sys, json
from bdd import connectDb

collection=connectDb()["prestamos"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5010)
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
            post = {"rut":data["rut"], "id_libro":data["id_libro"]}
            query = collection.find(post)
            for x in query:
                print('ESTES ES X: ',post)
                fecha_devolucion = x["fecha_devolucion"]
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