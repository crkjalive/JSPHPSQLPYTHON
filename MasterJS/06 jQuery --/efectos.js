$(document).ready(()=>{

	//mouseOver mouseOut
	let caja = $('#caja');

	caja.mouseover(()=>{
		$(this).css('background','dodgerblue');
	});

	caja.mouseout(()=>{
		$(this).css('background','glod');
	});


	//Hover recibe 2 parametros callback
	funcion cambiarRojo(){
		$(this).css('background','red');
	}
	funcion cambiarVerde(){
		$(this).css('background','green');
	}

	caja.hover(cambiarRojo,cambiarVerde)

	// click, dobleClick
	caja.click(function(){
		$(this).css('background','blue')
				.css('background','gold');
	});
	caja.dblclick(function(){
		$(this).css('background','pink')
				.css('background','yellow');
	});

	// focus, blur (input) .val==value
	let input = $('#input');

	input.focus(function(){
		$(this).css('border','2px solid red')
		console.log($(this).val();
	});
	input.blur(function(){
		$(this).css('border','2px solid gray')
		console.log($(this).val();
	});

	// mousedown mouseup (teclas del raton)
	let datos = $('#datos');

	datos.mouseup(function(){
		$(this).css('border-color','gray');
	});
	datos.mousedown(function(){
		$(this).css('border-color','lime');
	});

	// mousemove (cordenadas del ratón por consola)
	$(document).mousemove(function(){
		console.log(event.clienX);
		console.log(event.clienY);
		$('body').css('cursor', 'none');
		let sigueme = $('#sigueme'); 
		sigueme.css('left', event.clienX);
				.css('top', event.clienY);
	});
});