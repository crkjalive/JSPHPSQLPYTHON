<?php 

// se validan si las variables existen con datos, y las imprime
if (isset($_POST['titulo']) && isset($_POST['descripcion'])) {
	echo '<h1>'.$_POST['titulo'].'</h1>';
	echo '<h2>'.$_POST['descripcion'].'</h2>';
}