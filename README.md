# Cliente-Servidor-Python

_Este proyecto realiza la conexion entre Cliente y Servidor, y su funcionalidad es la conversion de distancias_

### Pre-requisitos 📋

_Python 3_

## Ejecutando servidor.py ⌨️

_Para ejecutar servidor.py hay que realizar lo siguiente, por consola nos ubicamos en la carpeta del proyecto y lanzamos el siguiente comando_

```
$ python3 servidor.py 9090
```

Donde el 3° parametro (9090) define el puerto del servidor

## Ejecutando cliente.py ⌨️

_Para ejecutar cliente.py hay que realizar lo siguiente, por consola nos ubicamos en la carpeta del proyecto y lanzamos el siguiente comando_

```
$ python3 cliente.py 192.168.122.214 9090
```

Donde:

El 3° parametro (192.168.122.214) define la IP del servidor a la cual se va a conectar el cliente

El 4° parametro (9090) define el puerto del servidor

_Una vez conectado_

_Para utilizar la funcionalidad de conversion de distancias hay que tener lo siguiente en consideracion_

_Las nomenclaturas utilizadas y las medidas que soporta_

- km: kilometros
- m: metros
- dm: decimetros
- cm: centimetros
- mm: milimetros
- micron: micrometros
- nm: nanometros
- mi: millas
- yd: yardas
- ft: pies
- in: pulgadas
- Nm: millas nauticas
- legua: leguas
- ln: leguas nauticas
- dam: decametros
- hm: hectometros
- Mm: megametros
- Gm: gigametros
- Tm: terametros
- Pm: petametros
- Em: Exametros
- Zm: zettametros
- Ym: yottametros
- pm: picometros
- fm: femtometros
- am: attometros
- zm: zeptometros
- ym: yoctometros
        
_Teniendo eso en cuenta hay que seguir el siguiente formato para lograr un buen funcionamiento y una correcta transformacion_

_1° parametro: Cantidad_

_2° parametro: Unidad incial_

_3° parametro: "a"_

_4° parametro: Unidad a la cual se quiere convertir_

_Importante: tener en consideracion la separacion por un espacio cada parametro_

_Ejemplo:_

```
$ 100 km a m
```

## Construido con 🛠️

* [Python 3](https://www.python.org/) - El lenguaje usado

## Autores ✒️

* **Andrés Sanchéz** - *Trabajo Inicial* -
* **Boris Molina** - *Documentación* -
* **Marcelo Salinas** - *Documentación* -

---
