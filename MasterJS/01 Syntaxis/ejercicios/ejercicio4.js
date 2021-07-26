'use strict'
/* imprimir los impares entre un rango de números 
introducidos por prompt */

let numero1 = parseInt(prompt("numero 1: "));
let numero2 = parseInt(prompt("numero 2: "));

while(numero1 < numero2) {
	numero1++;

	if (numero1 %2 != 0){
		console.log(`El numero ${numero1} es impar`);
	}
}