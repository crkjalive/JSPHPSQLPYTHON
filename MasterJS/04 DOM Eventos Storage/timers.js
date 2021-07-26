'use strict'

window.addEventListener('load', () => {
	
	const h1 = document.querySelector("#h1");
	const fechaHora = document.querySelector("#timer");
	const crono = document.querySelector('#crono');
	const iniciar = document.querySelector('#iniciar');
	const detener = document.querySelector('#detener');

function intervalo(){

	const valor = 60 

	let conteoRegresivo = valor;

	const tiempo = setInterval( ()=> {
		
		console.log(conteoRegresivo);
		
		let fecha = new Date;
		fechaHora.textContent = fecha;
			

		if (conteoRegresivo > 1) {
			
			if( h1.style.backgroundColor == 'lime'){
				h1.style.backgroundColor = 'dimgray'
				h1.style.color = 'white'
				h1.style.fontSize = 'white'
				crono.textContent = conteoRegresivo;
				conteoRegresivo = conteoRegresivo - 1;
			} else {
				h1.style.backgroundColor = 'lime'
				h1.style.color = 'black'
				crono.textContent = conteoRegresivo;
				conteoRegresivo = conteoRegresivo - 1;
			}
		} 
		else{
			h1.style.backgroundColor = 'lime'
			h1.style.color = 'black'
			crono.textContent = conteoRegresivo;
			conteoRegresivo = valor;
		}
		return tiempo;
	}, 1000);
}

	iniciar.addEventListener('click', ()=>{
		intervalo();
	});

	// no me funciono el boton detener
	detener.addEventListener('click', ()=>{
		clearInterval(tiempo);
	});

});