'use strict'

// comprobar si esta disponible el localstorage en el navegador
if(typeof(Storage) !== 'undefined') {
	console.log("localstorage disponible");
} 
else {
	console.log(("localstorage NO disponible"))
}

// añadir valores al localstorage
/* setItem guarda la key y su valor*/

// localStorage.setItem
localStorage.setItem("titulo1", "Curso Master Javascript");
localStorage.setItem("titulo2", "Curso Master PHP");
localStorage.setItem("titulo3", "Curso Master NodeJs");

// recuperar elemento
/* getItem recupera con la key y muestra su valor */

// localStorage.getItem('titulo');
let item = localStorage.getItem('titulo1');
document.querySelector("#titulo1").innerHTML = `insertando este item <br> ${item}` 
document.querySelector("#titulo2").innerHTML = localStorage.getItem('titulo2'); 
document.querySelector("#titulo3").innerHTML = localStorage.getItem('titulo3'); 

// de esta forma seria la opcion de guardar un usuario JSON
const usuario = {
	nombre: "Jared",
	email: "jared@hola.com",
	web: "jaredlatorre.com",
};
// almacenar el JSON string con (key , JSON.stringify(usuario)); 
localStorage.setItem("json_stringify", JSON.stringify(usuario));

// recuperar un JSON string a JSON object
/* toca pasar el string del key */
let userJson = JSON.parse(localStorage.getItem("json_stringify"));
console.log(userJson);

// mostrar el JSON en el documento html 
document.querySelector("#json").innerHTML = `<div><strong>Objeto JSON</strong></div>nombre: ${userJson.nombre} <br> email: ${userJson.email} <br> web: ${userJson.web} `; 
document.querySelector("#titulo1").innerHTML += `<h4>desde el Object JSON ${userJson.nombre}</h4>`; 

// remover un item, en este caso el key del JSON
// localStorage.removeItem("json_stringify");

// limpia los value pero no las key
// localStorage.clear();
