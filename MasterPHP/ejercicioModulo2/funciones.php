<?php
/*
function tabla($numero) {
  echo "<h3>Tabla de multiplicar del numero: $numero</h3>";

  for ($i=0; $i <= 10; $i++) {
    $operacion = $numero*$i;
    echo "$numero x $i = $operacion <br/>";
  }
}

for($i=0; $i <= 10; $i++){
  tabla($i);
}
*/

/* 
function calculadora($numero1, $numero2, $negrita = false) {
  $suma = $numero1 + $numero2;
  $resta = $numero1 - $numero2;
  $multiplicacion = $numero1 * $numero2;
  $division = $numero1 / $numero2;

  if(!$negrita){
    echo "<h1>";
  }

  echo "Suma: $suma\n";
  echo "Resta: $resta\n";
  echo "Multiplicacion: $multiplicacion\n";
  echo "Division: $division\n";
  echo "<hr/>\n";

 if(!$negrita){
    echo "</h1>";
  }

}
calculadora(10,5);
calculadora(12,3,true);
calculadora(42,2);
calculadora(6,3);
calculadora(19,7);
calculadora(8,2,true);
*/

// return 

/* 
function calculadora($numero1, $numero2, $negrita = false) {
  $suma = $numero1 + $numero2;
  $resta = $numero1 - $numero2;
  $multiplicacion = $numero1 * $numero2;
  $division = $numero1 / $numero2;

  $cadenaTexto = "";

  if($negrita){
    $cadenaTexto .= "<h1>";
  }

  $cadenaTexto .= "Suma: $suma\n";
  $cadenaTexto .= "Resta: $resta\n";
  $cadenaTexto .= "Multiplicacion: $multiplicacion\n";
  $cadenaTexto .= "Division: $division\n";
  $cadenaTexto .= "<hr/>\n";

  if($negrita){
    $cadenaTexto .= "</h1>";
  }

  return $cadenaTexto; // siempre devemos usar el return 

}
echo calculadora(10,20);
*/ 

// funciones que reciben funciones
/*
function getNombre ($nombre) {
  $texto = "Su nombre es <strong>$nombre </strong>";
  return $texto;
}

function getApellido($apellido) {
  $texto = "y su apellido es <strong>$apellido </strong>";
  return $texto;
}

function devuelveNombre ($nombre, $apellido) {
  $texto = "<h1>".getNombre($nombre).getApellido($apellido)."</h1>";
  return $texto;
}

echo devuelveNombre("Jared", "Latorre")."<br/>";
echo getNombre('Paco')."<br/>";
*/

// uso de variables locales y globales

/* 
$frase = " ni los genios son tanto, ni los mediocres tampoco ";

echo $frase;

function holaMundo() {
  global $frase;
  echo "<h1> $frase </h1>";
}
holaMundo();
*/
/*
// funciones en variables
function buenasDias () {
  return "<h1>Hola! buenos dias</h1>";
}
function buenasTardes () {
  return "<h1>Hola! como ha estado la comida</h1>";
}
function buenasNoches () {
  return "<h1>¿Te vas a dormir ya? Buenas noches!!</h1>";
}

$horario = 'Noches';

$miFuncion = "buenas".$horario;

echo $miFuncion();

// de esta manera guardamos el string con el nombre de la funtion, y luego ejecutamos estavariable con los parentesis, ejecutando la funcion. 

$jiji = 'buenasTardes';
echo $jiji();

echo date('D-d M Y')."\n"; // Mon-17 May 2021

echo round(7.325659)."\n"; // 7

echo pi()."\n"; // 3.1415926535898

echo rand(0,10)."\n"; // rango aleatorio entre 0 y 10

echo rand()."\n"; // numero aleatorio

$numberr = 0;
echo is_int($numberr);
*/

$textin = "";
if (empty($textin)) {
  echo "No hay dato\n";
} else {
   echo "Hay dato\n";
}

$pelicula = "La vida es bella";
echo strpos($pelicula, "vida");
