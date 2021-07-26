'use strict'
/* hacer un programa que nos diga si un numero es 
par o impar */

let numero = parseInt(prompt("numero: "));

while (isNaN(numero)) {
	numero = parseInt(prompt("debe de ser un numero: "));
}
	
if (numero % 2 == 0) {
	console.log(`el numero ${numero} es par`);
} else {
	console.log(`el numero ${numero} es impar`);
}