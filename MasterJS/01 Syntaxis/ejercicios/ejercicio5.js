'use strict'
/* mostrar todos los números divisores de un 
número introducido por pantalla */

let numero = parseInt(prompt("numero: "));

for (let i = 1; i <= numero; i++) {

	if (numero%i == 0) {
		console.log('Divisor: ',i);
	}
}