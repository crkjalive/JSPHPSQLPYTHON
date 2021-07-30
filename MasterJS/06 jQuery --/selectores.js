'use strict'

$(document).ready(()=>{

	// selector por ID

	$("#rojo").css("background","red")
		.css("color","white");

	$("#amarillo").css("background","yellow")
		.css("color","black");

	$("#verde").css("background","green")
		.css("color","white");

	// selector por class

	let mi_clase = $(".zebra");
	mi_clase.click(()=>{
		mi_clase.css('background','blue');
	})

	// selector por etiqueta
	
	let parrafos = $('p');
	parrafos.click(()=>{
		parrafos.css('background','blue');
	})

	// selector por atributo

	$('[title="google"]').css('background','#ccc');
	$('[title="facebook"]').css('background','blue');


	console.log('Cargado jQuery');
});