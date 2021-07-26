'use strict'
/* programa que reciba 2 numeros y que nos diga cual 
es mayor el menor y/o si son iguales */

let numero1 = parseInt(prompt("Escriba el primer número: ",0));

while(isNaN(numero1) || numero1 <= 0){
	numero1 = parseInt(prompt("Escriba el primer número: ",0));
}

let numero2 = parseInt(prompt("Escriba el segundo número: ",0));

while(isNaN(numero2) || numero2 <= 0){
	numero2 = parseInt(prompt("Escriba el segundo número: ",0));
}


if (numero1 > numero2) {
	alert(`${numero1} es mayor que ${numero2}`);
} else if (numero1 < numero2) {
	alert(`${numero1} es menor que ${numero2}`);
} else {
	alert(`${numero1} es igual que ${numero2}`);
}
 
/* buscar que funcion detecta letras y numeros 
en los prompt, o si contiene letras */