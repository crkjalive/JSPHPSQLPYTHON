<?php 
// para mostrar el valor de las cookies, tengo que usar $_COOKIE, una variable superglobal, siendo esta una array asociativo

if (isset($_COOKIE['micookie'])) {
	echo "<h1>".$_COOKIE['micookie'];
} else {
	echo "No existe la cookie";
}

if (isset($_COOKIE['oneyear'])) {
	echo "<h1>".$_COOKIE['oneyear'];
} else {
	echo "No existe la cookie";
}
?> 
<br/>
<h1>
	<a href="crear_cookie.php">crear cookie mis galletas</a>
</h1>
<h1>
	<a href="borrar_cookie.php">Borrar mis galletas</a>
</h1>