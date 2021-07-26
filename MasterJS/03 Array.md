# Arrays
### Arrays basicos

~~~
/* arrays, arreglos, o matrices
consta de un conjunto de datos, de cualquier tipo, al que se accede por medio de indices al array */

const datos = [1,2,3,4,5,true, false, "Jared"];

const lenguajes = new Array('PHP', 'Js', 'GO', 'Node', 'React', 'Vue', 'SQL');
console.log(lenguajes[6])
console.log(lenguajes[3])
~~~

___

### Array asociativos
capitulo de SoyDalto
aqui no se vio, me imagino que se manejan como objetos

___

### arrays avanzados

***length***

|funcion|operacion|
|-|-|
|array.length()|cuenta total de elementos de un array|
|for(let i = 0; i < lenguajes.length;i++){ // code... }	| ciclo for |


~~~
const lenguajes = new Array('PHP', 'Js', 'GO', 'Node', 'React', 'Vue', 'SQL');

// capturamos el indice por prompt
let elemento = parseInt(prompt(`indice del elemento hasta el ${lenguajes.length}: `, 1));

console.log(elemento);

// comprobamos la cantidad de indices del array
if (elemento > lenguajes.length) {
	alert('no tenemos mas lenguajes que: ' + (lenguajes.length));
} else {
	alert('el lenguaje almacenado es: ' + (lenguajes[elemento-1]));
}
~~~

### Recorrer un array con for

***mostrar todos los elementos del array en pantalla***

~~~
const lenguajes = new Array('php', 'js', 'go', 'node', 'react', 'vue', 'sql','git', 'markdown', 'vim');

document.write("<h3>Lenguajes y tecnologias de un programador</h3>");
document.write('<ul>');
for(let i = 0; i < lenguajes.length; i++ ) {
document.write('<li>');
	document.write(`Lenguaje ${i+1} ${lenguajes[i].toUpperCase()}`);
document.write('</li>');
}
document.write('</ul>');
~~~

### recorrer arrays con forEach

***forEach***

|funcion|operacion|
|-|-|
| foreach | lenguajes.forEach( (element, index, data) => {}) |
| element | es el elemento a mostrar por cada iteración|
| index | indice en el recorrido |
| data | muestra el array original |

**mostrar todos los elementos del array en pantalla**

~~~
const lenguajes = new Array('css','html','php', 'js', 'go', 'node', 'react', 'vue', 'sql','git', 'markdown', 'vim', 'kotlin');

document.write("<h3>Lenguajes y tecnologias de un programador</h3>");
document.write('<ul>');

lenguajes.forEach( (elemento, index, data) => {
	document.write(`<li> ${index} ${elemento.toUpperCase()} </li>`)
});

document.write('</ul>');
~~~

***for in***

|funcion|operacion|
|-|-|
| for in |  for (let variable in object) { // statement } |
| variable | es el elemento a mostrar por cada iteración|
| in | in que este en el array |
| object | array a recorrer |

~~~
const peliculas = new Array('Batman', 'Robin', 'Wonder Woman', 'Superman', 'Spiderman', 'Wason', 'Jared');

for (let pelicula in peliculas) {
	document.write('<h3>');
	document.write(peliculas[pelicula])
	document.write('</h3>');
	document.write('<p>Descripción de la película</p>');
}
~~~

### arrays multidimencionales

***son arrays dentro de otros arrays***

|funcion|operacion|
|-|-|
|[0][0]|primer array, indice 0|
|[1][0]|segundo array, indice 0|

~~~
const frontend = new Array('css', 'html', 'js', 'react', 'git', 'markdown');
const backend = new Array('php', 'node', 'sql', 'kotlin','go');
const desarrollo = [frontend, backend];

console.log(desarrollo[0][0]);
console.log(desarrollo[0][1]);
console.log(desarrollo[0][2]);
console.log(desarrollo[0][3]);
console.log(desarrollo[0][4]);
console.log(desarrollo[0][5]);

console.log(desarrollo[1][0]);
console.log(desarrollo[1][1]);
console.log(desarrollo[1][2]);
console.log(desarrollo[1][3]);
console.log(desarrollo[1][4]);
console.log(desarrollo[1][5]);
~~~

# Operaciones con arrays 
1. añadir elemento a una dimension
2. convertir un array a string
3. quitarlo elemento

| funcion | operacion |
|-|-|
| array.push() | agrega un elemento al final del array, arg|
| array.unshift() | agrega inicio del array |
| array.pop() | elimina el ultimo elemento del array |
| array.shift() | elimina primer elemento del array, devuelve el elemento |
| array.indexOf('param') | busca dentro del array la posicion del elemento |
| array.splice(indice, 1) | verifica el indice y borra 1 elemento |
| array.join() | convierte array, en un estring |
| array.sort() | ordena alfabeticamente los elementos de un array |
| array.reverse() | invierte los elementos de un array |

~~~
const frontend = new Array('css', 'html', 'js', 'react', 'git', 'markdown');

frontend.push('react native');
console.log(frontend);
~~~

### Metodos del array

~~~
const heroes = new Array('Batman', 'Robin', 'Wason', 'Wonder Woman', 'Jared');

console.log(heroes.shift())
console.log(heroes)

console.log(heroes.unshift('Hola Mundo'))
console.log(heroes.unshift('Google'))
console.log(heroes)

console.log(heroes.pop())
console.log(heroes)

console.log(heroes.push('IronMan'))
console.log(heroes)

console.log(heroes.indexOf('Batman'))
~~~

***splice, indexOf***

~~~
const peliculas = new Array('Batman', 'Robin', 'Wason', 'Wonder Woman', 'Jared');
console.log(peliculas)

let indice = peliculas.indexOf('Wason');

if (indice > -1) {
	peliculas.splice(indice, 2); // 2 elementos desde el encontrado
}
console.log('si es mayor a -1 es por que existe')
console.log(`eliminamos el elemento del array ${peliculas}`)
~~~

### Convertir un array a string 

***join*** separados con comas

~~~
const peliculas = new Array('Batman', 'Robin', 'Wason', 'Wonder Woman', 'Jared');
console.log(peliculas)

let cadena = peliculas.join()
console.log(`convertimos array a cadena separado por comas`)
console.log(`${cadena}`)
~~~

***join*** sin comas

~~~
const peliculas = new Array('Batman', 'Robin', 'Wason', 'Wonder Woman');

let arrAString = peliculas.join('');

console.log(`Convertimos un array en un string ${arrAString}`)
~~~

### Convertir un String a array

***split***

~~~
let cadena = "texto1,texto2,texto3";

let cadena_Array = cadena.split(",")

console.log("convertimos un String en un array");
console.log(cadena)
console.log(cadena_Array)
~~~

### Ejercicio

~~~
const peliculas = new Array();

let agregar = prompt('ingresa una pelicula: ');

while(agregar != 'salir') {
	peliculas.push(agregar);
	agregar = prompt('ingresa una pelicula: ');
	console.log(peliculas) 
}
const lista = peliculas

document.write(`<ul>`);
	peliculas.forEach( (peli, x) => {
		document.write(`<li>`);
			document.write(`<a href=''> ${x} ${peli} </a>`);
		document.write(`</li>`);
	});
document.write(`</ul>`);
~~~

# Ordenar array o arreglos

***Sort***
Ordena alfabeticamente un array

***reverse***
inviertelos elementos de un array

~~~
const peliculas = new Array('Batman', 'Robin', 'Wonder Woman', 'Superman', 'Spiderman', 'Wason', 'Jared');
console.log(peliculas)

peliculas.sort();
console.log("sort ordena alfabeticamente")
console.log(peliculas)

peliculas.reverse();
console.log("reverse invierte elementos")
console.log(peliculas)
~~~

# buscar en un array 

***find***  
find, recibe una funcion de callback que retorna true o false,  
si guardamos en variable podemos mostrar el valor del array. 
~~~
const peliculas = new Array('Batman', 'Robin', 'Wonder Woman', 'Superman', 'Spiderman', 'Wason', 'Jared');

let buscar = peliculas.find(pelicula => {
	return pelicula == "Batman"
});

document.write(buscar)
~~~

Esta funcion la saque de chiripas
~~~
const peliculas = new Array('Batman', 'Robin', 'Wonder Woman', 'Superman', 'Spiderman', 'Wason', 'Jared');


peliculas.find(pelicula => {
	document.write("<div>");
	document.write(pelicula)
	document.write("</div>");
});
~~~

***Simplificamos la función***
~~~
const peliculas = new Array('Batman', 'Robin', 'Wonder Woman', 'Superman', 'Spiderman', 'Wason', 'Jared');

let buscar = peliculas.find( pelicula => pelicula == "Jared");
document.write(buscar)
~~~

***findIndex***  
Devuelve el indice del elemento que estamos buscando
~~~
const peliculas = new Array('Batman', 'Robin', 'Wonder Woman', 'Superman', 'Spiderman', 'Wason', 'Jared');

let buscar = peliculas.findIndex( pelicula => pelicula == "Jared");

document.write(` findIndex me devuelve el indice del <br/>`)
document.write(` elemento dentro del array <h1> ${buscar} </h1>`)
~~~

***some***  
some compara valores dentro del array y si es valido devuelve true o false
~~~
const precios = new Array(10, 20, 30, 40, 50, 80);

let datoValor = precios.some(precio => precio >= 50);
document.write(`con some buscamos algo y lo comparamos <br>`);
document.write(`con un valor para saber si es True o False <br> ${datoValor}`);
~~~

# Bloque de ejercicios

***Mi codigo sin ver el video aun***

~~~


const numeros = [];
let conteo = 6

while (numeros.length <= 5){
	let pedirNumeros = parseInt(prompt(`Dame ${conteo} numeros: `,0));
	numeros.push(pedirNumeros);
	conteo--
}

document.write('<div class="numeros">');
document.write(numeros);
document.write('</div>');

let mostrar1 = numeros.sort();
console.log(mostrar1)

document.write('<div class="mostrar1">');
document.write(mostrar1);
document.write('</div>');


numeros.reverse();
document.write('<div class="mostrar2">');
document.write(numeros.reverse());
document.write('</div>');

console.log(numeros);
console.log(`¿Cuantos elementos ahi en el array? ${numeros.length}`);


const valorBuscar = parseInt(prompt("Busca un numero en el array: ", 100));

var buscado = numeros.find( k => {
	return k == valorBuscar
});

var posicion = numeros.findIndex( l => {
	return l == valorBuscar
});

if (buscado == undefined){
	console.log(`valor buscado ${valorBuscar} No esta`);
} else {
	console.log(`valor buscado Si está ${buscado} esta en la posicion ${posicion}`);
}

document.write('<div>');
if (buscado == undefined){
	document.write(`valor buscado ${valorBuscar} No esta`);
} else {
	document.write(`valor buscado Si está ${buscado} esta en la posicion ${posicion}`);
}
document.write('</div>');
~~~

***Código del master***

1. pedir numeros y guardalos en el array, va iterando y va metiendo el valor dentro del array, otra forma es con push(prompt())

~~~
const numeros = new Array(6);

for(let i = 0; i < numeros.length; i++) {
	numeros[i] = parseInt(prompt("introduce un numero: ",0));
}
console.log(numeros)
~~~

***Codigo Final***

~~~
const mostrarArray = (elementos, textoCustom = "") => {
	document.write(`<h1>Mostar array ${textoCustom}</h1>`);
	document.write(`<ul>`);
	elementos.forEach( (elemento, index) => {
	document.write(`<li>Números del array ${elemento} </li>`);
});
	document.write(`</ul>`);
}

const numeros = new Array(6);

for(let i = 0; i < numeros.length; i++) {
	numeros[i] = parseInt(prompt("introduce un numero: ",0));
}

// imprime el array
mostrarArray(numeros, 'numeros introducidos');

console.log(numeros);

// ordena numericamente, no alfabeticamente
console.log(numeros.sort( (a,b) => a-b ));
mostrarArray(numeros, 'ordenado');

// invierte el orden del array
console.log(numeros.reverse( (a,b) => a-b ));
mostrarArray(numeros, 'revertido');

document.write(`cantidad de elementos en el array ${numeros.length}`)

const busqueda = parseInt(prompt("busca un numero", 0));
const posicion = numeros.findIndex( (numero) => numero == busqueda );

if(posicion == -1){
	document.write("<h2>No Encontrado</h2>");
} else {
	document.write("<h2>Encontrado</h2>");
	document.write("<h3>Posición de la busqueda es el: "+posicion+"</h3>");
}
~~~

