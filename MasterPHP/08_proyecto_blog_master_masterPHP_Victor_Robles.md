# PHP y SQL
1. Conexion a MySQL
2. Consultas
3. Insertar datos
4. proyecto

# base de datos NOTAS 
1. id int auto_increment, primary key
2. titulo varchar(255)
3. descripcion mediumtext
4. color varchar(255)

# Orden del sitio
1. maquetar la web
2. hecer el registro de usuarios en el sidebar
3. hacer el login de usuarios en el sidebar
4. pagina edicion de datos de los usuarios
5. seccion de creacion de categorias
6. seccion de creacion de entradas para usuarios identificados
7. listar entradas en la página de inicio
8. página de edición de entradas para usuarios logueados
9. poder borrar entradas
10. añadir un buscador de entradas a la web

### code
~~~
// conectar a la base de datos
$conexion = mysqli_connect("localhost", "root", "", "phpsql");

// validacion de la conexion 
if (mysqli_connect_errno()) {
	echo "La conexion a la base de datos MYSQL ha fallado: ".mysqli_connect_errno();
} else {
	echo "Conexion realizada correctamente :) <br/><br/>";
}

// consulta para configurar la decodificacion de caracteres 
mysqli_query($conexion, "SET NAMES 'utf8' ");

// consulta select desde php 
$query = mysqli_query($conexion, "SELECT * FROM notas");

while($nota = mysqli_fetch_assoc($query)) {
	echo '<h3>Título: ',$nota['titulo'],'</h3>';
	echo $nota['descripcion'],'<br/>';
	echo $nota['color'],'<br/>';
}

// ver que datos hay en la variable
// var_dump($query);
~~~

### Conexion
1. decodificacion de la base de datos
~~~
utf8_general_ci
~~~

2. sintaxis de conexion
~~~
$conexion = mysqli_connect($host, $user, $password, $port, $database);
~~~

3. decodificacion de caracteres
~~~
mysqli_query($conexion, "SET NAMES 'utf8' ");
~~~

4. consulta
~~~
$query = mysqli_query($conexion, "SELECT * FROM notas");
~~~

5. recorrer array asociativo de los elementos
~~~
while($nota = mysqli_fetch_assoc($query)) {
	echo '<h2>',$nota['titulo'],'</h2>';
	echo $nota['descripcion'],'<br/>';
	echo $nota['color'],'<br/>';
}
~~~

6. valida la conexion si fue o no exitosa
~~~
if (mysqli_connect_errno()) {
	echo "La conexion a la base de datos MYSQL ha fallado: ".mysqli_connect_errno();
} else {
	echo "Conexion realizada correctamente <br/>";
}
~~~

# Insertar datos a la base de datos desde PHP 
1. insertar datos con php a nuestra base de datos
2. creamos la consulta INSERT, y la  almacenamos en un variable
3. mysqli_query($conexion, $sql), para insertar los datos
~~~

$sql = "INSERT INTO notas VALUES (null, 'Laravel', 'framework for PHP backend', 'lightgray')";

$insertar = mysqli_query($conexion, $sql);

if ($insertar) {
	echo "Datos insertardos correctamente";
} else {
	echo "Error: ".mysql_error($conexion);
}
~~~
___

# Proyecto completo de PHP, HTML, CSS y MySQL
1. primeros pasos
2. Maquetacion
3. de HTMl a PHP
4. Registro de usuarios
5. Login de usuarios
6. categorias y entradas
7. listado de entradas
8. edicion de entradas
9. borrado de entradas
10. buscador en PHP

# Proyecto blog de video juegos
Pasos para crear el blog de video juegos e ir validando los datos
1. se diseña la página en HTML y CSS
2. se crean las secciones
- registro.php
	- validacion de campos ***captura POST***
	- asignacion datos del metodo POST a la variable del campo
	- comprobacion de datos correctos
	- captura de errores en un array (key:value)
- index.php
	- includes el codgio separado por secciones, para mantenibilidad
3. includes
- connection.php
	- configuracion del servidor 
		- mysqli_connect
		- $server, $username, $password, $database
	- seteo de caracteres utf-8
		- mysqli_query($db, "SET NAMES 'utf-8' ");
	- estara la session activa, mientras el login este activo
		- session_start();
- header.php
	- importamos 
		- require_once 'connection.php';
	- cabecera ***logo***
	- metadatos ***meta etiquetas HTML***
	- stylos ***link ./assets/css/style.css***
	- menu ***navbar del menu de links***
- sidebar.php
	- require_once 'includes/helpers.php'
	- aside
		- bloque de login
		- bloque de registrese
			- form
				1. input ***campos datos post***
				2. echo ***manejo de errores con div***
				3. funcion mostrarErrores()
					- arrayErrores
					- campo a asociaciar
- footer
	- pie de página
4. funciones
	- helpers.php
		- mostrarErrores($errores, $campo);
			- $errores ***arrays clave valor***
				- clave = ***nombre del campo***
				- valor = ***mensaje de error***
			- $campo
				input validado, para buscar clave del array, y mostrar el error, que coincida
			- return alerta en div con el mensaje del valor del error del array
		- borrarErrores()
			- funcion que que vacia el array a null
			- div con el mensaje ***unset()***


### Pasos para validación y entrega del mensaje de error 
1. campurar los datos de los campos, validando que contenga datos
	- $name = isset($_POST['name']) ? $_POST['name'] : false;
	- $lastName = isset($_POST['lastName']) ? $_POST['lastName'] : false;
	- $email = isset($_POST['email']) ? $_POST['email'] : false;
	- $password = isset($_POST['password']) ? $_POST['password'] : false;
2. validamos que los datos que traigan cumplan con ciertas condiciones validando que el dato del campo sea correcto
~~~
if (!empty($name) && !is_numeric($name) && !preg_match("/[0-9]/", $name)) {
		$nombre_validado = true;
	} else {
		$nombre_validado = false;
		$errores['name'] = "Nombre Invalido";
	}
~~~
- si el dato del campo NO es correcto, cargamos el array de errores con clave ***nombre del la variable*** valor ***el mensaje de error***, para todos los campos
3. generamos alerta con una funcion que compruebe los datos que tenemos en el array de errores (key:value), retornando ***return*** un div con el ***value*** de la llave del campo
4. mostramos el mensaje de error, evitando el envio de datos erroneos a registro.php 

___

# envio de datos correctos a la base de datos por el formulario de registro.php

1. cifrar la contraseña
- guardamos la constraseña cifrada con password_hash, que recibe 3 parametros
	1. la contraseña real ***($password)***
	2. PASSWORD_BCRYPT ***encripta la contraseña***
	3. ['COST'=>4] ***numero de veces que encripta la contraseña***
~~~
$password_segura = password_hash($password, PASSWORD_BCRYPT, ['COST'=>4]);
~~~
con esto ya podemos almacenar la contraseña de manera segura, encriptada en la base de datos
~~~
string(4) "hola" string(60) "$2y$10$NRy1jJVYELzxuiQHSVQp2.l.21VEpViHU7VXMGoL2DtwRDpNIKya."
~~~
2. descifrar la contraseña
- debemos de comparar la password_segura, contra la password del usuario
- atraves de ***password_verify***, que recibe 2 parametros, la password del usuario y la password cifrada
~~~
var_dump(password_verify($password, $password_segura));
~~~
- lo que nos devuelve es un valor booleano ***true or false***, confirmando que son la misma clave

### Insertar el registro a la base de datos.
min 15:34, vistas de errores en el index

1. para escapar caracteres extraños en los campos
~~~
mysqli_real_escape_string()
~~~

faltan pasos de vistas de errores

### Login de registro
1. iniciar la session conexion a la db
2. recoger los datos del formulario
3. comprobar la contraseña
4. consulta para comprobar credenciales del usuario
5. utilizar una session para guardar los datos del usuario logeado
6. si falla enviar una sesion con el fallo
7. redirigir

# Categorias y Entradas
crear las tablas de entradas y de categorias

1. listo el video 2, mostrar posts en la web

vamos por el video 3. mostrar mas informacion de las entradas