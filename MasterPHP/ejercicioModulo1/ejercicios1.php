<?php 
// ejercicios de practica

// crear variables con pais y continente, he imprimirlas, luego comentario con el tipo de dato que tienen

$pais = 'alemania';
$continente = 'europa';

echo "pais $pais y continente $continente\n";
echo var_dump($pais);
echo var_dump($continente);

// solucion
$pais2 = 'argentina';
$continente2 = 'america del sur';
echo "$pais2 - $continente2";

// sacar los numeros pares del 1 al 100
$contador = 100;
$numero = 1;

do {
  if ($numero%2 == 0) {
    echo "imprimiendo los pares $numero\n";
    $numero++;
  } else {
    $numero++;
  }
} while ($numero <= $contador);

// solucion
for ($i = 1; $i <= 21; $i++) {
  if ($i%2 == 0) {
    echo "$i \n";
  }
}

// imprimir el cuadrado del 1 al 40, que es un numero multiplicado por si mismo, de los numeros naturales
// se debe hacer con while

$cuadrado = 1;
while ($cuadrado < 41) {
  $resultado = $cuadrado * $cuadrado;
  echo "cuadrado de $cuadrado es $resultado\n";
  $cuadrado++;
}

// solucion

$conteo = 0;
while ($conteo <= 40) {
  $cuadro = $conteo * $conteo;  
  echo $cuadro;
  $conteo++;
}

// con el for 
for ($i = 1; $i <= 40; $i++) {
  $igual = $i * $i;
  echo "cuadrado de: $i es $igual\n";
}

// solucion 
for ($contadorr = 0; $contadorr <= 40; $contadorr++) {
  $cuadro2 = $contadorr * $contadorr;  
  echo "$cuadro2\n";
}

// recoger dos numeros por url (parametros GET) y hacer todas las operaciones basicas de una calculadora (suma, resta, multiplicacion y division)

if (isset($_GET['numero1']) && isset($_GET['numero2'])) {
  $numeroGet1 = $_GET['numero1'];
  $numeroGet2 = $_GET['numero2'];
  
  echo "suma: ($numeroGet1+$numeroGet2)\n";
  echo "resta: ($numeroGet1-$numeroGet2)\n";
  echo "multiplicacion: ($numeroGet1*$numeroGet2)\n";
  echo "division: ($numeroGet1/$numeroGet2)\n";

} else {
  echo "introduce los valores por url\n";
  $numeroGet1 = 30;
  $numeroGet2 = 20;
  
  echo "vamos por consola con $numeroGet1 y $numeroGet2\n";
  echo "suma:".($numeroGet1+$numeroGet2)."\n";
  echo "resta:".($numeroGet1-$numeroGet2)."\n";
  echo "multiplicacion:".($numeroGet1*$numeroGet2)."\n";
  echo "division:".($numeroGet1/$numeroGet2)."\n";
}

// hacer un programa que muestre los numero entre dos numeros que entren por get 
if (isset($_GET['numero1']) && isset($_GET['numero2'])) {
  $numero3 = $_GET['numero1'];
  $numero4 = $_GET['numero2'];

  if ($numero3 > $numero4){
    for ($i = $numero3; $i <= $numero4; $i++) {
      echo "$i\n"; 
    }
  } 
  echo "el numero 2 debe de ser menos al numero 1";
} else {
  echo "introduce los valores por url\n";
  $numero3 = 10;
  $numero4 = 50;

  if ($numero3 < $numero4) {
    for ($i = $numero3; $i <= $numero4; $i++) {
      echo "$i\n"; 
    }
  }
  else {
  echo "el numero 2 debe de ser menos al numero 1";
  }
}

// crear todas las tablas de multiplicar en html
// modulo 13 tablas_multiplicar.php

// imprimir pares e impares

$num1 = 0;
for ($i = 0; $i < 100; $i++) {
  if ($i%2 == 0) {
    echo "$i es par\n";
  } else {
    echo "$i es impar\n";
  }
}

// listo hasta el modulo basico de programacion en php 






