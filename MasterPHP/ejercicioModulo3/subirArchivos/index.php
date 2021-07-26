<?php ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        input[type='file']{padding: 1em 1em 1em 0 ;border:0}
        input[type='submit']{padding:1em 3em; border:none;}
    </style>  
</head>
<body>
    <h1>Subir archivos con PHP</h1>
    <form action="./upload.php" method="post" enctype="multipart/form-data">
       <input type="file" name="archivo" id="" />
       <br/>
       <input type="submit" value="enviar" />
    </form>
    <h1>Listado de imagenes</h1>
    <?php
        $gestor = opendir('./images');

        if ($gestor) {
            while(($image = readdir($gestor)) !== false) {
                if ($image != '.' && $image != '..') {
                    echo "<img src='images/$image' width='300px' /><br/>";
                    
                }
            }
        }
    ?>
</body>
</html>