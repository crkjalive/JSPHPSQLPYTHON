<?php

$resultado = false;

if (isset($_POST['n1']) && isset($_POST['n2'])) {
	
	$digito1 = $_POST['n1'];
	$digito2 = $_POST['n2'];
	
	if (is_numeric($digito1) && is_numeric($digito2)) {
			
		if (isset($_POST['sumar'])){
		$resultado = " $digito1 más $digito2 = ". ($digito1 + $digito2);
		}
	
		if (isset($_POST['restar'])){
			$resultado = " $digito1 menos $digito2 = ". ($digito1 - $digito2);
			}
		
		if (isset($_POST['multiplicar'])){
			$resultado = " $digito1 por $digito2 = ". ($digito1 * $digito2);
		}
		
		if (isset($_POST['dividir'])){
			$resultado = " $digito1 entre $digito2 = ". ($digito1 / $digito2);
		}
	}
	else {
		$resultado = "No hay datos que operar";
	}

}

?>
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Calculadora en PHP</title>
	<style>
		*,*::after,*::before{box-sizing:border-box;padding:0;margin:0;font-family: arial;}
		form{width:400px;padding:0 2em 2em 2em;margin:0 auto;}
		h2{text-align:center; padding: 0 0 1em 0;}
		input{width:100%;border:none;padding: 1em .5em;background-color:#dddddd;border-radius:5px;margin-bottom:.5em}
		input[type='submit']{width:24%; background-color:#dddddd;margin-top:.5em;border-radius:5px}
		.title_calculadora{padding: .5em 1em;text-align:center}
		.grande{font-size: 30px;font-weight: bold;}
		label{text-transform:uppercase;font-weight:600}
	</style>
</head>
<body>
	<h1 class="title_calculadora">Calculadora en PHP</h1>
	<form action="" method="post">

		<?php 
			if ($resultado != false):
				echo '<h2>'.$resultado.'</h2>';
			endif;
		?>
	
		<label for="n1">cifra 1</label>	
		<input type="number" name="n1" id="">
		
		<label for="n2">cifra 2</label>	
		<input type="number" name="n2" id="">
		
		<input type="submit" value="Sumar" name="sumar">
		<input type="submit" value="Restar" name="restar">
		<input type="submit" value="Multiplicar" name="multiplicar">
		<input type="submit" value="Dividir" name="dividir">
	
	</form>
</body>
</html>