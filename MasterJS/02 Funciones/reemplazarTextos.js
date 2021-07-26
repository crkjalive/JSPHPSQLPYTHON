'use strict'

let cadenaDeTexto = "     Hola mundo, vamos a hacer busquedas, con las funciones de reemplazo y de más      ";
console.log(cadenaDeTexto);

// replace reemplaza cadenas de texto por otro
let reemplazar = cadenaDeTexto.replace('Hola mundo', 'Holis Jared');

console.log(reemplazar);

// slice rebanada desde el una posicion, hasta el final o hasta otro caracter especifico
let rebanada1 = cadenaDeTexto.slice(15);
let rebanada2 = cadenaDeTexto.slice(15, 30);

console.log(rebanada1); // os a hacer busquedas, con las funciones de reemplazo y de más
console.log(rebanada2); // os a hacer busq

// split separa el string entre comillas y agrega en un array, separando las palabras
let split = cadenaDeTexto.split(" ");

console.log(split); 
/* array (14)
0: "Hola"
1: "mundo,"
2: "vamos"
3: "a"
4: "hacer"
5: "busquedas,"
6: "con"
7: "las"
8: "funciones"
9: "de"
10: "reemplazo"
11: "y"
12: "de"
13: "más"
*/

// trim funcion que quita los espacios al inicio y al final, limpiando el string
let trimm = cadenaDeTexto.trim();
console.log(trimm);