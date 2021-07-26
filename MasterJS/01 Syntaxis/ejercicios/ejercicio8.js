'use strict'

/* crear una calculadora */

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