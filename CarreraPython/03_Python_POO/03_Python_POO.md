# Python POO

## Tipos de datos abstractos

- en python todo es un objeto y tiene un tipo
- representacion de datos y formas de interactuar con ellos

## Formas de interactuar con un objeto:

- creacion
- manipulacion
- destruccion

## ventajas
- descomposicion
- abstraccion
- encapsulacion

Sintaxis de tipo de datos abstractos
~~~
class Name_class(super_class):
	def __init__(self, param):
		expresion

	def nombre_del_metodo(self, param):
		expresion
~~~

1. class (keyword class, para definir la clase)
2. Name_class (nombre de la clase)
3. super_class (hace parte de la herencia)
4. ```__init__``` metodo constructor
5. ```self``` (todos los metodos llevan self)
6. parametros de inicializacion
7. expresion que puede estar vacia, o podemos inicializar nuestra clase
8. def se usa normalmente para funciones, pero dentro de las clases se usa como ***metodo de la clase***


Ejemplo: Persona
~~~
class Persona(object):

	# metodo constructor inicializa la clase
	def __init__(self, nombre, edad):

		self.nombre = nombre
		self.edad = edad


	# metodo saludar
	def saluda (self, otra_persona):
		return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'


david = Persona('David', 35)
erika = Persona('Erika', 25)

print(david.saluda(erika))
print(erika.saluda(david))
~~~

- como podemos ver la clase es un molde de caracteristicas de una persona  la cual cualquier instancia puede hacer uso de sus caracteristicas y metodos

## Instancias

- mientras la clase es un molde, a los objetos creados se les conoce como instancias
- cuando se crea una instancia, se ejecuta el metodo ```__init__```
- todos los metodos de una clase reciben implicitamente como primer parametro self

## los atributos de clase nos permiten

- representar datos
- procedimientos para interactuar con los mismos (métodos)
- macanismos para esconder la representacion interna

- se accede a los atributos con la notacion de punto
- puede tener atributos privados que comienzan con ***```_```***, en otros lenguajes se conoce como ***private***

~~~
class Coordenada():

  # metodo constructor inicializa la clase
  def __init__(self, x, y):

    self.x = x
    self.y = y


  # metodo distancia
  def distancia(self, otra_cordenada):

    x_diff = (self.x - otra_cordenada.x)**2
    y_diff = (self.y - otra_cordenada.y)**2

    return (x_diff + y_diff)**0.5


def run():
  # instancias de la clase
  cordenada_1 = Coordenada(3, 30)
  cordenada_2 = Coordenada(4, 8)

  # 22.02271554554524
  # print(cordenada_1.distancia(cordenada_2)) 

  # para ver si una instancia pertenece a una clase
  print( isinstance(cordenada_2, Coordenada) ) # True


if __name__ == '__main__':
  run()
~~~

- isinstance nos confirma si la instancia pertenece a una clase
- con .metodo accedemos a los metodos de la instancia de la clase

## Decomposición
Video 3




