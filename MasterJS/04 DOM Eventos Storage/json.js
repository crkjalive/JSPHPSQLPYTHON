'use strict';

window.addEventListener('load', ()=> {

const pelicula = {
	title: "Batman y Robin",
	origin: "USA",
	year: 1997,
};

const peliculas = [
	{title:"Ironman",origin:"USE",year:2008},
	{title:"La vida es bella",origin:"alemania",year:1997},
	pelicula,
];
let caja_peliculas = document.querySelector("#peliculas");


for (let index in peliculas) {
	let p = document.createElement("p");
	p.append(`${peliculas[index].title} - ${peliculas[index].year}`);
	caja_peliculas.append(p);

	// por consola
	console.log(peliculas[index]);
}


});






















