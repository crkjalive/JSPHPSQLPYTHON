# Arrays 
1. son arrays arreglos o vectores 
2. un array es una coleccion o un conjunto de datos/valores, bajo un unico nombre.
3. en poca palabras, es una variable que contiene variables.
4. para acceder a esos valores podemos usar un indice numero o alfanumerico.

### sintaxis
~~~
$pelicula = array('batman','spiderman','señor de los aninillos');
var_dump($pelicula);
~~~

### dos formas de hacer arrays
~~~
$peliculas = array('batman', 'joker', 'end game', 'superman');
$cantantes = ['alicia keys', 'shakira', 'Dr Dre', 'Snoop Dogg']; 
~~~
### mostrando tipo de dato
~~~
var_dump($peliculas);
// array(4) { [0]=> string(6) "batman" [1]=> string(5) "joker" [2]=> string(8) "end game" [3]=> string(8) "superman" }
~~~
### accediendo a cada indice
~~~
echo '<br/>';
echo $peliculas[0];
echo '<br/>';
echo $peliculas[1];
echo '<br/>';
echo $peliculas[2];
echo '<br/>';
echo $peliculas[3];
~~~

# recorer arrays 
### con el ***cilo for***, podemos recorrer arrays
~~~
$cosas = ["tete","pelota","baba","jeep"];

echo "<ul>";
for($i = 0; $i < count($cosas); $i++) {
  echo "<li>".$cosas[$i].'</li>';
}
echo "</ul>";

var_dump($cosas);
~~~


### con el ***cilo foreach***, podemos recorrer arrays
~~~
$autos = ["mazda","toyota","jeep","lamborgini"];

echo "<ul>";
foreach($auto as $autos) {
  echo "<li>auto $auto</li>";
}
echo "</ul>";
~~~

# arrays asociativos 
~~~
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
~~~

*de esta forma podemos asociar el indice y su valor*

### cuando enviamos datos por get o por post, tambien es por array asociativo

# array multidimensional 
es un array con arrays dentro 

~~~
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
~~~

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
ar_dump(cantantesFemeninas);

# agergar elementos a un array 
agregar manualmente un dato a un array 
~~~
$cantantesFemeninas[] = 'Fergie';
~~~

### push agregar al final del array 
~~~
array_push($cantantesFemeninas, "Shakira");
~~~

### quitar el ultimo o el que uno quiera 
~~~
array_pop($cantantesFemeninas);
var_dump($cantantesFemeninas);
array_push($cantantesFemeninas, "Shakira");
~~~

### aleatorio con array_rand()
~~~
$indice = array_rand($cantantesFemeninas);
echo $cantantesFemeninas[$indice];
~~~

### reverzar un array 
creando un nuevo array con los datos alreves 
~~~
var_dump(array_reverse($cantantesFemeninas));
~~~

### buscar dentro de un array / me da el indice de la busqueda 
~~~
$resultado = array_search('Dua',$cantantesFemeninas);
var_dump($resultado);
~~~
#### si no esta me da un bool(false)

### contar elementos
~~~
echo "<hr/>";
echo count($cantantesFemeninas);
echo "<hr/>";
echo sizeof($cantantesFemeninas);
~~~

# modulo 2 ejercicios 1
1. crear array con 8 numeros
2. recorerlo y mostrar
3. ordenarlo y mostrar 
4. mostrar su longitud 
5. buscar algo 

# modulo 2 ejercicios 2
1. ejercicio 2
// escribir un programa con php que añada valores a un array mientras que su longitud sea menor a 120 y luego mostrarlo por pantalla
~~~
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
~~~

2. ejercicio 3 
// programa que compruebe si una variable esta vacia y si esta vacia, rellenarla con texto y mostrarlo en mayusculas y negrita

## ejercicios2.php
aqui quedo la parctica de los siguientes ejercicio.

1. detectar si la variable tiene datos o esta vacia, si esta vacia agregar datos y convertirlo en mayusculas
2. crear 4 tipos de variables y que me diga que tipo de variable es, mostrandola en pantalla 
3. crear una tabla apartir de los datos de una array y mostrar en html, luego incluir cada array desde un archivo externo









