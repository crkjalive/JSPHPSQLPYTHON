'use strict'

const formPeliculas =  document.querySelector("#formPeliculas");
const list =  document.querySelector("#list");
const add =  document.querySelector("#add");
const addMovie =  document.querySelector("#addMovie");
const limpieza =  document.querySelector("#limpieza");
const quitar =  document.querySelector("#quitar");

// el formulario detecta el submit el cualquier boton, ya que trabaja sobre ese evento
add.addEventListener('click', () => {
	if(addMovie.value != "" && isNaN(addMovie.value) ){
		localStorage.setItem(addMovie.value, addMovie.value);
	}
	recorrido();

});

limpieza.addEventListener('click', ()=> {
	localStorage.clear();

});

addMovie.addEventListener('focus', ()=>{
	addMovie.value = ''
	recorrido();
})

document.addEventListener('focus', ()=>{
	//console.log(localStorage);
	recorrido();
})

quitar.addEventListener('click', ()=>{
	localStorage.removeItem(addMovie.value);
	addMovie.value = ''

	recorrido();
})

const recorrido = () => {
	list.textContent = "";
	const ol = document.createElement('ol');
	// recorrido del localStorage y su contenido
	for(let i in localStorage){
		// verifica que el tipo sea un string para dejarlo ingresar
		if(typeof localStorage[i] == 'string'){
			let li = document.createElement('li');
			li.className = "borra"
			li.textContent = localStorage.getItem([i]);
			ol.append(li)
			list.append(ol);
		}
	}
}

console.log(localStorage);