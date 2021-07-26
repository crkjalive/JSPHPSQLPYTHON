<?php 

if (isset($_POST)) {
	
	require_once 'includes/connection.php';
	
	$name = isset($_POST['name']) ? mysqli_real_escape_string($db, trim($_POST['name'])) : false;
	$lastName = isset($_POST['lastName']) ? mysqli_real_escape_string($db, trim($_POST['lastName'])) : false;
	$email = isset($_POST['email']) ? mysqli_real_escape_string($db, trim($_POST['email'])) : false;
	$password = isset($_POST['password']) ? mysqli_real_escape_string($db, trim($_POST['password'])) : false;
	
	// var_dump($_POST); // muestra que llega del formulario

	// almacenamiento de errores
	$errores = array();

	// Validar los campos antes de almacenarlos en la base de datos
	// name
	if (!empty($name) && !is_numeric($name) && !preg_match("/[0-9]/", $name)) {
		$nombre_validado = true;
	} else {
		$nombre_validado = false;
		$errores['name'] = "Nombre Invalido";
	}

	// lastName
	if (!empty($lastName) && !is_numeric($lastName) && !preg_match("/[0-9]/", $lastName)) {
		$apellido_validado = true;
	} else {
		$apellido_validado = false;
		$errores['lastName'] = "Apellido Invalido";
	}

	// email
	if (!empty($email) && filter_var($email, FILTER_VALIDATE_EMAIL)) {
		$email_validado = true;
	} else {
		$email_validado = false;
		$errores['email'] = "Correo Invalido";
	}

	// password
	if (!empty($password)) {
		$password_validado = true;
	} else {
		$password_validado = false;
		$errores['password'] = "Contraseña vacia";
	}

	// var_dump($errores);

	$guardar_usuario = false; 

	if (count($errores) == 0) {

		// cifrar contraseña
		$password_segura = password_hash($password, PASSWORD_BCRYPT, ['COST'=>4]);

		/* var_dump($password);
		var_dump($password_segura);
		echo "<br/>";
		var_dump(password_verify($password, $password_segura));
		die(); */

		// Insertamos el usuario
		$guardar_usuario = true;

		// creamos consulta del formulario para insertarlo en la base de datos
		$sql = "INSERT INTO usuarios VALUES (null, '$name', '$lastName', '$email', '$password_segura', null);";

		// guardar la consulta en la DB, con la conexión
		$guardar_insert = mysqli_query($db, $sql);

		// comprobamos si son correctos los datos
		if ($guardar_insert) {
			$_SESSION['completado'] = "el registro fue exitoso";
		} else {
			$_SESSION['errores']['general'] = "Fallo al insertar el registro";
		}

	} else {
		$_SESSION['errores'] = $errores;
	}
}
// redireccionamos al index luego de todo
header('Location: index.php');
 