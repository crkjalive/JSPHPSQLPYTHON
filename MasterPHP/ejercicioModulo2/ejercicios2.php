<?php
// ejercicio 2
// escribir un programa con php que añada valores a un array mientras que su longitud sea menor a 120 y luego mostrarlo por pantalla

$arrai = array();

for ($i = 120; $i >= 1;$i--) {
  array_push($arrai,"$i");
}

var_dump($arrai)."<bh/>";

// solucion 

$coleccion = array();
for ($i = 0; $i < 120; $i++) {
  array_push($coleccion, "elemento-$i <br/>");
}

var_dump($coleccion);

// ejercicio 3 
// no lo hice por que estaba haciendo con funciones

// solucion 

$texto = "";

if (empty($texto)) {
  $texto = "Hola yo soy un texto de relleno";
  $mayus = strtoupper($texto);
  echo "<h1>$mayus</h1>";
} else {
  echo "<h1>la variable no esta vacia contiene: $texto</h1>";
}

// ejercicio 4 
// crear un script que tenga4 variables, una de array, int, string, bool, y que imprima, un mensaje segun el tipo de variable 

$variable1 = [];
$variable2 = true;
$variable[2] = 1;
$variable4 = "chanchito feliz";

echo gettype($variable1).'<br/>';
echo gettype($variable2).'<br/>';
echo gettype($variable[2]).'<br/>';
echo gettype($variable4).'<br/>';

// solucion

$matriz = array("hola mundo",88);
$titulo = "master en php";
$numx = 77;
$verdadera = true;

if (is_array($matriz)) {
  echo "<h1>$matriz, es un array</h1>";
}
if (is_string($titulo)) {
  echo "<h1>$titulo, es un string</h1>";
}
if (is_int($numx)) {
  echo "<h1>$numx, es un entero</h1>";
}
if (is_bool($verdadera)) {
  echo "<h1>$verdadera, esta variable es booleana</h1>";
}

// ejercicio 5
// crear un array con el contenido de la siguiente tabla:
/* columna indice, 
ACCION    AVENTURA    DEPORTE
gta	  assasins    fifa 19
cod	  crash	      pes 19
pugb 	  persia      moto gp 19

cada columna edbe llegar en un fichero externo
 */

// code..
/*
$titulos = ['accion','aventura','deporte'];
$accion = ['gta','cod','pugb'];
$aventura = ['assasins','crash', 'persia'];
$deporte = ['fifa 19','pes 19', 'moto gp 19'];

echo "<div> caja";
for ($i = 0; $i < count($titulos); $i++) {
  echo "<div>".$titulos[$i];
  for ($g = 0; $g < count($titulos); $g++) {
  echo "<div>";
    echo "<span>".$accion[$g]."</span>"; 
  echo "</div>";
  echo "<div>";
    echo "<span>".$aventura[$g]."</span>"; 
  echo "</div>";
  echo "<div>";
    echo "<span>".$deporte[$g]."</span>"; 
  echo "</div>";
  }
}
echo "</div>";
// no me salio 
 
*/

// solucion

$tabla = array(
  "accion" => array('gta','cod','pugb'),
  "aventura" => array('assasins','crash', 'persia'),
  "deporte" => array('fifa 19','pes 19', 'moto gp 19'),
);

  $categorias = array_keys($tabla);
?>

<table border='1'>
  <tr>
  <?php foreach($categorias as $categoria) : ?>
    <th><?=$categoria?></th>
  <?php endforeach; ?>
  </tr>
  <tr>
    <td><?=$tabla['accion'][0] ?></td>
    <td><?=$tabla['aventura'][0] ?></td>
    <td><?=$tabla['deporte'][0] ?></td>
  </tr>  
  <tr>
    <td><?=$tabla['accion'][1] ?></td>
    <td><?=$tabla['aventura'][1] ?></td>
    <td><?=$tabla['deporte'][1] ?></td>
  </tr>
  <tr>
    <td><?=$tabla['accion'][2] ?></td>
    <td><?=$tabla['aventura'][2] ?></td>
    <td><?=$tabla['deporte'][2] ?></td>
  </tr>
</table>

<?php
// hasta aqui solo faltaria separar en archivos diferentes y lusgo include_once
//
// include_once'accion.php';
// include_once'aventura.php';
// include_once'deporte.php';
// este codigo entro de la tabla; 

?>
