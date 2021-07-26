'use strict'
/* mostrar los numeros que hay entre el primero que 
introduzca el usuario y el segundo numero que introduzca 
el usuario */

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
