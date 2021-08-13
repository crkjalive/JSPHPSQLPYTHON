# Django 
- Vamos a crear un platzigram 
curso del 2018

Objetivos de Django
1. mantener sitios grandes
2. crear sitios rapidamente 
3. precargado con muchas herramientas
4. seguridad
5. escalabilidad
6. versatil (mucho tipo de proyectos)
7. DRY (dont repeat yourself)

## Entorno de trabajo
python3 pip3 

1. crear venv ***(python3 -m venv venv)***
2. activamos el entorno ***(source env/bin/activate)***
3. .venv (podemos dejar oculto nuestro directorio)

- hemos creado nuestro entorno virtual fuera de nuestro proyecto  
platzigram/  
venv/  

desde platzigram activamos el entorno virtual  
***source ../venv/bin/activate***


### Instalamos django en su ultima version
- pip install django -U

#### Miramos que instalo django
- pip freeze 
~~~
asgiref==3.4.1
Django==3.2.6
pytz==2021.1
sqlparse==0.4.1
~~~

## Creacion del proyecto platzigram
comandos django para empezar

1. django-admin
~~~
check
compilemessages
createcachetable
dbshell
diffsettings
dumpdata
flush
inspectdb
loaddata
makemessages
makemigrations
migrate
runserver
sendtestemail
shell
showmigrations
sqlflush
sqlmigrate
sqlsequencereset
squashmigrations
startapp
startproject
test
testserver
~~~
- inicialicemos un proyecto
django-admin startproject platzigram .

# creacion de proyecto 
que compone nuestro proyecto?
1. /manage.py
	- una interface sobre django admin

2. ```__init__.py```
	- objetivo de este archivo es declarar platzigram como modulo de python
	- archivo vacio

3. urls.py
	- archivo de entrada para todas las peticiones en django
	- busca las vistas correspondientes

4. wsgi.pi
	- archivo usado durante el deployment en produccion
	- y es la interface, cuando el proyecto esta corriendo en produccion

5. settings.py
	- define todas las configuraciones del proyecto

#### settings.py
1. links a la documentacion
2. ***BASE_DIR*** linea que declara el lugar donde se esta corriendo el proyecto
3. ***SECRET_KEY*** usado para el hashing de las contraseñas, y de las sesiones que se almacenan en la base de datos
4. ***DEBUG*** nos dice que el proyecto esta en desarrollo, debe estar en ***False*** cuando pase a ***produccion***
5. ***INSTALL_APPS*** nos dice que aplicaciones estan ligadas al proyecto
6. ***ROOT_URLCONF*** modulo de entrada url
7. ***DATABASES*** default ya nos trae sqlite3
	- aqui cambiamos a la configuracion de base de datos
	- postgress, mysql, oracle
8. ***STATIC_URL*** archivos staticos (CSS, Javascript, Images)

#### las aplicaciones ligadas a django son
.admin  
.auth  
.contenttypes  
.sessions  
.messages  
.staticfiles  

#### ```AUTH_PASSWORD_VALIDATORS``` 
***auth*** trae un validador de contraseñas que valida que:
- que lo valores de la contraseña no sea similares al usuario
- minima longitud de caracteres
- valida la contraseña contra un diccionario de contraseñas comunes
- y que la contraseña no sea numerica

#### manage.py
output -> python3 manage.py

comandos de operaciones de:
1. django
2. contenttypes
3. auth
4. sessions
5. staticfiles

___

### runserver

> python3 manage.py runserver

1. levantamos el servidor
2. nos muestra que estamos en modo desarrollo ***DEBUG=True***

#### inspeccion
1. color verder django 19865C
2. estructura
	- header grid
		- grid-template-columns: auto auto;
	- main
		- svg
		- h1
		- p
	- footer
		- grid
			- left:50%
			- transform:translateX(-50%)

## Hello World

~~~
from django.urls import path
from django.http import HttpResponse

def hellow_world(request):
    return HttpResponse("Hola Mundo, Django")


urlpatterns = [
    path('hellow-world', hellow_world),
] 
~~~
Lo que hace django
1. crear rutas url para nuestro proyecto
2. path recibe la ruta, y la funcion
3. la funcion no retorna una respuesta HttpResponse

## El Objeto Request
separamos el codigo  
urls.py  
views.py  

en el archivo urls.py, se crean las rutas  
en el archivo views.py, se crean las vistas (lo que ve el cliente)

## debugging
import pdb; pdb.set_trace()  
esta linea la ponemos donde querramos detener la ejecucion del programa  
para ver que esta pasando  

### urlpatters
- aqui va la lista de path, que cada una es una url del sitio

## Ordenar numeros pasados por la url (GET)
- pasando argumentos url
- responder JSON

Vamos a pasar numeros por url
http://127.0.0.1:8000/hi/?numbers=1,9,3,15,12

~~~
def hi(request):
    numbers = request.GET['numbers']
    return HttpResponse(f'Hi! care monda {str(numbers)}')
~~~

#### convirtamos nuestro array de numeros pasado por url
estos lo revizamos en terminal con el debugging Pdb  
pasamos la variable  
~~~
(Pdb) numbers
'1,9,3,15,12'
(Pdb) numbers.split(',')
['1', '9', '3', '15', '12']
(Pdb) [int(i) for i in numbers.split(',') ]
[1, 9, 3, 15, 12]
~~~

#### implementemos 
list comprehensions  
para comvertir nuestro estring a una lista de numeros  
luego la ordenamos
~~~
numbers = [ int(i) for i in request.GET['numbers'].split(',') ]
sorted_ints = sorted(numbers)
~~~

#### mostremos los datos en json ordenados
de esta forma agregamos información a nuestros json visualmente  
y hasta nuestro saludo costeño  
~~~
data = {
        'hi': "Hola care monda",
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully' 
    }
~~~

#### mostremos el json
- json.dumps(data), convierte a estring nuestro json
- para poderlo ver sobre el html
- content_type="application/json", le dice a django que es json nuestra respuesta
- convirtiendo en texto plano nuestro json
~~~
return HttpResponse( json.dumps(data), content_type="application/json" )
~~~

#### comentario
- ahora le podemos pasar cualquier numero a nuestra variable get y automaticamente se cargan en la pagina de nuestra app
- todo esto para ver las formas de como pasar argumentos url get

#### otra forma de pasar datos
- pasamos datos por la url
- convirtiendo directamente el tipo de dato que es en el path de nuestra url  
~~~
path('hi/<str:name>/<int:age>/', views.hi),
~~~

- recibe name como string, y age como entero
- teniamos la funcion con un nombre distinto por eso debemos poner la funcion con el mismo nombre/var/var, para que concuerde la ruta

~~~
def hi(request, name, age):
    
    if age > 14:
        message = f'<h2>Bienvenido a Platzigram</h2><p>Hola {name}, {age}</p><h4>recibiendo nombre y edad por get</h4>'
    else:
        message = f'Sorry {name} {age} no puede estar aquí'

    return HttpResponse(message)
~~~

#### conclusiones
- con django creamos rutas, el las urls
- en la views.py creamos las funciones con la respuesta que return HttpResponse(message)
- se valida los datos en la funcion para mostrar

___


# Creacion Nuevo Proyecto

- arrancamos nuevo proyecto

> django-admin startproject clonestagram . 

- corramos el servidor

> python3 manage.py runserver

- perfecto, se manega con manage.py y con python3

#### crearemos nuestra primera app

> python3 manage.py startapp posts

- esta app es como un modulo independiente de la aplicación, y se maneja como app
- de esta forma tiene garantizado la estabilidad de los componentes
- aprendimos a entregar views HTML de un objeto json
- estas vistas entregan la informacion de la misma manera que las veniamos haciendo
- toca es repasar la forma en que importamos los modulos para que no se corten las rutas del modulo

Vista basica en HTMl
~~~
path('posts', posts_views.list_posts),
~~~

list posts
~~~
def list_posts(request):

	""" List existings posts """
	content = []
	for post in posts:
		content.append("""
			<h1>Hola care monda</h1>
			<h3><strong>{name}</strong></h3>
			<p><small>{user} - <i>{timestamp}</i></small></p>
			<figure><img src="{picture}"/></figure>
			""".format(**post))

	return HttpResponse("<br>".join(content))
~~~

## Introducción al Template System
video 9