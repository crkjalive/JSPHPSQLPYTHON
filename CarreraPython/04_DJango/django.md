# Django avanzado requiere
[T] python, terminal, POO, bash scripting, pipes
[-] modelo cliente servidor, protocolosinternet y http
[-] fundamentos de ingenieria de software, y desarrollo web
[-] Django, HtypResponse, HttpRequest, haber concluido 3 o mas proyectos
[-] class-based views y curso Django, herencias de clases
[x] Docker, contenedores, imagenes, volumenes, DockerCompose, Curso de Docker
proyecto Comparte Ride (comparte el uso del carro)

___

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


### Instalamos Django en su ultima version
- pip install django -U

#### Miramos que instalo Django
- pip freeze 
~~~
asgiref==3.4.1
django==3.2.6
pytz==2021.1
sqlparse==0.4.1
~~~

## Creacion del proyecto platzigram
comandos Django para empezar

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
	- una interface sobre Django admin

2. ```__init__.py```
	- objetivo de este archivo es declarar platzigram como modulo de python
	- archivo vacio

3. urls.py
	- archivo de entrada para todas las peticiones en Django
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

#### las aplicaciones ligadas a Django son
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
1. color verde Django 19865C
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
Lo que hace Django
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
- content_type="application/json", le dice a Django que es json nuestra respuesta
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
- con Django creamos rutas, el las urls
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
- el template system de Django, es una menera de presentar los datos usando HTML
- tiene similitud en en la sintaxsys de ninja2  

#### Estructura
- urls.py (encargada de hacer match con la rutas y las views haciendo la relacion)
- views.py (encargado de la logica de encontrar los datos y entregalo a las vistas)
- template (seria la logica de presentar los datos)

### templates de Django
- la configuracion de los templates se encuentra en ***settings.py*** en la parte de TEMPLATES
- para hacer uso de los templates de Django, debemos crear nuestra carpeta de templates en la carpeta de los posts
- dentro de esta carpeta vamos a contener nuestro html
- que se renderizaran con el modulo render
~~~
from django.shortcuts import render 
~~~
- para entregar este archivo .html, debemos en la funcion
~~~
return render(request, 'feed.html')
~~~
- el render recibe 2 argumentos, el html y un contexto
- que simplemente son diccionarios {'name':'wizard'}
~~~
return render(request, 'feed.html', {'name':'wizard'})
~~~
- como mostramos este diccionario
- con dobles brackets {{}}, en el feed.html que renderizara, la variable name de nuestro diccionario
~~~
{{ name }}
~~~

#### Vamos a insertar datos de nuestro objeto json
- entregamos datos de nuestro objeto json ***posts***
~~~
return render(request, 'feed.html', {'posts': posts})
~~~
- nuestro render tiene logica de programación
- lo cual mostraremos con lenguaje python nuestros datos en el html
- for in de posts
~~~
{% for post in posts %}
	<p> {{ post.title }} </p>
{% endfor %}
~~~
- se debe abrir y cerrar los for o if, entre brackets y porcentajes
- manjeamos la iteracion dentro de etiquetas html, y le insertamos la iteracion, y la llave de nuestro objeto
- aqui se abre la mente y se entiende como trabajamos con los templates systems de Django

#### ahora vamos a htmliar
- vamos a dar estilos con Bootstrap
- aprovechando para aprender Bootstrap
- como es html, creamos una estructura basica de html
- manejamos stilos de bootstrap, informacion en bootstrap.md, la linkeamos a nuestro feed
~~~
<!-- CSS only -->
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
~~~
- Codigo de los post basico hasta el momento con Bootstrap
~~~
<div class="container">
	<div class="row">
		{% for post in posts %}
			<div class="col-lg-4 offset-lg-4">
				<div class="media">
					<img class="mt-3 rounded-circle" src=" {{ post.user.picture }} " alt=" {{ post.user.name }}">
					<div class="media-body">
						<H5 class="mt-0"> {{ post.user.name }} </H5> 
						{{post.timestamp}}
					</div>
				</div>
				<img class="img-fluid mt-3 border rounded" src="{{ post.photo }}" alt=" {{ post.user.name }} ">
				<h6 class="ml-1 mt-1"> {{ post.title }} </h6>
			</div>
		{% endfor %}
	</div>
</div>
~~~
- de esta forma es como insertamos python en html, atraves de template system
- estamos trayendo imagenes random

## Patrones de diseño
- tenemos codigo mezclado de html, python
- patrones de diseño: consiste en solucionar estos problemas, separando la logica de la presentacion y del modelo de datos

### MVC (Model, View, Controller)
separando:
1. Model 
	- datos 
2. View 
	- presentacion datos al usuario
3. Controller
	- logica (valida, controla las rutas, cambia datos)  

este patron de diseño es el implementado en la mayoria de lenguajes

### MTV (Model, Template, Controller)
Django implementa el MTV

1. Model
	- Define la estructura de los datos
	- igual al ***modelo del MVC***
2. Template
	- Logica de presentacion de datos
	- equivalente al ***View*** entrega las vistas al usuario
3. View
	- Encargado de traer los datos y pasarlos al template
	- equivalente al ***controller***, que maneja la logica de las url

## La M en el MTV 
modelo

formas de conectarnos a una base de datos con Django  
bases de datos con las que nos podemos conectar  
compatibilidad con ***postgress***, ***MySQL***, ***Oracle***  
default ***sqlite3***  


Configuracion es ***settings.py*** aqui tenemos toda la configuracion del proyecto  
***DATABASES*** en esta variable cargamos la configuracion de nuestra base de datos  

***ENGINE***  
- especifica el motor de la base de datos con la que estamos trabajando  
1. 'django.db.backends.postgresql'
2. 'django.db.backends.mysql'
3. 'django.db.backends.sqltile3'
4. 'django.db.backends.oracle'

ejemplo en la documentacion de Django
~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
~~~

#### Migrations
- debemos migrar las configuraciones para poder trabajar con las bases de datos

> ```python3 manage.py migrate```

- esto instala o compacta todos los paquetes de Django desconectados en el proyecto

Aplica  
Apply all migrations: admin, auth, contenttypes, sessions
- esta aplicacion creo unas tablas en sqlite3
- que vamos a inspeccionar con dbBrowser
- estas tablas son distintas dependiendo de el engine que vallamos a usar
- esto Django las ataca con una tecnica ***ORM*** (Object Relation a Mapper)
- la tecnica para trabajar con multiples sistemas 
- que es una abstraccion de POO atraves de clases de Python, para el manejo de  
los diferentes motores de DB (mysql, postgres, oracle), que nos permiten la interaccion
- para definir la estructura

#### modelo de usuarios
- vamos a crear un modelo para el manejo de usuarios
- atraves de una clase manejamos la creacion una tabla
- referencia de los field para crera las tablas desde Django
- https://docs.djangoproject.com/en/3.2/ref/models/fields/
- todas las opciones para ponerle el tipo de campo en la base de datos
- osea la codificacion de cada campo

Modelo class User
~~~
from django.db import models

# Create your models here.

class User (models.Model):
	"""Modelo de Usuario"""

	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	is_admin = models.BooleanField(default=False)

	bio = models.TextField(blank=True)

	birthdate = models.DateField(blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
~~~
- de esta forma creamos una tabla

#### Detalle de la clase
1. unique=True (campo unico)
2. max_length=100 (varchar 100, maximo de caracteres)
3. CharField (caracter)
4. blank=True (pemite esta campo en blanco)
5. null=True (permite que este nulo este campo)
6. auto_now_add (estampa la fecha de creacion)
7. auto_now (estampa la fecha de actualizacion)
8. BooleanField (va a ser booleano)
9. default=False (dar valor por defecto)


#### debemos migrar la tabla para que reciba los cambios
***makemigrations***, ***migrate***

- comando para alterar la tabla

> ```python3 manage.py makemigrations```


> ```python3 manage.py migrate```

- esto altera la base de datos agregando el modelo User
- en migrations podemos encontrar el archivo 0001_initial.py
- con toda la configuracion que hizo
- actualizamos la migracion, sin errores
- Django ya agrega un id

~~~
# Generated by Django 3.2.6 on 2021-08-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
~~~

#### SQLite3
- instalacion de sqlitebrowser

> ```sudo apt-get install sqlitebrowser```

- vamos a ver con sqlitebrowser, que campos realmente tenemos en sqlite3

| Tabla | posts_user | - | - | - |
|-|-|-|-|-|
| id | integer | NOT NULL | PRIMARY KEY | AUTOINCREMENT |   
| email | varchar(254) | NOT NULL | UNIQUE ||
| password | varchar(100) | NOT NULL |||
| first_name | varchar(100) | NOT NULL |||
| last_name | varchar(100) | NOT NULL |||
| bio | text | NOT NULL |||
| birthdate| date ||||
| created | datetime | NOT NULL |||   
| modified | datetime | NOT NULL ||| 
| is_admin | bool | NOT NULL |||   


## El ORM de Django
- como insertar datos
- hacer consultas
- hacer filtros

#### vamos abrir el shell de Django
- ya que el shell de python asi lo abramos para trabajar desde consola, no tiene el proyecto cargado

> ```python3 manage.py shell```

- con este comando podemos interactuar con la shell de python y Django cargado
- debemos entender que Django esta basado en objetos, 
- debemos crear objetos instanciando la clase de user

#### interactuemos con el shell, grabando datos

importamos de posts el models User, para trabajar en el shell
~~~
from posts.models import User
~~~

#### creemos un usuario con objects.create,  la clase User (create)
~~~
wizard = User.objects.create(
...     email='wizard@wizard.com',
...     password='123456',
...     first_name='Wizard',
...     last_name='Deejay'
... )
~~~
- para confirmar los datos, accedemos como se acceden  
a los objetos normalmente
- objeto.propiedad

#### Miremos 
| nombre | apellido | email | id | is_admin |
|-|-|-|-|-|
| wizard.first_name | wizard.last_name | wizard.email | wizard.id ||
|'Wizard' | 'Deejay' | 'wizard@wizard.com' | 1 ||
| jared.first_name | jared.last_name | jared.email | jared.id ||
| 'Jared' | 'KenJar' | 'jared@jared.com' | 2 | True = 1 |


#### Editando Valores
chanchito.email = 'lalala@lalala.com'

#### guardando los cambios en la tabla
chanchito.save()

#### revizando datos
chanchito.created
chanchito.modified

## creemos un usuario instanciando la clase
teresita = User()  
teresita.first_name = "Teresita"  
teresita.last_name = "Ramos"  
teresita.email = "tere@tere.com"  
teresita.password = 963.8520  
teresita.is_admin=True  
teresita.id  

#### guardar en la base de datos .save()
teresita.save()  

- mucho mas facil y directo a la propiedad de la clase
- con .save() se guarda el objeto en la base de datos
- teresita.id confirmamos que esta greado el objeto User

#### diferencia 0 
~~~
from posts.models import User

for user in users:
	
	obj = User.objects.create(**user) # así crea y guarda directamente
	
	print(obj.pk)
~~~

#### es lo mismo que
~~~
from posts.models import User

for user in users:
	
	obj = User(**user) # asi crea 
	obj.save() # así guarda

	print(obj.pk)
~~~

#### borrar de la base de datos .delete()
teresita.delete()
chanchito.delete()

#### agregar desde un script

> ```data_script_list.py```

- podemos insertar datos copiados desde un script  
- debemos importar la libreria date, para que reconozca la fecha de cumpleños  
- debemos importar la libreria del objeto


### Querys
- mostrar los datos almacenados en la base de datos

#### carguemos un usuario .get
- trae un solo elemento
- asi que debemos hacer la consulta, por un dato especifico
~~~
user = User.objects.get(email='jared@jared.com')
user
User: User object (8)>
type(user)
<class 'posts.models.User'>
user.pk
8
user.email
'jared@jared.com'
user.first_name
'Jared'
user.last_name
'Latorre'
user.password
'74108520'
~~~

#### carguemos los que conincidan .filter
- vamos a traer varios usuarios
- es como en like de sql, 
- que conincida algo o parte de algo
~~~
gmail_email = User.objects.filter(email__endswith='@gmail.com')
~~~
- devuelve una lista de User Object 
~~~
<User: User object (13)>
~~~
- cambiemos a que nos muestre por correo
- agregamos al modelo de la tabla  
~~~
def __str__(self):
	"""Return email"""
	return self.email
~~~
- ya al volver hacer la consulta nos muestra por email
~~~
from posts.models import User
>>> gmail_email = User.objects.filter(email__endswith='@gmail.com')
>>> gmail_email
<QuerySet [<User: masha@gmail.com>, <User: marcos@gmail.com>, <User: lucas@gmail.com>, 
<User: paco@gmail.com>, <User: luis@gmail.com>, <User: hugo@gmail.com>, 
<User: lisa@gmail.com>, <User: marge@gmail.com>]>
~~~

#### consulta de todos los usuarios .all
- trae todos los usuarios  
users = User.objects.all()  
users

- usuarios que trajo, solo muestra los email
~~~
<QuerySet [<User: wizard@wizard.com>, <User: jared@jared.com>, <User: ken@ken.com>, 
<User: linda@lin.com>, <User: tere@tere.com>, <User: masha@gmail.com>, 
<User: marcos@gmail.com>, <User: lucas@gmail.com>, <User: paco@gmail.com>, 
<User: luis@gmail.com>, <User: hugo@gmail.com>, <User: lisa@gmail.com>, 
<User: marge@gmail.com>]>
~~~

#### cambiemos datos por lotes .update
- consulta  
gmail_email = User.objects.filter(email__endswith='@gmail.com')
- actualizacion  
gmail_email = User.objects.filter(email__endswith='@gmail.com').update(is_admin=0) # 1 True 0 False

| tabla de querys disponibles |-|-|
|-|-|-|
| filter(**args) | devulve todos los objetos que hacen match con los argumentos ||
| exclude(**args) | devulve objetos que NO hagan match con los parametros ||
| .all() | devulve todos los registros ||
| .update() | actualiza los datos del objeto u objetos que hacen match ||
| .get() | trae 1 objeto | clase.objects.get(pk=1) |
|  .all()[:5] | trae los ultimos 5 objetos | [-1] no soportado |
| order_by | .order_by('headline')[0:1].get() ||

#### comparacion query SQL y Django

-SQL
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';  

- Django
Entry.objects.filter(pub_date__lte='2006-01-01')  

- filter hace la funcion del where

### Reto
1. crear campo de country
2. crear registros
3. hacer consultas

## extendiendo el modelo de usuario Auth_user
- vamos a crear un usuario de los definidos por Django
- auth_user
- esto valida nuestro nuevo usuario
- y encripta el password del usuario
- este usuario se crea en la tabla auth_user, predefinidas en Django

#### creemos el usuario
~~~
from django.contrib.auth.models import User

u = User.objects.create_user(username='yesika',password='admin123')
~~~
#### miremos la tabla que nos entrega y el registro

|id|password|last_login|is_superuser|username|last_name|email|is_staff|is_active|date_joined|first_name|
|-|-|-|-|-|-|-|-|-|-|-|-|
|1|pbkdf2|null|0|yesica|null|null|0|1|2021-08-16 00:50:03.182990|null|

#### comprobemos como encripta la contraseña
> u
<User: yesika>
u.pk  
1  
u.username  
'yesika'  
u.password  
'pbkdf2_sha256$260000'  

- este modelo que nos da Django, esta casi completo
- faltaria mas campos como img, pais, website, vaiod, picture
- son cosas que debemos implementar para extender el modelo

#### crear un superuser
> python3 manage.py createsuperuser  

Username (leave blank to use 'crkj'):   
Email address: 0soundlive@gmail.com  
Password:   
Password (again):  

|id|password|last_login|is_superuser|username|last_name|email|is_staff|is_active|date_joined|first_name|
|-|-|-|-|-|-|-|-|-|-|-|-|
|2|pbkdf2_sha256$260000||1|crkj||0soundlive@gmail.com|1|1|2021-08-16 01:17:01.975653||


#### levantemos el servidor para ver el superuser
- esto es registrando la ruta admin, nuevamente en las urls
- localhost:8000/admin
- aqui administramos

~~~
from django.contrib import admin

path('admin/', admin.site.urls),
~~~

- levantamos la administracion de Django

### AUTHENTICATION AND AUTHORIZATION
1. Groups
2. Users

- en este modulo podemos ver los usurios de la tabla registrados
- podemos ver los datos de cada usuario
- apartir de aqui, ya Django nos muestra que no hay necesidad de crear nada
- todo lo hacemos desde el administrador de Django
- asi ya todo viene validado, y ajustado a las necesidades del proyecto

___

Nos hemos dado cuenta de que todo lo que hicimos de manera manual, ya Django nos lo da  
y solo era para ver como se hacia, y como es que funciona, borremos toda esa informacion  
que se conbierte en fallos para la seguridad de Django  
ya que Django mantiene validada es información, rutas e informacion segura  
ya que podriamos exponer informacion de los usuarios

___

Borremos
1. models (informacion no archivo)
~~~
from django.db import models


# Create your models here.

class User (models.Model):
	"""Modelo de Usuario"""

	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	is_admin = models.BooleanField(default=False)

	bio = models.TextField(blank=True)

	birthdate = models.DateField(blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return email"""
		return self.email
~~~
2. las migraciones sin borrar el ```__init__```
3. y la base de datos sqlite3, ya que es un archivo
```rm db.sqlite3```

- hasta aquí fue lo aprendido, empezamos de nuevo, de la forma correcta
___


## Implementación del modelo de usuarios de Clonestagram


























