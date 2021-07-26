<?php 
// elimina las cookies, y ademas debemos caducar las cookies tambien.
if ($_COOKIE['micookie']) {
	unset($_COOKIE['micookie']);
	setcookie('micookie','',time()-100);
}

// configuramos que nos regrese a ver_cookie.php
header('location:ver_cookie.php');
// hace el borrado de la cookie y vuelve a mostrar las cookies

?>

<h1>
	<a href="ver_cookie.php">vuelve</a>
</h1>