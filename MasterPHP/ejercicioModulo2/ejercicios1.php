<?php
/* 
modulo 2 de ejercicios acerca de los arrays
1. crear array con 8 numeros
2. recorerlo y mostrar
3. ordenarlo y mostrar 
4. mostrar su longitud 
5. buscar algo 
 */

echo "---mi code---\n";
$numeros = [4,47,5,2,3,7,10,50];
sort($numeros); // true 1
for ($i=0; $i < count($numeros); $i++){
  echo "recorriendo con for un array, indice $i, valor: ".$numeros[$i]."\n";
}

echo sizeof($numeros)."\n";
echo array_search("7",$numeros)."\n";

// solucion 
$enteros = array(11,44,55,77,23,9,97,67);
echo "---Solucion---\n";

function mostrarArray ($enteros) {
  $resultado = "";
  foreach($enteros as $entero){
    $resultado .= "$entero\n";
  }
  return $resultado;
}

sort($enteros);
echo mostrarArray($enteros)."\n";

echo count($enteros)."\n";

$buscar = 44;
$search = array_search($buscar, $enteros);
  
  if(!empty($search)) {
    echo "El numero $buscar existe";
} else {
    echo "El numero $buscar NO existe";
}





















