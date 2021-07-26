<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>formularios</title>
	<style>
		*{box-sizing: border-box;margin: 0;padding: 0}
		body{padding: 1em;font-weight: 600;font-family: arial}
		h1{text-transform: uppercase;text-align: center}
		form{border-radius: 5px; border: 1px solid dodgerblue; padding:1em;width: 250px; text-transform: uppercase; margin: .5em auto}
		input{width: 100%;border: none;border-bottom: 1px solid dodgerblue; margin: .5em 0;padding: .5em;}
		input[type="submit"]{border: none;border-radius: 5px;cursor: pointer}
  .seleccion{
  margin:0 auto;font-size: 1em;width:100%;
}
  h4{text-transform:capitalize;}
	</style>
</head>
<body>
	<h1>formularios</h1>
	<form action="" method="POST" enctype="multipart/form-data">
		<?php $nombre = "wizard"; ?>
		<label for="nombre">Nombre</label>
		<input type="text" name="nombre"/>
		<label for="apellido">Apellido</label>
		<input type="text" name="apellido"/>
	<input type="submit" value="enviando datos"/>

<h4>Seleccionador de opciones</h4>
<select class="seleccion" name="peliculas">
  <option>Batman</option>
  <option>Spiderman</option>
  <option>Wonder Woman</option>
  <option>Joker</option>
  <option>Flash</option>
  <option>Joda</option>
</select>
	</form>

</body>
</html>
