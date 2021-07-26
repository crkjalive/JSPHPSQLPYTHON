<?php

// esta funcion nos filtra que sea un email valido
function validarEmail ($email) {

	$status = 'No valido';

	// filtramos la variable y el campo si no esta vacio
	if (!empty($email) && filter_var($email, FILTER_VALIDATE_EMAIL)) {
		$status = 'Valido';
	}

	return $status;
}

// recibimos el parametro por get, y llamamos la funcion que valide si ese parametro es un email

if (isset($_GET['email'])) {
	echo validarEmail($_GET['email']);
} else {
	echo "pasar un email por el metodo GET";
}

/*
pasamos por get el email para validar
validarEmail.php?email=jared@gmail.com
*/
