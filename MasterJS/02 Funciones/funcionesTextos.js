'use strict'

// funciones texto
let numero = 444;
let texto1 = "Bienvenidos al curso de Javascript";
let texto2 = "mAsteR De VicTor RoBlEs";

let dato = numero.toString();
console.log(typeof dato); // string

let texto = texto1.toUpperCase();
console.log(texto);

let textin = texto2.toLowerCase();
console.log(textin);

// longitud del texto
let nombre = "Wizard";
console.log(nombre.length) // 6

let elementos = ["Hola", "Mundo"];
console.log(elementos.length); // 2

// concat - concatenar uniendo textos
let textoTotal = texto1.concat(" ", texto2);
console.log(textoTotal);