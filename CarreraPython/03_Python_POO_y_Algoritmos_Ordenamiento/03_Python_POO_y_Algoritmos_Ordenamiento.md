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
class NameClass(superClass):
	def __init__(self, param):
		expresion

	def nombre_del_metodo(self, param):
		expresion
~~~

1. class (keyword class, para definir la clase)
2. NameClass (nombre de la clase)
3. superClass (hace parte de la herencia)
4. ```__init__```metodo constructor
5. ```self``` (todos los metodos llevan self)
6. parametros de inicializacion
7. expresion que puede estar vacia, o podemos inicializar nuestra clase
8. def se usa normalmente para funciones, pero dentro de las clases se usa como ***metodo de la clase***


Ejemplo: class Persona

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
- puede tener atributos privados que comienzan con ***```_```***, en otros lenguajes se hace con ***private***

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

> ```class_Coordenada.py```

- isinstance nos confirma si la instancia pertenece a una clase
- con .metodo accedemos a los metodos de la instancia de la clase

## Decomposición
- partir un problema en problemas mas pequeños
- las clases permiten crear mayores abstracciones 
- cada clase se encarga de una parte del problema y el programa se vuelve mas facil de mantener

> ```decomposicion.py```

- que otros componentes podria tener nuestro carro

## Abstraccion
- enfocarnos en la informacion importante 
- separar la informacion central de los detalles secundarios
- podemos utilizar variables y metodos (privados o publicos)

- como podemos interactuar con estas clases 
- generando una interface

> ```abstraccion.py```

- Se hace ejemplo del ciclo de una lavadora
- con el proposito de entender como todo son objetos
- y como podemos entender la abstraccion de cada objeto en la vida real 

## Encapsulacion (getters and setters)
- permite agrupar datos y su comportamiento
- controla el acceso a dichos datos
- previene modificaciones no autorizadas (defencing programming)

> ```encapsulacion.py```

- se implementan los getter con la propiedad @propierty
- con el decorador @region.setter se setean los setters
- estos metodos de proteccion de accesos no autorizados, nos mantienen segura  
nuestra aplicacion

## Herencia 
- la herencia nos permite modelar una jerarquia de clases
- permite compartir comportamiento comun en una jerarquia
- al padre se le conoce como superclase y al hijo como subclase

- a su vez cada nueva clase hereda de su padre las propiedades y metodos de la clase  

> ```herencia.py```

- la herencia de una superclase se hereda en python en la supreclase
- para que herede de clase se pasa por parametro clase padre
- y se inicializa con super, para llamar los metodos de la clase que hereda
- 

## Polimorfismo
- es la habilidad de tomar varias formas
- en Python, nos permite cambiar el comportamiento de   
una superclase para adaptarlo a la subclase.

> ```polimorfismo.py```

- en el polimorfismo su comportamiento cambia el metodo, ya que son metodos de clases distintas
- pero heredan de la clase principal todos sus metodos

___

# Comparación de algoritmos

## Introducción a la complejidad algorítmica
- Proque comparamos la eficiencia de un algoritmo
- complejidad temporal vs complejidad espacial
- podemos definirla como T(n)

Aproximaciones
- cronometrar el tiempo en el que corre un algoritmo (atraves de un reloj)
- contar los pasos con una medida abstracta de operación (atraves de un contador)
- contar los pasos conforme nos aproximamos al infinito (medida asintotica)

> ```complejidad_algoritmica_tiempo.py```

## conteo abstracto de operación

- lo importante es ver en esta ecuacion que tan grande se puede volver nuestro polinomio

> ```complejidad_algoritmica_polinomio.py```

## Notación asintótica o Crecimiento asintotico
- no importa variaciones pequeñas (si nos vamos al infinito)
- el enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito
- mejor de los casos, promedio, peor de los casos
- Big O notation
- nada más importa el término de mayor tamaño

## Ley de la suma

#### crecimiento lineal

~~~
# crecimiento lineal
def f(n):

    for i in range(n):
        print(i)

    for i in range(n):
        print(i)
~~~

- O(n) + O(n) = O(n+n) = O(2n) = O(n) 
- esta funcion tiene un crecimiento lineal
- en O de n

~~~
# crecimiento cuadratica
def f(n):

    for i in range(n):
        print(i)

    for i in range(n*n):
        print(i)
~~~

- O(n) + O(n*n) = O(n+n2) = O(n2)
- en O de n al cuadrado

> ```complejidad_algoritmica_polinomio.py```

## Ley de la multiplicacion

#### crecimiento cuadratico

~~~
def f(n):

    for i in range(n):
        for j in range(n):
            print(i,j)

f(3)
~~~
- O(n) * O(n) = O(n*n) = O(n2)
- esta funcion tiene un crecimiento cuadratico
- en O de n al cuadrado
- loop dentro de otro loop, normalmente es una funcion cuadratica
- si hay un solo loop, es de crecimiento lineal


## recursividad múltiple

#### crecimiento exponencial 
~~~
def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# O(2**n)
~~~

de esta manera pudimos ver estas tres formas de medir nuestro algoritmo
- crecimiento lineal (O de n)
- crecimiento cuadratico (O de n2)
- crecimiento exponencial (O de n * n)

## Busqueda lineal
- algoritmos de busqueda y ordenación
- buscar en todos los elementos de manera secuencial

#### numero aleatorio entre 0 y 100
```random.randint(0,100)```

#### Operador ternario
- if else en una misma linea
```print(f'El elemento {objetivo} {"esta" if encontrado} else "no esta"} en la lista')```

#### este algoritmo de busqueda lineal en una lista nos asegura si esta o no el elemento a buscar

- la complejidad algoritmica de este algoritmo es un O(n)
- puesto que el elemento mas importante es el loop for in, ya que depende de la longitud de la lista
- y esto nos dira que tan grande ira creciendo nuestro algoritmo

> ```busqueda_lineal.py```

~~~
import random

def busqueda_lineal(lista, objetivo):
    match = False 

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match


if __name__ == '__main__':
    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    
    #print(lista)

    objetivo = int(input('que número quieres encontrar? '))

    
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
~~~

## Ordenamiento de burbuja
- algoritmo de ordenación
- este algoritmo lo que hace es comparar un dato contra otro dato adyacente
- dependiendo si es mayor o menor, lo ordenara cambiando su posicion en la lista
- esto se repetira hasta que queda completamente ordenada la lista

> ```ordenamiento_burbuja.py```

~~~
import random

def ordenamiento_burbuja(lista):

    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):

            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
    
    return lista


if __name__ == '__main__':

    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    print(lista)
 
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)

~~~

- la complejidad algoritmica de este metodo de ordenamiento 
- seria de n veces por cada elemento de la lista
- crecimiento cuadratico, polinomineal
- ```O(n) * O(n) = O(n * n) = O(n**2)```


#### proceso interno
~~~
[62, 62, 54, 89, 67, 94, 4]
[62, 54, 62, 89, 67, 94, 4]
[62, 54, 62, 67, 89, 94, 4]
[62, 54, 62, 67, 89, 4, 94]
[54, 62, 62, 67, 89, 4, 94]
[54, 62, 62, 67, 4, 89, 94]
[54, 62, 62, 4, 67, 89, 94]
[54, 62, 4, 62, 67, 89, 94]
[54, 4, 62, 62, 67, 89, 94]
[4, 54, 62, 62, 67, 89, 94]
[4, 54, 62, 62, 67, 89, 94]
~~~

- este algoritmo no es tan optimo para listas grandes

## Ordenamiento por insercion
- consiste en ir almacenando en memoria 
- cada valor en de la lista, mientra va comparando si el siguiente valor es mayor o menor
- agregandolo a su derecha o izquierda
- ideal para listas pequeñas
- para listas grandes no es lo mas optimo, ya que requiere mucha memoria
- para poder ordenan la lista, ya que toda la operacion es sobre la ram

~~~
import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            lista[posicion_actual] = valor_actual

    return lista


if __name__ == '__main__':

    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    print(lista)
 
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)
~~~
#### secuencia generada
~~~
[78, 5, 19, 96, 34]
[5, 19, 34, 78, 96]
~~~

## Ordenamiento por mezcla
- merge sort en ingles
- usa la estrategia de divide y conquista
- divide la lista en sublistas, cada vez mas pequeñas
- de 1 ó 0 elementos, y luego las compara entre si armando nuevamente la lista ordenada
- agregando en el codigo a la derecha el valor mayor y a la izquierda el valor menor

~~~
import random

def ordenamiento_por_mezcla(lista):

    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(f"izquierda {izquierda}-{derecha} derecha")
        print("*"*35)
    
        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # iteradores de sublistas
        i = 0
        j = 0
        # iterador de lista principal
        k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1
            k+=1


        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1 
        
        #print(f"{izquierda}-{derecha}")
        print(f"Izquierda {izquierda}-{derecha} Derecha")
        print(f"lista armada {lista}")
        print('*'*35)

    return lista



if __name__ == '__main__':

    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    print(f"lista a ordenar {lista}")
 
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(f"lista finalmente ordenada {lista_ordenada}")
~~~

> ```ordenamiento_merge_sort.py```

## Ambientes virtuales
- permiten aislar el ambiente para poder instalar diversas versiones de paquetes
- a partir de python 3 se incluye en la libreria estandar en el modulo venv
- ningun ingeniero profesional de python trabaja sin ellos

#### pip (tienda)
- permite descargar paquetes de terceros para utilizar en nuestro programa
- permite compartir nuestros paquetes con terceros
- permite especificar la version del paquete que necesitamos
- pypip (tienda virtual)

graficado/
python3.9 -m venv venv
source venv/bin/activate
deactivate

pip install bokeh
pip freeze
 

## el problema del morrar
- algoritmo codicioso

~~~
def morral(tamano_morral, pesos, valores, n):

    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1)

    return max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos, valores, n-1), morral(tamano_morral, pesos, valores, n-1))

if __name__ == '__main__':
    valores = [60,100,120]
    pesos = [10, 20, 30]
    tamano_morral = 30 # cambiamos para ver que nos cabe
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
~~~

> ```morral.py```

- con estos algoritmos ya podemos saber donde implementarlos, como computer science

## Conclusiones
1. los tipos de abstractos (clases) permiten crear programas poderosos que modelan al mundo
2. podemos medir la eficiencia de diversos algoritmos
3. las graficas nos permiten encontrar patrones rapidamente
4. optimizacion

#### Habilidades del pensamiento computacional desarrollado
1. Decomposicion (division en problemas)
2. Abstraccion
3. Reconocimiento de patrones
4. Diseño de algoritmos

