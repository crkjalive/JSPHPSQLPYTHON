# Funciones y métodos
1. las funciones son un grupo de ordenes agrupados con un nombre en concreto
2. regla de ordenes a ejecutar
3. se crea codigo reutilizable

~~~
'use strict'

function calculadora() { // Defino la funcion
	return "Hola mundo"; // instrucciones a ejecutar
}

console.log(calculadora(), calculadora(), calculadora());
~~~

### Parámetros en las funciones
1. las funciones reciben los parámetros para poder manipularlos atraves de la funcion

~~~
function calculadora(arg1, arg2) {
	let suma = arg1 + arg2;
	let resta = arg1 - arg2;
	let multi = arg1 * arg2;
	let divi = arg1 / arg2;
	console.log(suma);
	console.log(resta);
	console.log(multi);
	console.log(divi);
}

calculadora(5, 6);
calculadora(8, 9);
calculadora(2, 3);
~~~

2. ejecutar funciones
~~~
function calculadora(arg1, arg2) {
	let suma = arg1 + arg2;
	let resta = arg1 - arg2;
	let multi = arg1 * arg2;
	let divi = arg1 / arg2;
	console.log(`${arg1} y ${arg2} `);
	console.log(`suma ${suma}`);
	console.log(`resta ${resta}`);
	console.log(`multi ${multi}`);
	console.log(`divi ${divi}`);
}

for (let i = 0; i <= 10; i++) {
	calculadora(i, 8);
}
~~~

### parametros opcionales
1. ya vienen por defecto
2. parametro flag (que hace algo diferente)
~~~

function calculadora(arg1, arg2, mostrar = false) {

    let suma = arg1 + arg2;
    let resta = arg1 - arg2;
    let multi = arg1 * arg2;
    let divi = arg1 / arg2;

    if (mostrar == false) {
        console.log(`${arg1} y ${arg2} `);
        console.log(`suma ${suma}`);
        console.log(`resta ${resta}`);
        console.log(`multi ${multi}`);
        console.log(`divi ${divi}`);
    } else {
        document.write(`${arg1} y ${arg2} `);
        document.write(`suma ${suma}`);
        document.write(`resta ${resta}`);
        document.write(`multi ${multi}`);
        document.write(`divi ${divi}`);
    }
}

for (let i = 0; i <= 10; i++) {
    calculadora(i, 8);
}

calculadora(5, 9, true);

~~~
3. si el 3 parametro lo pasamos como variable, podemos alterar el comportamiento de la funcion
4. parametros inicializados pero que no son obligatorios a la hora de invocar la funcion

### Funciones dentro de otras funciones 
1. vamos a refactorizar el codigo de la funcion
2. funciones que muestren menos codigo 

***Code a refactorizar***

~~~
'use strict'

function calculadora(arg1, arg2, mostrar = false) {

    let suma = arg1 + arg2;
    let resta = arg1 - arg2;
    let multi = arg1 * arg2;
    let divi = arg1 / arg2;

    if (mostrar == false) {
        console.log(`${arg1} y ${arg2} `);
        console.log(`suma ${suma}`);
        console.log(`resta ${resta}`);
        console.log(`multi ${multi}`);
        console.log(`divi ${divi}`);
    } else {
        document.write(`${arg1} y ${arg2} `);
        document.write(`suma ${suma}`);
        document.write(`resta ${resta}`);
        document.write(`multi ${multi}`);
        document.write(`divi ${divi}`);
    }
}

for (let i = 0; i <= 10; i++) {
    calculadora(i, 8);
}

calculadora(5, 9, false);
~~~

***Code todo por funciones*** 
~~~
function porConsola(arg1, arg2) {
	let suma = arg1 + arg2;
	let resta = arg1 - arg2;
	let multi = arg1 * arg2;
	let divi = arg1 / arg2;
	console.log(`${arg1} y ${arg2} `);
	console.log(`suma ${suma}`);
	console.log(`resta ${resta}`);
	console.log(`multi ${multi}`);
	console.log(`divi ${divi}`);
}

function porNavegador(arg1, arg2) {
	let suma = arg1 + arg2;
	let resta = arg1 - arg2;
	let multi = arg1 * arg2;
	let divi = arg1 / arg2;
	document.write(`${arg1} y ${arg2} `);
	document.write(`suma ${suma}`);
	document.write(`resta ${resta}`);
	document.write(`multi ${multi}`);
	document.write(`divi ${divi}`);
}

function calculadora(arg1, arg2, mostrar = false) {

	if (mostrar == false) {
		porConsola(arg1, arg2);
	} else {
		porNavegador(arg1, arg2);
	}
}

for (let i = 0; i <= 10; i++) {
	calculadora(i, 8);
}

calculadora(5, 9, false);
~~~

### Parámetros REST y SPREAD
1. puede ser que se pasen mas parametros de los que se piden en la funcion
2. con el spread operator podemos recoger el resto de parametros en un array

~~~
'use strict'

// parámetros REST y SPREAD 

// Spread de tipo Rest en el 3er parámetro
function listadoFrutas(fruta1, fruta2, ...demas_frutas) { 
	console.log(`Fruta 1 ${fruta1}`);
	console.log(`Fruta 2 ${fruta2}`);
	console.log(`resto de frutas ${demas_frutas}`);
}

listadoFrutas('Coco', 'Naranja', 'Manzana', 'Kiwi', 'Melon', 'Banano', 'Fresa', 'Sandia', 'Pera');

console.log(typeof(demas_frutas)); // object
~~~
3. de esta manera podemos capturar los demas parametros de tipo rest

~~~
'use strict'

// parámetros REST y SPREAD 

// Spread de tipo Rest en el 3er parámetro
function listadoFrutas(fruta1, fruta2, ...demas_frutas) { 
	console.log(`Fruta 1 ${fruta1}`);
	console.log(`Fruta 2 ${fruta2}`);
	console.log(`${demas_frutas}`);
}

let frutas = ['Piña', 'Ciruela', 'Coco', 'Naranja', 'Manzana', 'Kiwi', 'Melon', 'Banano', 'Fresa'];

// concatenacion con SPREAD OPERATOR 
listadoFrutas( ...frutas, 'Sandia', 'Pera' )

/* resultado
Fruta 1 Piña
Fruta 2 Ciruela
Coco,Naranja,Manzana,Kiwi,Melon,Banano,Fresa,Sandia,Pera */
~~~

### Funciones anonimas
1. consiste que esta funcion no tiene nombre, que normalmente se utiliza para hacer callbacks
~~~
const pelicula = (nombre) => {
	return `La pelicula es ${nombre}`;
}
console.log(pelicula('advengers'));
~~~
2.  de esta manera contenemos una funcion anonima en una variable

### Callback
1. es una funcion que se ejecuta dentro de otra funcion

### Funciones de callbacks
~~~
function sumame(num1, num2, sumaMuestra, sumaPorDos) {
	let sumar = num1 + num2;

	sumaMuestra(sumar);
	sumaPorDos(sumar);

	return sumar;
}

sumame(4, 5, function(dato){
	console.log(`La suma es: ${dato}`);
},
function (dato) {
	console.log(`la suma por dos es: ${(dato*2)}`);
});
~~~

2. invocamos la función, y sus parámetros con los callbacks, que son funciones anónimas


### Funciones de fecha
~~~
function sumame(num1, num2, sumaMuestra, sumaPorDos) {
	let sumar = num1 + num2;

	sumaMuestra(sumar);
	sumaPorDos(sumar);

	return sumar;
}

sumame(4, 5,(dato) => { 
	document.write(`La suma es: ${dato}`);
}, 
(dato) => { 
	document.write(`la suma por dos es: ${(dato*2)}`);
});
~~~

***funciones de flecha***

~~~
function sumame(num1, num2, sumaMuestra, sumaPorDos) {
	let sumar = num1 + num2;

	sumaMuestra(sumar);
	sumaPorDos(sumar);

	return sumar;
}

sumame(9, 7, 
	dato => document.write(`La suma es: ${dato} <br/>`),
	dato => document.write(`La suma por dos es: ${(dato*2)} <br/>`)
);
~~~
1. las funciones de flecha simplifican la sintaxis de una funcion, quitando llaves, parentesis, y agregando flecha directamente a lo que devuelve
2. los parametros se pasan directamente si hay, si no se dejan.
### Sintaxis
~~~
const fun = (nombre) => console.log("hola Mundo", nombre);
fun('Wizard')
~~~

### El ambito de las variables
1. el ambito de las variables segun su scope
2. global ***var***
3. local ***let***
4. constante ***const*** 
~~~
const holaMundo = (texto) => {
	var hola_mundo = "Texto dentro de la funcion";
	console.log(texto);
	console.log(numero);
}
var numero = 12;
var texto = "hola mundo soy una variable global";
holaMundo(texto);
~~~

### convertir un numero a un string
### volver un numero a string
~~~
let numero = 12;
console.log(numero+7); // 19
console.log(numero); // 12
console.log(numero.toString()+8); // 128
~~~

### Metodos para procesar textos

***funciones texto***

~~~
let numero = 444;
let texto1 = "Bienvenidos al curso de Javascript";
let texto2 = "mAsteR De VicTor RoBlEs";

let dato = numero.toString();
console.log(typeof dato); // string

let texto = texto1.toUpperCase();
console.log(texto);

let textin = texto2.toLowerCase();
console.log(textin);
~~~

***longitud del texto***

~~~
let nombre = "Wizard";
console.log(nombre.length) // 6

let elementos = ["Hola", "Mundo"];
console.log(elementos.length); // 2
~~~

***concat - concatenar uniendo textos***

~~~
let textoTotal = texto1.concat(" ", texto2);
console.log(textoTotal);
~~~
___

# Metodos de busqueda
### metodos y propiedades para hacer busquedas

1. indexOf() ***buscar en cadenas de texto***

***funciones texto***

~~~
let texto = "Bienvenidos al curso de Javascript";
~~~

***busqueda de texto en la cadena***

~~~
let busqueda = texto.indexOf('curso');
console.log(busqueda); // 15
~~~

***funciona igual al indexOf***

~~~
let busqueda1 = texto.search('llorar');
console.log(busqueda1); // -1
~~~

***metodo match devuelve una coleccion con los resultados***

~~~
let busqueda2 = texto.match('curso');
console.log(busqueda2); // -1
~~~

~~~
Array [ "curso" ]
0: "curso"
groups: undefined
index: 15
input: "Bienvenidos al curso de Javascript"
length: 1
<prototype>: Array []
~~~

***toma desde el caracter 14 y 8 letras más***

~~~
let busqueda3 = texto.substr(14, 8);
console.log(busqueda3); // curso d
~~~

***para sacar una letra en concreto***

~~~
let busqueda4 = texto.charAt(24);
console.log(busqueda4); // J
~~~

***verifica si el string comienza con, devolviendo true o false***

~~~
let busqueda5 = texto.startsWith('Bienveni');
console.log(busqueda5); // true
~~~

***busca si terina el string con, devolviendo true o false***

~~~
let busqueda6 = texto.endsWith('cript');
console.log(busqueda6); // true
~~~

***includes, busqueda si contiene ese string***

~~~
let busqueda7 = texto.includes('al curso');
console.log(busqueda7); // true
~~~

### Funciones de remplazo

***funciones texto***  

let texto = "Bienvenidos al curso de Javascript";

***busqueda de texto en la cadena***

let busqueda = texto.indexOf('curso');
console.log(busqueda); // 15

***funciona igual al indexOf***

let busqueda1 = texto.search('llorar');
console.log(busqueda1); // -1

***metodo match devuelve una coleccion con los resultados***

let busqueda2 = texto.match('curso');
console.log(busqueda2); // -1

~~~
Array [ "curso" ]
0: "curso"
groups: undefined
index: 15
input: "Bienvenidos al curso de Javascript"
length: 1
<prototype>: Array [] 
~~~

***toma desde el caracter 14 y 8 letras más***

let busqueda3 = texto.substr(14, 8);  
console.log(busqueda3); // curso d

***para sacar una letra en concreto***

let busqueda4 = texto.charAt(24);  
console.log(busqueda4); // J

***verifica si el string comienza con, devolviendo true o false***

let busqueda5 = texto.startsWith('Bienveni');
console.log(busqueda5); // true

***busca si terina el string con, devolviendo true o false***

let busqueda6 = texto.endsWith('cript');  
console.log(busqueda6); // true

***includes, busqueda si contiene ese string***

let busqueda7 = texto.includes('al curso');  
console.log(busqueda7); // true


## Funciones de busquedas en strings 

~~~
let cadenaDeTexto = "     Hola mundo, vamos a hacer busquedas, con las funciones de reemplazo y de más      ";
console.log(cadenaDeTexto);
~~~

***replace reemplaza cadenas de texto por otro***

let reemplazar = cadenaDeTexto.replace('Hola mundo', 'Holis Jared');
console.log(reemplazar);

***slice rebanada desde el una posicion, hasta el final o hasta otro caracter especifico***

~~~
let rebanada1 = cadenaDeTexto.slice(15);  
let rebanada2 = cadenaDeTexto.slice(15, 30);  
console.log(rebanada1); // os a hacer busquedas, con las funciones de reemplazo y de más
console.log(rebanada2); // os a hacer busq
~~~

***split separa el string entre comillas y agrega en un array, separando las palabras***

let split = cadenaDeTexto.split(" ");
console.log(split); 

~~~
array (14)
0: "Hola"
1: "mundo,"
2: "vamos"
3: "a"
4: "hacer"
5: "busquedas,"
6: "con"
7: "las"
8: "funciones"
9: "de"
10: "reemplazo"
11: "y"
12: "de"
13: "más"
~~~

***trim funcion que quita los espacios al inicio y al final, limpiando el string***

let trimm = cadenaDeTexto.trim();
console.log(trimm);


# Plantillas de texto en javascript
1. back this, o comillas invertidas
me sirbe para crear plantillas, y sustituir las variables

***plantillas de texto***

~~~
let nombre = prompt('dame tu nombre: ');
let apellido = prompt('dame tu apellido: ');
~~~

***let nombreCompleto = "mi nombre es "+ nombre + " mi apellido es " + apellido;***

~~~
let nombreCompleto = `
	<h2>plantillas o back this</h2>
	<h3>mi nombre es ${nombre}</h3>
	<h3>mi apellido es ${apellido}</h3>
`;

document.write(nombreCompleto);
~~~
