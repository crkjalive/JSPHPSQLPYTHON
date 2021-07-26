'use strict'

/* tabla de multiplicar de un numero introducido por 
pantalla */

// let numero = parseInt(prompt("numero: "));

for (let t = 1; t <= 15; t++) {
	
	document.write(`<h2>Tabla del ${t} </h2>`);
	
	for (let i = 1; i <= 10; i++) {
	
		document.write(`${t} x ${i} = ${(i*t)} <br/>`);
	
	}

}