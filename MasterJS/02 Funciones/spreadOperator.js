'use strict'

// parámetros REST y SPREAD 

// Spread de tipo Rest en el 3er parámetro
function listadoFrutas(fruta1, fruta2, ...demas_frutas) { 
	console.log(`Fruta 1 ${fruta1}`);
	console.log(`Fruta 2 ${fruta2}`);
	console.log(`${demas_frutas}`);
}

let frutas = ['Piña', 'Ciruela', 'Coco', 'Naranja', 'Manzana', 'Kiwi', 'Melon', 'Banano', 'Fresa'];

// concatenacion con SPREAD OPERATOR 
listadoFrutas( ...frutas, 'Sandia', 'Pera' )

/* resultado
Fruta 1 Piña
Fruta 2 Ciruela
Coco,Naranja,Manzana,Kiwi,Melon,Banano,Fresa,Sandia,Pera */

