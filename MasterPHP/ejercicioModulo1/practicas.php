<?php


echo "--- ### --- while --- ### --- \n";

$numeros = 0;

while ($numeros <= 100) {
  echo ("imprimiendo lineas de texto con variables $numeros\n");
  $numeros++;
}

echo "--- ### --- while --- ### --- \n";

if (isset($_GET['numero'])) {
  // casting, cambiar tipo de dato
  $numero = (int)$_GET['numero'];
} else {
  $numero = 9;
}

//var_dum($numero);

echo "<h1>Tabla de multiplicar del numero $numero</h1>";
$contador = 0;

while ($contador <= 10) {
  echo "$numero x $contador = " . ($numero*$contador)."\n";
  $contador++;

}

echo "--- ### --- for --- ### --- \n";

$resultado = 0;

for ($i= 0;$i <= 10; $i++) {
  $resultado = $resultado + $i;
  echo "el resultado es $resultado\n";
}


for ($contador = 1; $contador <= 10; $contador++) {
  echo "$numero x $contador = ".($numero*$contador)."\n";
}





































