<?php

$archivo = $_FILES['archivo'];
$nombre = $archivo['name'];
$tipo = $archivo['type'];

//comprobamos que sea una imagen de cualquiera de estos tipos jpg, jpeg, png, gif.

if ($tipo == 'image/jpg' || $tipo == 'image/jpeg' ||$tipo == 'image/png' || $tipo == 'image/gif') {
    
    // images/ donde vamos a guardar la imágen.

    if (!is_dir('images')) {
        mkdir('images', 0777);
    }

    // archivo en directorio temporal, antes de subir al servidor.

    move_uploaded_file($archivo['tmp_name'], 'images/'.$nombre);
    
    // refresca a los 5 seg y redirecciona a index

    header("Refresh: 5; URL=index.php");
    echo "<h1>Imagen subida correctamente</h1>";

} else {
    header("Refresh: 5; URL=index.php");
    echo "<h1>Sube una imágen de formato correcto</h1>";
}






/* var_dump($archivo);
die(); */