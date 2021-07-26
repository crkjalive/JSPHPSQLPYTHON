'use strict'

// plantillas de texto

let nombre = prompt('dame tu nombre: ');
let apellido = prompt('dame tu apellido: ');

// let nombreCompleto = "mi nombre es "+ nombre + " mi apellido es " + apellido;

let nombreCompleto = `
	<h2>plantillas o back this</h2>
	<h3>mi nombre es ${nombre}</h3>
	<h3>mi apellido es ${apellido}</h3>
`;
document.write(nombreCompleto);
