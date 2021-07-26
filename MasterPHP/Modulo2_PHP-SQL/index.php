<?php 

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

/*
//insertar datos en sql desde php

$sql = "INSERT INTO notas VALUES (null, 'Laravel', 'framework for PHP backend', 'lightgray')";
$insertar = mysqli_query($conexion, $sql);

if ($insertar) {
	echo "Datos insertardos correctamente";
} else {
	echo "Error: ".mysql_error($conexion);
}
*/