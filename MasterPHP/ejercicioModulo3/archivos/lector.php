<?php 

// abrir archivos r de read, a+ todos los permisos.
$archivo = fopen("archivo.txt","a+");

// leer contenido linea por linea
while (!feof($archivo)) {
	$contenido = fgets($archivo);
	echo $contenido."<br/>";
}

// escribir dentro del fichero
fwrite($archivo, "probemos con mas agregando datos al fichearo\n mientras escribimos texto de relleno\n");

// cerrar archivo
fclose($archivo);

?>