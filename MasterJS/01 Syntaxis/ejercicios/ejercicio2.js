'use strict'
/* utiliza un bucle, mostrando la suma y la media de los numeros hasta introducir el numero 0 y ahi mostrar el resultado */

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