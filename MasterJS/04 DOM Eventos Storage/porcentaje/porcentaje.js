const porciento = (valor, porciento) =>{
	let operacion = valor * porciento;
	return operacion;
}

const visor = document.getElementById('visor__green');
const valor = document.getElementById('valor__green');
const enviar = document.getElementById('enviar__green');

let porcentaje = 0.19


enviar.addEventListener('click', ()=>{
	let valorReal = parseInt(valor.value);
	// console.log("es NaN" + valorReal)

	if(valorReal <= 0){
		console.log("aqui entra 1")
		return false;
	} 
	else if (valor.value == ""){
		visor.textContent = "no hay valor";
		console.log("esta vacio entra aqui 2")
		return false;

	}
	else if (!isNaN(valorReal)){
		let mostrar = `Más IVA del ${porcentaje * 100}% son ${porciento(valorReal, porcentaje)} Total ${porciento(valorReal, porcentaje) + valorReal}`
		visor.textContent = mostrar;
		// console.log("aqui soy un numero + 2",valorReal + 2)
		return false;

	}
	else if (valorReal){

		console.log(valorReal+2);

	}
	else {

		visor.textContent = `${valor.value} No es un valor operable`;
		console.log("por defecto")
	}
})

