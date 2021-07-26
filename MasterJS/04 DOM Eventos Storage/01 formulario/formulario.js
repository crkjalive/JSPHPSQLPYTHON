'use strict'

window.addEventListener('load', ()=>{
	console.log('Dom cargado');


	const formulario = document.querySelector('#formulario');

	formulario.addEventListener('submit', ()=>{
		console.log('submit cap turado');

		let informacion = document.querySelector('#informacion');
		let nombre = document.querySelector('#nombre').value;
		let apellido = document.querySelector('#apellido').value;
		let edad = document.querySelector('#edad').value;

		// Validacion de datos
		if (nombre.trim() == null || nombre.trim().length == 0) {
			alert("El nombre no es valido");
			return false;
		}
		if (apellido.trim() == null || apellido.trim().length == 0) {
			alert("El apellido no es valido");
			return false;
		}
		if (edad == null || edad <= 0 || isNaN(edad)) {
			alert("El edad no es valida");
			console.log(edad)
			return false;
		}

		const name = document.createElement('h2');
		name.className = "nombre"
		const lastName = document.createElement('h2');
		lastName.className = "apellido"
		const age = document.createElement('h2');
		age.className = "edad"

		name.textContent = nombre;
		lastName.textContent = apellido;
		age.textContent = edad;

		informacion.append(name, lastName, age);

		console.log(nombre, apellido, edad);

	})



});