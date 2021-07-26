'use strict'

// funciones
const cambiarColor = () => {

	let bg = h1.style.backgroundColor;
	if (bg == "lightgreen") {
		h1.style.backgroundColor = 'dodgerblue';
	} else {
		h1.style.backgroundColor = 'lightgreen';
	}
	return true;
}

// captura de elementos
const boton = document.getElementById('boton');
const h1 = document.getElementById('h1');
const input = document.getElementById('inp_nombre');

// estilos
boton.style.backgroundColor = 'orange';
boton.style.padding = '2em';
boton.style.border = 'none';
h1.style.backgroundColor = 'lightgreen';
input.style.width = '80%'
input.style.margin = '0 auto'
input.style.fontSize = '2em'

// eventos
boton.addEventListener('onclick', ()=> {
	cambiarColor();
});

h1.addEventListener('mouseover', ()=> {
	h1.style.backgroundColor = 'red';	
});

h1.addEventListener('mouseout', ()=> {
	h1.style.backgroundColor = 'gold';	
});

input.addEventListener('focus', ()=> {
	h2.style.backgroundColor = 'gold';
	h2.textContent = "hiciste click dentro del input evento focus";
});

input.addEventListener('blur', ()=> {
	h2.style.backgroundColor = 'gold';
	h2.textContent = "saliste del input evento blur";
	input.value = "";
	input.placeholder = "presiona teclas";
});

input.addEventListener('keydown', (event)=> {
	h2.style.backgroundColor = 'gold';
	h2.textContent = "esta presionando teclas";

	console.log("Pulsaste la tecla", String.fromCharCode(event.keyCode));
});


input.addEventListener('keyup', ()=> {
	let mimimi = '';
	mimimi = input.value;
	h1.textContent = mimimi
	h2.style.backgroundColor = 'gold';
	h2.textContent = "soltaste la tecla";
});

input.addEventListener('keypress', ()=> {
	h2.style.backgroundColor = 'gold';
});