<?php
// arrays
$peliculas = array('batman', 'joker', 'end game', 'superman');

// array(4) { [0]=> string(6) "batman" [1]=> string(5) "joker" [2]=> string(8) "end game" [3]=> string(8) "superman" }
echo "<hr/>";
echo "<h3>Listado de peliculas por indice [0][1][2][3]</h3>";

// accediendo a cada indice
echo "<ol>";
echo "<li>$peliculas[0]</li>";
echo "<li>$peliculas[1]</li>";
echo "<li>$peliculas[2]</li>";
echo "<li>$peliculas[3]</li>";
echo "</ol>";
var_dump($peliculas);


echo "<hr/>";
echo "<h3>Listado de marca de cosas con for</h3>";
$cosas = ["tete","pelota","baba","jeep"];

echo "<ul>";
for($i = 0; $i < count($cosas); $i++) {
  echo "<li>".$cosas[$i].'</li>';
}
echo "</ul>";

var_dump($cosas);

echo "<hr/>";
echo "<h3>Listado de marca de carro con foreach</h3>";
$autos = ["bugatti","toyota","jeep","lamborgini"];

echo "<ul>";
foreach($autos as $auto) {
  echo "<li>marca: $auto </li>";
}
echo "</ul>";

// arrays asociativos
$personas = array(
  'nombre' => 'Wizard',
  'apellido' => 'Deejay',
  'web' => 'wizarddj.com',
);
var_dump($personas);


echo "<h3>accediendo al array asociativo key value </h3>";
echo "<li>".$personas['nombre']."</li>";
echo "<li>".$personas['apellido']."</li>";
echo "<li>".$personas['web']."</li>";
echo "<hr/>";

$contactos = [
    array(
    'nombre' => 'okolobebes',
    'email' => '@okolobebes',
  ),array(
    'nombre' => 'hugo',
    'email' => 'hugo@chanchitofeliz.com',
  ),
  array(
    'nombre' => 'paco',
    'email' => 'paco@chanchitofeliz.com',
  ), 
  array(
    'nombre' => 'luis',
    'email' => 'luis@chanchitofeliz.com',
  ), 
  array(
    'nombre' => 'lala',
    'email' => 'lala@chanchitofeliz.com',
  ), 

];

var_dump($contactos);

echo "<li>name <strong>". $contactos[0]['nombre']."</strong> </li>";
echo "<li>email: <strong>". $contactos[0]['email']."</strong> </li>";
echo "<li>name <strong>". $contactos[1]['nombre']."</strong> </li>";
echo "<li>email: <strong>". $contactos[1]['email']."</strong> </li>";
echo "<li>name <strong>". $contactos[2]['nombre']."</strong> </li>";
echo "<li>email <strong>". $contactos[2]['email']."</strong> </li>";
echo "<li>name <strong>". $contactos[3]['nombre']."</strong> </li>";
echo "<li>email <strong>". $contactos[3]['email']."</strong> </li>";
echo "<li>name <strong>". $contactos[4]['nombre']."</strong> </li>";
echo "<li>email <strong>". $contactos[4]['email']."</strong> </li>";

echo "<hr/>";

# funciones para arrays 
$cantantesFemeninas = ['Rihanna', 'Ariana Grande','Dua Lipa', 'Carolina Giraldo'];

### ordena alfabeticamente 
echo "<h2>ordena alfabeticamente </h2><br/>"; 
echo asort($cantantesFemeninas);
var_dump($cantantesFemeninas);

echo "<hr/>";

### ordena alfabeticamente alreves 
echo "<h2>ordena alfabeticamente alreves</h2><br/>"; 
echo arsort($cantantesFemeninas);
var_dump($cantantesFemeninas);

### ordena alfabeticamente y numericamente
$numeros = [1,2,6,3,5,7,8];
echo "<h2>ordenados de menor a mayor</h2><br/>"; 
echo sort($numeros);
var_dump($numeros);

// metodos de arrays

// insertar al final
array_push($cantantesFemeninas, "Shakira");
var_dump($cantantesFemeninas);

// quitar el ultimo o el que uno quiera 
array_pop($cantantesFemeninas);
var_dump($cantantesFemeninas);
array_push($cantantesFemeninas, "Shakira");

echo "<hr/>";

// aleatorio con array_rand()
$indice = array_rand($cantantesFemeninas);
echo $cantantesFemeninas[$indice];

echo "<hr/>";

// reverzar un array 
// creando un nuevo array con los datos alreves 
var_dump(array_reverse($cantantesFemeninas));

echo "<hr/>";

// buscar dentro de un array
// me da el indice de la busqueda 
$resultado = array_search('Dua',$cantantesFemeninas);
var_dump($resultado);
// si no esta me da un bool(false)

// contar elementos
echo "<hr/>";
echo count($cantantesFemeninas);
echo "<hr/>";
echo sizeof($cantantesFemeninas);









