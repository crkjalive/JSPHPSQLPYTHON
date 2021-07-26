<?php 
$error = 'faltan_datos';
if ( !empty($_POST['name']) && !empty($_POST['lastName']) && !empty($_POST['age']) && !empty($_POST['email']) && !empty($_POST['pass']) ) {
	$error = 'Datos exitosos OK';
	$name = $_POST['name'];
	$lastName = $_POST['lastName'];
	$age = (int) $_POST['age'];
	$email = $_POST['email'];
	$pass = $_POST['pass'];

	// Validar realmente el tipo dato
	if(!is_string($name) || preg_match("/[0-9]+/", $name)){
		$error='error en el nombre';
	}

	if(!is_string($lastName) || preg_match("/[0-9]+/", $lastName)){
		$error='error en el apellido';
	}
	
	if(!is_int($age) || !filter_var($age, FILTER_VALIDATE_INT) || $age > 99 || $age < 18){
		$error='error en la edad';
		header("Location:index.php?error=$error");
	}
	
	if(!is_string($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)){
		$error='error en el correo';
	}

	if(empty($pass) || strlen($pass)<5){
		$error='error en la clave';
	}


	// debugging
	// var_dump($_POST); // muestra que datos estoy ingresando
	// var_dump($error); // muestra que valor tiene el error
	// die();


} else {
	$error = 'faltan_datos';
	header("Location:index.php?error=$error");
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>validacion</title>
</head>
<body>
	<?php if ($error=="Datos exitosos OK"): ?>
		<h1>Datos validados correctamente</h1>
		<p><?=$name?></p>
		<p><?=$lastName?></p>
		<p><?=$age?></p>
		<p><?=$email?></p>
		<p><?=$pass?></p>
	<?php endif; ?>
	
</body>
</html>

