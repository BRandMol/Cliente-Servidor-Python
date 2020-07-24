import socket
import sys

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
        "Nm": "millas nauticas",

        "dam": "decametro",
        "hm": "hectometro",
        "Mm": "megametro",
        "Gm": "gigametro",
        "Tm": "terametro",
        "Pm": "petametro",
        "Em": "Exametro",
        "Zm": "zettametro",
        "Ym": "yottametro",
        
        "pm": "picometro",
        "fm": "femtometro",
        "am": "attometro",
        "zm": "zeptometro",
        "ym": "yoctometro"

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
        "in": 0.0254,
        "Nm": 1852.0,

        "dam": 10.0,
        "hm": 100.0,
        "Mm": 10.0**6,
        "Gm": 10.0**9,
        "Tm": 10.0**12,
        "Pm": 10.0**15,
        "Em": 10.0**18,
        "Zm": 10.0**21,
        "Ym": 10.0**24,
        
        "pm": 10.0**(-12),
        "fm": 10.0**(-15),
        "am": 10.0**(-18),
        "zm": 10.0**(-21),
        "ym": 10.0**(-24)
    }

    return (values[b] * a) / values[c]


ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser.bind((sys.argv[1], int(sys.argv[2])))

ser.listen(1)

try:
    while True:
        print ("Esperando conexión de un cliente ...")
        cli, addr = ser.accept()
        print ("Cliente conectado desde: ", addr)
        print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

        while True:
            try:
                recibido = cli.recv(1024)
                if recibido == "finalizar":
                    print ("Cliente a finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    cli.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                data = recibido.decode("utf-8").split()
                if len(data) == 4:
                	msg_toSend = str(convert(int(data[0]),data[1],data[3])) + " " + get_unity(data[3])
                	cli.send(msg_toSend.encode('ascii'))
                else:
                	break

            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                cli.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\nSe interrumpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                cli.close()
                print ("Conexion con el cliente cerrado.")
                break
except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    print ("Cerrando el servicio ...")
    ser.close()
    print ("Servicio cerrado, Adios!")