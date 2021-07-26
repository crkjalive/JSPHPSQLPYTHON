'use strict'

// funciones de flecha
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

const fun = (nombre) => console.log("hola Mundo", nombre);
fun('Wizard');

// volver un numero a string
let numero = 12;
console.log(numero+7);
console.log(numero);
console.log(numero.toString()+8);