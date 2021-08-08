# Programacion Orientada a Objetos

Clases y Objetos

- programacion orientada a objetos
- permite definir tipos propios
- permite manejar datos y logica en un solo contenedor
- las clases son como fabricas (moldes) para crear otros objetos

### metodos y propiedades
- las propiedades son las caracteristicas del objeto
ejemplo:  
1. Persona: ojos, cabello, piernas, manos, ropa, zapatos, reloj
2. Coche: gasolina, noGasolina, puertas, llantas, motor, timon

- los metodos son las acciones o estado de los objetos
ejemplo  
1. Persona: habla, corre, grita, mira, come, duerme, piensa
2. Coche: anda, frena, acelera, derrapa, gira, prende, apaga

### Concepto abstracto

- los objetos tienen atributos que se pueden definir al momento de inicializar un nuevo objeto o directamente en la instancia
- las clases pueden pueden tener variables de clase, variables de instancia, variables locales
- aunque Python no tiene el concepto de variables privadas integrado al lenguaje, es practica comun definirlas con un guion bajo
- ***isinstance*** y ***hasattr***

- los metodos son como funciones que tienen sentido unicamente en al contexto de una clase
- al igual que las variables, los metodos privados se definen con un guion bajo
- la ***encapsulacion*** es un concepto clave de la programacion orientada a objetos
	- la forma practica de aplicar este principio es declarar todas las variables y metodos como privados, a menos de que sea necesario exponerlos a otros programadores
- un metodo clave que casi todas las clases deben de teneres ***__init__***
- otro es ***__str__***
- existen varios tipos de metodos, estaticos, de clase, de instancia, getters y setters

***encapsulacion***
- basicamente es la complejidad que contiene al clase, para devolver el objeto o la accion  
ejemplo:  
- Computador: no nos preocupamos de como funciona, se activan los controladores, funete de alimentacion regulada, activar los perifericos, si no en prenderlo y empezar a trabajar con él

# Modelar un objeto
- las clases se declaran con mayuscula
- se usa PascalCase
- ```def __init__(self):``` debe de ir ya que es la propia instancia, es un metodo de instancia
- ```def __init__(class):``` metodos de clase con class
- ```__init__``` se conoce como el constructor de la clase, es el primer metodo que se ejecuta al instanciar la clase
- ```self._is_turned_on = false``` declaracion de la variable privada, se debe iniciar con guion bajo
- ```_LAMP = []``` una variable clase

### class
ejemplo: constructor, metodos publico, metodo privado
~~~
class Lamp():
	_LAMPS = ['''

			||| O N |||

	''',
	'''

			|| O F F ||

	''']


	# constructor
	def __ini__(self): 
		self._is_turned_on = False


	# prendido (metodos publicos)
	def turn_on(self):
		self._is_turned_on = True
		self._display_image()


	# apagado (metodos publicos)
	def turn_off(self):
		self._is_turned_on = False
		self._display_image()


	# estado (metodo privado)
	def _display_image(self):
		if self._is_turned_on:
			print(self._LAMPS[0])
		else:
			print(self._LAMPS[1])

def run():
	
	# instancia del objeto
	lamp = Lamp()

	while True:
		command = str(input('''
			Que quieres hacer: 

			[p] prender
			[a] apagar
			[s] salir

			=> '''))

		if command == 'p':
			lamp.turn_on()

		elif command == 'a':
			lamp.turn_off()

		elif command == 's':
			print('''
				
			||| chao |||

				''')
			break
		else:
			break

if __name__ == '__main__':
	run()
~~~

# Decoradores
- simplemente es una funcion que recibe otra funcion y retorna otra funcion
- se aplica con @
- super util para definir si una funcion debe ejecutarse o no
- en un servidor: existen funciones que se ejecutan si el usuario esta autenticado, o administrador

~~~
# -*- coding: utf-8 -*- 

def protected(func):

	def wrapper(password):
		
		if password == 'felixtomas':
			return func()
		else:
			print('no es la contraseña')

	return wrapper


@protected
def protected_func():
	print('Tu contraseña es correcta')


if __name__ == '__main__':
	
	password = str(input('Ingreso de contraseña: '))

	protected_func(password)
~~~

#### Lo que hace: 
- ejecuta la funcion que valida si el usuario puso la contraseña correcta
- si es asi podemos ejecutar la funcion protegida
- si no dara error y mostrara que no accede
- y sobre la funcion protegida
- hacemos el llamado de la funcion que valida con @
- es una funcion que se ejecuta antes de la funcion a ejecutar, filtrando su ejecucion e impidiendo que se ejecute

ejemplo como lo entendi
- es un portero de discoteca
- verifica si viene borracho, o solo y no lo deja pasar


# Paquetes y modulos
- la idea es modularizar el codigo
- permitiendo agrupar la funcionalidad comun en un solo archivo
- cuando varios modulos agrupan funcionalidades comunes, se pueden agrupar, a su vez en paquetes
- python reconoce qu un directorio es un paquete porque contiene un archivo llamado ``` __init__.py```

- vamos a dividir la funcionalidad de nuestro codigo lamparas
1. con la funcionalidad
2. con el punto de entrada, o logica de inicializacion

- se debe crear un archivo con la clase.py
- y se debe importar en el archivo de inicializacion del programa

#### De esta forma se importan las clases, al archivo principal
~~~
from nombreArchivo import Lamp, Foco
~~~

#### archivo principal
- contiene esta linea

- cuando python importa un modulo, siempre lo importa con el nombre del archivo
- exceptuando si el archivo es el punto de entrada
- lo que hace es verificar si el nombre del archivo es dunder main ```__main__```
- que seria el archivo principal, o punto de entrada que ejecuta python

~~~
if __name__ == '__main__':
	main()
~~~

> main.py

> class.py

# Entorno virtual de Python

- Manegador de paquetes pip (python package index)
- es un repositorio de paquetes de terceros
- python3.8
- pip 20.0.2 
- pip install nombre_paquete
- con requirement.txt ordenamos los paquetes que vamos a utilizar en nuestros proyectos

### Ambientes virtuales
- debemos crear un hambiente virtual por proyecto que se trabaje
- evitando conflictos de paquetes, en el interprete principal

***comandos para comprobar en consola***
- which pip (me dice el directorio de pip)
- pip freeze (muestra paquetes instalados en ese entorno virtual)

***comandos***
1. instalamos paquete virtualenv
```pip install virtualenv ```
2. creamos directorio del proyecto
```mkdir servidor```
3. creamos un ambiente virtual
```python3 -m venv venv```
4. activar el entorno virtual
```source venv/bin/activate```
5. salir del entorno virtual
```deactivate```

|libreria a instalar| 
|-|-|
| pip install flask | libreria |
| requirements.txt | guardar las versiones del proyecto |
| pip install -r requirements.txt | instalara las versiones almacenadas |

### levantemos un servidor web de Flask

> main.py

~~~
from flask import Flask 

app = Flask(__name__)



@app.route('/')
def hellow_world():
    return 'Hola, mundo desde Flask server'



if __name__ == '__main__':
    app.run()
~~~

- luego lo ejecutamos python3 main.py
- listo servidor en localhost:5000 

# Que es web Scraping
- permite obtener datos de los sitios web 
- las famosas arañas que copian los vinculos almacenandolos 
- vamos bajar imagenes de xkcd.com

# implemetar el scriper 
Buscar informacion de paginas, y atraves de funciones, podemos bajar  
imagenes archivos o los que se quiera, por lotes  
osea es bajar informacion de pagina

#### pasos para crear el entorno virtual
- creamos entorno virtual
- virtualenv env
- source venv/bin/activate
- dependencias 
	- requirements.txt
	- 1 requests
	- 2 beautifulsoup4

- lo que hace con estas libreria es hacer que con una funcion, captura los datos de una pagina, y se puede descargar cualquier cantidad de elementos, imagenes  

No hice el ejercicio, por que tocaba entenderlo primero

# Proyecto interfaz directorio de usuarios 
agenda telefonica

> contacts.py

- esta pendiente la logica de actualizar el contacto

# Persistencia de datos

- guardaremos los datos, y los almacenamos en disco en archivo.csv

> save_contacts.csv


___

De aqui en adelante es nube, template pug, y aplicar el proyecto en flask

Video 46 al 54 pendiente por ver

Vamos para python2020



