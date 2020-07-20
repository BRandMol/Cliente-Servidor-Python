import socket

def get_unity(s):
	unities = {
		"km": "kilometros",
		"m": "metros",
		"dm": "decimetros",
		"cm": "centimetros",
		"mm": "milimetros",
		"micron": "micrometros",
		"nm": "nanometros",
        "mi": "millas",
        "yd": "yardas",
        "ft": "pies",
        "in": "pulgadas",
        "Nm": "millas nauticas"
	}
	return unities[s]

def convert(a, b, c):
    values = {
        "km": 1000.0,
        "m": 1.0,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001,
        "micron": 0.000001,
        "nm": 0.00000001,
        "mi": 1609.34,
        "yd": 0.9144,
        "ft": 0.3048,
        "in":0.0254,
        "Nm": 1852.0
    }

    return (values[b] * a) / values[c]


ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser.bind(('192.168.122.214', 9090))

ser.listen(1)

cli, addr = ser.accept()

while True:

	recibido = cli.recv(1024)

	print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1])) + " " + get_unity(data[3])

	data= recibido.decode("utf-8").split()
	msg_toSend = str(convert(int(data[0]),data[1],data[3]))

	cli.send(msg_toSend.encode('ascii'))

cli.close()