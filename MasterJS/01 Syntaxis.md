## Que aprenderas en Master en JS
1. programacion desde cero
2. JS Moderno
3. JQuery
4. Maquetacion web
5. TypeScript y JS POO 
6. Angular
7. NodeJs
8. Express / REST 
9. MEAN STACK
10. Desarrollo web full-stack

## Programación desde cero 
1. primeros pasos
2. variables
3. tipos de datos
4. operadores
5. condicionales
6. bucles
7. alertas y ventanas 
8. ejercicios
9. funciones
10. arrays
11. ejercicios2

## Herramientas
1. Navegador ***browser***
2. IDE ***entorno de desarrollo***
3. NodeJs ***ejecutar scripts***

## Hola Mundo
1. alert('Hola Mundo'); ***ventana de información***
2. document.write('Hola Mundo'); ***escribir sobre el documento***
3. prompt("Dame tu nombre: "); ***captura de datos por ventana***

## Mostrar por consola del navegador
1. console.log('Hola Mundo'); ***imprime string***
1. console.log(variables); ***imprime variable*** 
1. console.log(2+2); ***imprime operaciones directamente*** 

## Comentarios
1. /* block code.. */
2. // line code.. 

## Modo estricto de Javascript 
impide que yo asigne variables sin averlas declarado
1. ```'use strict'```


## Variables
una variable es un contenedor de información

| declaracion | valor |
|-|-|
| const | const nombre = "Jared";|
| let | let primerNombre = "Kenneth";|
| var | var apellidos = "Latorre Ramos"; | 


1. var ***variable global***
~~~
var pais = 'Colombia'
var contienente = 'América'
document.write(pais, ' ',contienente)
~~~

2. let ***variable con alcance a nivel scope de bloque***
~~~
var lenguaje = "javascript";
console.log(lenguaje)

if(true){
	let lenguaje = "python";
	console.log(lenguaje);
}
console.log(lenguaje)
~~~

3. const ***constante, su contenido no se puede modificar***
~~~
const web = "http://www.google.com"
~~~

## Operadores y tipos de datos 
|no.| operadores | tipo de operador |
|-|-|-|
|1.| ```+ - * / %``` | operadores matematicos |
|2.| ```<> <= >= == != === = !``` | comparacion | 
|3.| ```and && y or ll``` | operador condicional |
|4.| ```true false``` | validadores |
|5.| ```string, int, bool, float``` | tipos de datos en Js |
|6.| ```++ -- += -= **``` | incrementos y decrementos |

## Convierte el tipo de dato
1. Number() ***combierte un string númerico a número***
2. parseInt() ***transforma a entero***
3. parseFloat() ***transforma a flotante***
3. String() ***transforma a texto***

## Que tipo de dato es
saber el tipo de dato de una variable
1. typeof(variable) ***me devuelve el tipo de dato de la variable***

# Estructuras de control

### debugger;
me ayuda a debuggear mientras va iterando

## if 
la condicional if lo que hace es evaluar si es verdadero o falso, la condición  
1. if (condicion) {bloque} else if (condicion) {bloque} else {bloque}  
~~~
let edad = 18;

if (edad >= 18) {
	document.write("eres mayor de edad")
} else if (edad <= 10 ) {
	document.write("eres un niño")
} else {
	document.write("eres menor de edad")
}
~~~

## switch
estructura de control, de posibles casos
1. switch case 
~~~
let edad = 21;
let imprime = '';

switch (edad) {
	case 21:
		imprime = 'eres mayor de edad';
	break;

	case 18:
		imprime = 'eres menor de edad en EU';
	break;

	case 30:
		imprime = 'crisis de los 30';
	break;

	default:
		imprime = 'edad por default';
	break;
}
console.log(imprime);
~~~

## for 
estructura de control ciclo ***for*** que repite varias veces sí la condición es true, cuando sea falsa detendra su ejecución
~~~
let numero100 = 100;

for (let i = 0; i < numero100; i++) {
	document.write(i);
}
~~~

## while
estructura de ciclo o bucle
~~~
let year = 2020;
while (year <= 2051) {
	console.log('Estamos en el año: ', year);
	year++;
}
~~~

## do while
esta instruccion se ejecutara por lo menos 1 vez 
~~~
let years = 15; 

do {
	document.write('se va a ejecutar asi no se haya validado la condicion <br/>')
	years++;
} while (years != 20)
~~~

### break
con break cortamos la ejecucion del bucle, en algun momento que necesitemos salir de la ejecución


# Alertas y Ventanas y PopUp
1. alert(); ***ventana de alerta***
2. confirm(); ***ventana de confirmacion***
~~~
let mi_resultado = confirm("Estas seguro de querer continuar?");
console.log(mi_resultado);
~~~
3. prompt("pregunta: ", default);
~~~
let mi_resultado = prompt("Que edad tienes? ",18);
console.log(mi_resultado);
~~~
los datos que se capturan con prompt siempre son string,  
si requiere otro tipo de dato, debe cambiar su tipo de dato
___ 

# Ejercicios
1. programa que reciba 2 numeros y que nos diga cual es mayor, cual es el menor o si son iguales
~~~
'use strict'

let numero1 = parseInt(prompt("Escriba un número: ",0));
let numero2 = parseInt(prompt("Escriba otro número: ",0));

if (numero1 > numero2) {
	alert(`${numero1} es mayor que ${numero2}`);
} else if (numero1 < numero2) {
	alert(`${numero1} es menor que ${numero2}`);
} else {
	alert(`${numero1} es igual que ${numero2}`);
}
~~~
2. utiliza un bucle, mostrando la suma y la media de los numeros hasta introducir el numero 0 y ahi mostrar el resultado
~~~
'use strict'

var suma = 0;
var contador = 0;

do {
	var numero = parseInt(prompt("numeros a sumar y promediar: "));
	suma = suma + numero;
	contador++;
	console.log(suma)
	console.log(contador)

} while (numero != 0)

document.write("suma total ", suma ,"<br/>");
document.write("promedio ", (suma/(contador-1)) ,"<br/>");
~~~
3. mostrar los numeros que hay entre el primer numero que introduzca el usuario y el segundo numero que introduzca el usuario
~~~
'use strict'

let rango = [];
let numero1 = parseInt(prompt("numero 1: "));
let numero2 = parseInt(prompt("numero 2: "));

rango[0] = numero1;
rango[1] = numero2;

console.log(rango[0])//50
console.log(rango[1])//0

if (rango[0] > rango[1]) {

	for (let i = rango[0]; i >= rango[1]; i--){
		console.log(i);
	}
}

if (rango[0] < rango[1]) {
	
	for (let i = rango[0]; i <= rango[1]; i++){
		console.log(i);
	}
}
~~~
4. mostar impares introducidos entre dos numeros
~~~
'use strict'

let numero1 = parseInt(prompt("numero 1: "));
let numero2 = parseInt(prompt("numero 2: "));

while(numero1 < numero2) {
	numero1++;

	if (numero1 %2 != 0){
		console.log(`El numero ${numero1} es impar`);
	}
}
~~~
5. mostrar todos los numeros divisores de un numero introducido por pantalla
~~~
'use strict'

let numero = parseInt(prompt("numero: "));

for (let i = 1; i <= numero; i++) {

	if (numero%i == 0) {
		console.log('Divisor: ',i);
	}
}
~~~
6. hacer un programa que nos diga si un numero es par o impar
~~~
'use strict'

let numero = parseInt(prompt("numero: "));

while (isNaN(numero)) {
	numero = parseInt(prompt("debe de ser un numero: "));
}
	
if (numero % 2 == 0) {
	console.log(`el numero ${numero} es par`);
} else {
	console.log(`el numero ${numero} es impar`);
}
~~~
7. tabla de multiplicar de un numero introducido por pantalla
~~~
'use strict'

let numero = parseInt(prompt("numero: "));

for (let i = 0; i <= 10; i++) {
	console.log(`la tabla del ${numero} x ${i}:`, (numero * i));
}
~~~
8. Todas las tablas de multiplicar
~~~
for (let t = 1; t <= 15; t++) {
	document.write(`<h2>Tabla del ${t} </h2>`);
	for (let i = 1; i <= 10; i++) {
		document.write(`${t} x ${i} = ${(i*t)} <br/>`);
	}
}
~~~
9. calculadora 
~~~
'use strict'

let numero1 = parseInt(prompt("numero: "));
let numero2 = parseInt(prompt("numero: "));

while (numero1 < 0 || numero2 < 0 || isNaN(numero1 || isNaN(numero2))) {

	numero1 = parseInt(prompt("numero: "));
	numero2 = parseInt(prompt("numero: "));
}

let resultado = 
`La suma es: ${(numero1+numero2)} <br/>`+ 
`La resta es: ${(numero1-numero2)} <br/>`+
`La multiplicacion es: ${(numero1*numero2)} <br/>`+
`La division es: ${(numero1/numero2)} <br/>`;

document.write(resultado);
~~~