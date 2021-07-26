<?php

// iniciar la conexion con la DB
require_once ('includes/connection.php');

// llegan los datos por post de email y password
if (isset($_POST)) {

    // borrar error antigüo 
    if (isset($_SESSION['error_login'])) {
        session_unset($_SESSION['error_login']);
    }

    // recibimos datos del formulario 
    $email = trim($_POST['email']);
    $password = $_POST['password'];

    // consulta para comprobar las credenciales
    $sql = "SELECT * FROM usuarios WHERE email = '$email' ";
    // ejecutar la consulta 
    $login = mysqli_query($db, $sql);

    // comprobamos si hay registro
    if ($login && mysqli_num_rows($login) == 1) {

        // generar array asociativo del usuario
        $usuario = mysqli_fetch_assoc($login);

        // comprobar la contraseña / cifrar
        $verifica = password_verify($password, $usuario['password']);
        
        if($verifica) {
            // creamos una session para guardar los datos del usuario
            $_SESSION['usuario'] = $usuario;
            $_SESSION['error_login'] = null;
        } else {
            // si algo falla enviar una session con el fallo
            $_SESSION['error_login'] = 'login incorrecto';
        }
    } else {
        // mnensaje de error
        $_SESSION['error_login'] = 'login incorrecto';
    }
}
// redirigir al index.php
header('Location: index.php');