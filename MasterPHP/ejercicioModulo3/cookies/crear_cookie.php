<?php 

// crear cookie estructura
//setcookie("nombre", "valor que solo puede ser texto", 'capacidad, ruta, dominio');

// cookie básica
setcookie("micookie", "cree una cookie");

// cookie con expiración
setcookie("oneyear", "valor de mi cookie con 365 dias", time()+(60*60*24*365));

// relocalización dejando los archivos solo de paso
header('location:ver_cookie.php');


?>
<h1>
	<a href="ver_cookie.php">Ver las galletas</a>
</h1>





 