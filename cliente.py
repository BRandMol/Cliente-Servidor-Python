import socket
import sys

# funcionalidad encargada de desplegar las intrucciones del programa
def menu():
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

        "dam": "decametros",
        "hm": "hectometros",
        "Mm": "megametros",
        "Gm": "gigametros",
        "Tm": "terametros",
        "Pm": "petametros",
        "Em": "Exametros",
        "Zm": "zettametros",
        "Ym": "yottametros",
        
        "pm": "picometros",
        "fm": "femtometros",
        "am": "attometros",
        "zm": "zeptometros",
        "ym": "yoctometros"
        
    }
    print("\nPara realizar una transformacion debe utilizar las siguientes abreviaciones\n")
    for x in unities:
        print("\t" + x + ": " + unities[x])
    print("\nDebe hacerlo mediante el siguiente formato de ejemplo:")
    print("\n\t 100 cm a m\n")
    print("El ejemplo anterior realizara la conversion de 100 centimetros a metros")
    print ("\n Para terminar la conexion escriba finalizar\n")

#variables que indican la IP y el PUERTO
host = sys.argv[1]
port =int(sys.argv[2])

# variable que permitira la conexion indicando la IP y el PUERTO
obj = socket.socket()

try:
    obj.connect((host, port))
    print ("\nConectandose al servidor ", host, " en el puerto ", port, " ...")
except:
    print ("No se puede conectar con el servidor.", host, " en el puerto ", port)
    sys.exit(0)
menu()


try:
    while True:
        while True:
            # Mensaje del cliente al servidor
            mens = input("Mensaje desde Cliente a Servidor >> ")
            if len(mens) != 0:
                break
        
        obj.send(mens.encode('ascii'))
        if mens == "finalizar":
            break
        # mensaje recibido por el cliente    
        recibido = obj.recv(1024)
        print("\n\t"+recibido.decode("utf-8") + "\n")

except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrumpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    obj.close()
    print ("Conexion con el servidor terminado.")