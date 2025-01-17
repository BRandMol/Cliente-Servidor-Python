import socket
import sys
import netifaces as ni

#Funcionalidad que perimite indicar la unidad de medida asociada
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

        "legua": "leguas",
        "ln": "leguas nauticas",

        "dam": "decametros",
        "hm": "hectometros",
        "Mm": "megametros",
        "Gm": "gigametros",
        "Tm": "terametros",
        "Pm": "petametros",
        "Em": "exametros",
        "Zm": "zettametros",
        "Ym": "yottametros",

        "pm": "picometros",
        "fm": "femtometros",
        "am": "attometros",
        "zm": "zeptometros",
        "ym": "yoctometros"

    }
    return unities[s]

#Funcionalidad que perimite la conversion de las unidades de medida
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

        "legua": 4828.03,
        "ln": 5558.0,

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

#Creacion de un TCP/IP socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenemos la ip local
ni.ifaddresses('ens3')
ip = ni.ifaddresses('ens3')[ni.AF_INET][0]['addr']

# Enlace del socket con la IP y el puerto
ser.bind((ip, int(sys.argv[1])))

# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
ser.listen(1)

try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto cli para recibir datos,
        # addr recibe la tupla de conexion: IP y puerto
        cli, addr = ser.accept()

        
        print ("Cliente conectado desde: ", addr)
        print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

        while True:
            try:
                # mensaje recibido por el usuario
                recibido = cli.recv(1024)
                if recibido == "finalizar":
                    print ("Cliente a finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    #Terminar la conexion cliente - servidor
                    cli.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                # variable que almacenara el mensaje del cliente y lo separara
                data = recibido.decode("utf-8").split()
                if len(data) == 4:
                    # variable que alamacenara la conversion de las unidades de medida entregadas por el cliente
                    msg_toSend = str(convert(int(data[0]),data[1],data[3])) + " " + get_unity(data[3])
                    # envia la respuesta de la conversion al cliente
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