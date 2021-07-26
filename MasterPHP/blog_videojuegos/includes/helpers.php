<?php 

function mostrarError ($errores, $campo) {
	$alerta = '';
	
	if (isset($errores[$campo]) && !empty($campo)) {
		$alerta = "<div class='alerta'> ".$errores[$campo]."</div>";
	}
	
	return $alerta;
}

function borrarErrores () {
	$borrar = false;

	if ( isset($_SESSION['errores'])){
		$_SESSION['errores'] = null;		
		$borrar = "<div class='alerta'>".session_unset($_SESSION['errores'])."</div>";
	}

	if ( isset($_SESSION['completado'])) {
		$_SESSION['completado'] = null;
		session_unset($_SESSION['completado']);
	}

	return $borrar;
}

function conseguirCategorias($connection) {
	$sql = "SELECT * FROM categorias ORDER BY id ASC;";
	$categorias = mysqli_query($connection, $sql);

	$resultado = array();

	if ($categorias && mysqli_num_rows($categorias) >= 1) {
		$resultado = $categorias;
	}
	
	return $resultado;
}

function conseguirEntradas($connection){
	$sql = "SELECT p.*, c.* FROM posts p
			INNER JOIN categorias c ON p.categoria_id = c.id
			ORDER BY p.id DESC LIMIT 4";
	$post = mysqli_query($connection, $sql);

	$resultado = array();

	if($post && mysqli_num_rows($post) >= 1) {
		$resultado = $post;
	}

	return $resultado;
}