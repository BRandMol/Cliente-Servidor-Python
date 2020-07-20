host = '192.168.122.214'
port = 9090

import socket

obj = socket.socket()

obj.connect((host, port))
print("Conectado al servidor")

while True:

    mens = input("Mensaje desde Cliente a Servidor >> ")

    obj.send(mens.encode('ascii'))

    recibido = obj.recv(1024)
    print(recibido)

obj.close()

print("Conexión cerrada")