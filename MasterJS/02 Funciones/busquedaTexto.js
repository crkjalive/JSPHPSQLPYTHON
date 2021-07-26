'use strict'

// funciones texto
let texto = "Bienvenidos al curso de Javascript";

// busqueda de texto en la cadena
let busqueda = texto.indexOf('curso');
console.log(busqueda); // 15

// funciona igual al indexOf
let busqueda1 = texto.search('llorar');
console.log(busqueda1); // -1

// metodo match devuelve una coleccion con los resultados
let busqueda2 = texto.match('curso');
console.log(busqueda2); // -1

/* 
Array [ "curso" ]
0: "curso"
groups: undefined
index: 15
input: "Bienvenidos al curso de Javascript"
length: 1
<prototype>: Array [] */

// toma desde el caracter 14 y 8 letras más
let busqueda3 = texto.substr(14, 8);
console.log(busqueda3); // curso d

// para sacar una letra en concreto
let busqueda4 = texto.charAt(24);
console.log(busqueda4); // J

// verifica si el string comienza con, devolviendo true o false
let busqueda5 = texto.startsWith('Bienveni');
console.log(busqueda5); // true

// busca si terina el string con, devolviendo true o false
let busqueda6 = texto.endsWith('cript');
console.log(busqueda6); // true

// includes, busqueda si contiene ese string
let busqueda7 = texto.includes('al curso');
console.log(busqueda7); // true