'use strict'

var pais = 'Colombia';
var contienente = 'América';
document.write(pais, ' ',contienente);

var lenguaje = "javascript";
console.log(lenguaje)

if(true){
	let lenguaje = "python";
	console.log(lenguaje);
}
console.log(lenguaje)

document.write('<br/>');

let num1 = 7;
let num2 = 6;
let resultado = num1 + num2;
document.write(`El resultado es ${resultado} <br/>`);
resultado = num1 - num2;
document.write(`El resultado es ${resultado} <br/>`);
resultado = num1 / num2;
document.write(`El resultado es ${resultado} <br/>`);
resultado = num1 * num2;
document.write(`El resultado es ${resultado} <br/>`);


let edad = 18;

if (edad >= 18) {
	document.write("eres mayor de edad")
} else if (edad <= 10 ) {
	document.write("eres un niño")
} else {
	document.write("eres menor de edad")
}

document.write('<br/>')

let eded = 18;
let imprime = '';

switch (eded) {
	case 18:
		imprime = 'acabas de cumplir la mayoria de edad';
	break;
	
	case 25:
		imprime = 'ya eres un adulto';
	break;

	case 40:
		imprime = 'crisis de los 40';
	break;

	default:
		imprime = 'tu edad es neutral';
	break;
}

document.write(imprime)

document.write('<br/>')

let numero100 = 30;

for (let i = 0; i < numero100; i++) {
	document.write(i);
	// debugger
}


let year = 2020;
while (year <= 2051) {
	console.log('Estamos en el año: ', year);
	year++;
}
document.write('<br/>')

let years = 15; 

do {
	document.write('se va a ejecutar asi no se haya validado la condicion <br/>')
	years++;
} while (years != 20)

