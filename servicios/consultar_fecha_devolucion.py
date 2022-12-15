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
            query = collection.find(post)
            fecha_devolucion = None
            for x in query:
                print('ESTES ES X: ',x)
                fecha_devolucion = x["fecha_devolucion"]
                fecha_devolucion = datetime.strptime(fecha_devolucion, '%Y-%m-%d')
            atraso_total = datetime.now() - fecha_devolucion 
            atraso_total = atraso_total.days
            if atraso_total < 0:
                atraso_total = 0
                messs = str({"atraso_total":str(atraso_total), "fecha_devolucion":str(fecha_devolucion)}).replace("'",'"').encode()
            else:
                messs = str({"atraso_total":str(atraso_total), "fecha_devolucion":str(fecha_devolucion), "deuda":str(1000*atraso_total)}).replace("'",'"').encode()
                
            if post != None:
                print('sending data back to the client')
                connection.sendall(messs)
                break
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()