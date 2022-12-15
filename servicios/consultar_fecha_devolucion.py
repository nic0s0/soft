#esperar cliente, recibir data
#recibe datos: "rut", "id_libro"
#consultar a bdd tabla "prestamos" la "fecha_devolucion"
#retornar "fecha_devolucion" a cliente

import socket, sys, json
from bdd import connectDb
from datetime import datetime, timedelta

collection=connectDb()["prestamos"]

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
            post = {"rut":data["rut"], "id_libro":data["id_libro"]}
            query = collection.find_one(post)
            fecha_devolucion = None
            if query:    
                print('ESTES ES X: ',query)
                fecha_devolucion = query["fecha_devolucion"]
                fecha_devolucion = datetime.strptime(fecha_devolucion, '%Y-%m-%d')

                atraso_total = datetime.now() - fecha_devolucion 
                fecha_devolucion = str(fecha_devolucion).replace(" 00:00:00","")
                atraso_total = atraso_total.days
                if atraso_total < 0:
                    atraso_total = 0
                    messs = "El libro "+str(data["id_libro"])+" se devuelve el "+str(fecha_devolucion)
                else:
                    messs = "El libro "+str(data["id_libro"])+" tiene "+str(atraso_total)+" dias de atraso, debe pagar $"+str(1000*atraso_total)
            else:
                messs = 'Libro no prestado a este usuario'
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