import socket

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser.bind(('192.168.122.214', 9090))

ser.listen(1)

cli, addr = ser.accept()

while True:

	recibido = cli.recv(1024)

	print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

	data= recibido.decode("utf-8").split()
	msg_toSend = "Recibi tu mensaje"

	cli.send(msg_toSend.encode('ascii'))

cli.close()