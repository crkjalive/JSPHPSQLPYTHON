<?php 

// recibimos el contenido por _GET
/* 
echo '<h1>' .$_GET['nombre']. '</h1>';
echo '<h1>' .$_GET['apellido']. '</h1>';
*/

// recibimos por _POST
echo '<h1>' .$_POST['nombre']. '</h1>';
echo '<h1>' .$_POST['apellido']. '</h1>';

var_dump($_POST);
