<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Validacion de formularios</title>
	<style>
		*{box-sizing: border-box;font-family: arial;}
		h1{text-align: center;margin: 1em auto;width: 100%;}
		h3{text-align: center}
		form{width: 200px;margin: 0 auto;border: 1px solid dodgerblue; padding: 1em; box-shadow: 0px 5px 6px #456776}
		input{margin: 0 0 1em 0;width: 100%;padding: .5em}
		label{text-transform: uppercase;font-weight: bold;font-size:14px}
	</style>
</head>
<body>
	<h1>Validar formularios en php</h1>
	<h3>
		
<?php 
	if (isset($_GET['error'])) {
		$error = $_GET['error'];
		
		if ($error == 'faltan_datos') {
			echo "<strong style='color:red'>debes llenar todos los campos</strong>";
			}

		if ($error == 'error en el nombre') {
				echo "<strong style='color:red'>error en el nombre</strong>";
			}

		if ($error == 'error en el apellido') {
				echo "<strong style='color:red'>error en el apellido</strong>";
			}

		if ($error == 'error en la edad') {
				echo "<strong style='color:red'>Debes ser mayor de edad</strong>";
			}

		if ($error == 'error en el correo') {
				echo "<strong style='color:red'>error en el correo</strong>";
			}

		if ($error == 'error en la clave') {
				echo "<strong style='color:red'>error en la clave</strong>";
			}
	}
?>
	</h3>
	<form action="procesarFormulario.php" method="POST">
		
		<label for="name">Nombre</label>
		<!-- <input type="text" name="name" /> -->
		<input type="text" name="name" required="required" pattern="[A-Za-z]+" />

		<label for="lastName">Apellido</label>
		<!-- <input type="text" name="lastName" /> -->
		<input type="text" name="lastName" pattern="[A-Za-z]+" />
		
		<label for="age">Edad</label>
		<!-- <input type="number" name="age" /> -->
		<input type="number" name="age" required="required" pattern="[0-9]+" range="18-99" />
		
		<label for="email">Correo</label>
		<!-- <input type="email" name="email" /> -->
		<input type="email" name="email" required="required" />
		
		<label for="pass">Contraseña</label>
		<!-- <input type="password" name="pass" /> -->
		<input type="password" name="pass" required="required" />

		<input type="submit" value="Cargar">

	</form>
</body>
</html>