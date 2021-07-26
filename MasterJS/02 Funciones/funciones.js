'use strict'

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