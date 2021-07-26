<?php 
echo "<table border=1><tr>"; // inicio de la tabla

echo "<tr>"; // inicio de las celdas 
  for($cabecera = 0; $cabecera <= 100; $cabecera++) {
    echo "<td>Tabla del $cabecera</td>";
  }

echo "</tr>"; // cierre fila 1 de celdas 

echo "<tr>"; // inicio fila 2 de celdas

for ($i = 0; $i <= 100; $i++) {
  echo "<td>";
  
  for($x = 0; $x <= 100; $x++) {
    
    echo "$i x $x = " . ($i*$x)."<br/>";
    
  }
  
  echo "</td>";
}
  
echo "</tr>"; // cierre fila 2 de celdas

echo "</table>";


?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>tablas de multiplicar</title>
  <style>
    
  </style>
</head>
<body>
  


</body>
<html>
