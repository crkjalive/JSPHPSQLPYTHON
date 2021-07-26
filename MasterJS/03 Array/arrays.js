'use strict'
// arrays

const mostrarArray = (elementos, textoCustom = "") => {
	document.write(`<h1>Mostar array ${textoCustom}</h1>`);
	document.write(`<ul>`);
	elementos.forEach( (elemento, index) => {
	document.write(`<li>Números del array ${elemento} </li>`);
});
	document.write(`</ul>`);
}

const numeros = new Array(6);

for(let i = 0; i < numeros.length; i++) {
	numeros[i] = parseInt(prompt("introduce un numero: ",0));
}

// imprime el array
mostrarArray(numeros, 'numeros introducidos');

console.log(numeros);

// ordena numericamente, no alfabeticamente
console.log(numeros.sort( (a,b) => a-b ));
mostrarArray(numeros, 'ordenado');

// invierte el orden del array
console.log(numeros.reverse( (a,b) => a-b ));
mostrarArray(numeros, 'revertido');

document.write(`cantidad de elementos en el array ${numeros.length}`)

const busqueda = parseInt(prompt("busca un numero", 0));
const posicion = numeros.findIndex( (numero) => numero == busqueda );

if(posicion == -1){
	document.write("<h2>No Encontrado</h2>");
} else {
	document.write("<h2>Encontrado</h2>");
	document.write("<h3>Posición de la busqueda es el: "+posicion+"</h3>");
}