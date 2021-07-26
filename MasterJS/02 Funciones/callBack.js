'use strict'

const pelicula = (nombre) => {
	return `La pelicula es ${nombre}`;
}
console.log(pelicula('advengers'));

// funciones de callbacks
function sumame(num1, num2, sumaMuestra, sumaPorDos) {
	let sumar = num1 + num2;

	sumaMuestra(sumar);
	sumaPorDos(sumar);

	return sumar;
}

// invocamos la función, y sus parámetros con los callbacks, que son funciones anónimas
sumame(4, 5, 
	function(dato){
			console.log(`La suma es: ${dato}`);
	},
	function (dato) {
		console.log(`la suma por dos es: ${(dato*2)}`);
	}
);