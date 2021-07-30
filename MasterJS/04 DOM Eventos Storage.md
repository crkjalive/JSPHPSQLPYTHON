# Javascript a profundidad
1. DOM
2. BOM
3. Eventos
4. Bloque de ejercicios
5. JSON
6. LocalStorage
7. Peticiones Asíncronas
8. Fechas Matemáticas y más

# DOM - Document Object Model
Interaccion con Javascript manipulando el DOM

| Seleccionar Elementos del DOM | descripción|
|-|-|
| document.| accedo al DOM del browser |
| .getElementsById() | selecciono el elemento por su id |
| .getElementsByClassName() | me trae un array con los elementos className |
| .getElementsByTagName() | me trae un array con todos los elementos existentes | 
| .getElementsByName() | me trae el elemento por su name="" |
| .querySelector() | me trae el primer elemento #id .class tagName que encuentre |
| .querySelectorAll() | me trae NodeList o array de todos los elementos .class tagName que encuentre |

| Propiedades del DOM en los Elementos | descripción|
|-|-|
| .innerHTML | accedo al contenido del elemento HTML |
| .style.propiedad | podemos dar estilos de CSS directamente desde Javascript |
| .className | asinamos una clase al elemento desde Javascript |

***HTML***
~~~
<div id="principal__container">
	Texto interno del contenedor
</div>
~~~

***Javascript***
~~~
const principal = document.getElementById('principal__container');
console.log(principal)
~~~

### innerHTML

***Mostar el contenido del elemento***
~~~
const principal = document.getElementById('principal__container').innerHTML;
console.log(principal)
~~~

***Cambiar el contenido del elemento***
~~~
principal.innerHTML = "agregando nuevo contenido de Javascript";
console.log(principal)
~~~

***CSS desde Javascript***

~~~
principal.style.propiedad = "valor";
~~~

| CSS | Propiedades |
|-|-|
|elemento.style.propiedad | valor |

### Ejemplo de alguna propiedades de CSS

~~~
const principal = document.getElementById('principal__container');
principal.innerHTML = "agregando nuevo contenido de Javascript";
console.log(principal)

principal.className = 'principal__container';
principal.style.backgroundColor = 'dodgerblue';
principal.style.padding = '1em';
principal.style.textAlign = 'center';
principal.style.color = 'white';
principal.style.fontSize = '1.2rem';
principal.style.textTransform = 'capitalize';
~~~

***tagName***  

Me trae un array de elementos encontrados
~~~
const divs = document.getElementsByTagName('div');
console.log(divs)
~~~

como accedo a este array de elementos
~~~
const segundoDiv = divs[2];
segundoDiv.innerHTML = 'modificando el div 2 en concreto';
segundoDiv.style.fontSize = '1.2rem';
segundoDiv.style.backgroundColor = 'lime';
~~~

### Ejercicio
~~~
const principal = document.querySelector('#principal__container');
principal.innerHTML = "agregando nuevo contenido de Javascript";
// console.log(principal)

principal.className = 'principal__container';
principal.style.backgroundColor = 'dodgerblue';
principal.style.padding = '1em';
principal.style.textAlign = 'center';
principal.style.color = 'white';
principal.style.fontSize = '1.2rem';
principal.style.textTransform = 'capitalize';

const divs = document.getElementsByTagName('div');
console.log(divs)

const segundoDiv = divs[2];
segundoDiv.innerHTML = 'modificando el div 2 en concreto';
segundoDiv.style.fontSize = '1.2rem';
segundoDiv.style.backgroundColor = 'lime';

const footer = document.querySelector('footer');
console.log(footer)
footer.textContent = '';

for (let elemento = 0; elemento < divs.length; elemento++) {
	let li = document.createElement('p');
	let texto = document.createTextNode(divs[elemento].textContent);
	li.appendChild(texto);
	footer.append(li);
	console.log(divs[elemento]);
}
~~~

### averiguar como dar estilos a diferentes class del mismo elemento
que segun la clase se le aplique el color que uno valla a usar, desde javascript
en CSS solo es agregar los estilos a las class y ya

listo!

~~~
let divs = document.querySelectorAll('div');

console.log(divs)

for (let div in divs){
	if (divs[div].className == 'rojo'){
		divs[div].style.backgroundColor = '#c0c1f3';
	} else if (divs[div].className == 'azul') {
		divs[div].style.backgroundColor = 'dodgerblue';
	} else if (divs[div].className == 'verde') {
		divs[div].style.backgroundColor = 'lightgreen';
	} else if (divs[div].className == 'rosa') {
		divs[div].style.backgroundColor = 'pink';
	}
}
~~~

# BOM - Browser Object Model
Como trabajar con el browser y Javascript

***window***
1. window para acceder a la ventana del navegador
2. estos metodos no toman en cuenta el developer tools del navegador

| objeto | accion |
|-|-|
| window. | 
| window.innerHeight | alto de la ventana en px | 
| window.innerWidth | ancho de la ventana en px |
| screen.height | alto de la pantalla en px |
| screen.width | ancho de la pantalla en px |
| window.location | me muestra la url actual |
| window.location.href = url | abre un nueva url |
| window.open(url) | abre nueva pestaña con la nueva url |
| window.open(url,"", "width=600, height=300") | abre nueva ventana |

~~~
const anchoAlto = () => {
	document.write(`mostramos el alto <h2>window.innerHeight</h2> ${window.innerHeight} </br>`)
	document.write(`mostramos el ancho <h2>window.innerWidth</h2> ${window.innerWidth} </br>`)
}
anchoAlto()

const anchoAltoScreen = () => {
	document.write(`mostramos el alto de la pantalla<h2>screen.height</h2> ${screen.height} </br>`)
	document.write(`mostramos el ancho de la pantalla <h2>screen.width</h2> ${screen.width} </br>`)
}
anchoAltoScreen()

const urlCargada = () => {
	document.write("mostrar la url cargada en el navegador: </br>")
	document.write(window.location)
}
urlCargada()

const redireccionarUrl = (url) => {
	window.location.href = url
}
/* redireccionarUrl("https://google.com") */

const abrirVentana = (url) => {
	/*abre nueva ventana*/
	window.open(url,"", "width=600, height=300");

	/*abre nueva pestaña*/
	window.open(url, "width=600, height=300");
}
/* abrirVentana("https://google.com") */
~~~

# Eventos del navegador
- los eventos sos funciones que se ejecutan cada vez que sucede algo, en interacción del usuario
- ejemplos: movimientos de mouse, click a algun elemento, cuando se escribe en un input, redimensiona la ventana etc. 

***eventos con el mouse***

- existen estos metodos directos en el html

| evento | detalle | zona de accion |
|-|-|-|
| onclick="" | cuando el usuario le de click | html |
| ondblclick="" | cuando el usuario le de 2 click | html |
| onchange="" | si el elemento cambia | html |
| onblur="" | no sé | html |
| onsubmit="return false" | bloquea el envio del formulario |

~~~
<button id="boton" onclick="cambiarColor()">Presioname</button>
~~~

- la forma optima de encapsular estos eventos es con addEventListener

| evento | parametros | zona de accion |
|-|-|-|
| addEventListener() | 'evento', callback | Javascript |
| onclick | si le damos click sobre el elemento | evento |
| mouseover | si nos ponemos sobre el el elemento | evento |
| mouseout | si nos salimos del elemento | evento |
| submit | envia los datos del formulario, el formulario trabaja sobre este evento |

~~~
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

// estilos
boton.style.backgroundColor = 'orange';
boton.style.padding = '2em';
boton.style.border = 'none';
h1.style.backgroundColor = 'lightgreen';

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
~~~
### buscar mas eventos para probar y saber que otros existen

# Eventos del teclado 

| Evento | Acciona |
|-|-|-|
| focus | cuando entro al input | 
| blur | cuando salgo del input | 
| keydown | capturo el evento cuando se oprime una tecla | 
| keypress | evento tecla orpimida | 
| keyup | cuando suelto la tecla libera el evento | 
| String.fromCharCode(event.keyCode) | me muestra la tecla que se orpimio |

~~~
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
~~~

### Se hizo el MIMIMI como práctica de los eventos

# Evento Load
- permite cargar los scripts, cuando ya los elementos han sido cargados en el DOM
- una ventaja es que podemos cargar nuestros script en el head, que es lo mas recomendable

~~~
window.addEventListenner('load', () => {
	// todo el codigo del script
});
~~~

# Timers
- funciones de tiempo

|funciones | accion | parametros |
|-|-|
| setTimeout()  | se ejecutara 1 sola vez | callback, milisegundos (3000) |
| setInterval() | se ejecutara siempre el codigo, cada x segundos | callback, milisegundos (3000) | 
| clearInterval | funcion que frena el bucle del setInterval | la variable que contenga el setInterval |

***setInterval***
~~~
const tiempoIntervalo = setInterval( ()=> {
		console.log('el setInterval se va a ejecutar cada 3 segundos')
	},3000);
~~~

***setTimeout***
~~~
const tiempo = setTimeout( ()=> {
		console.log('el setInterval se va a ejecutar cada 3 segundos')
	},3000);
~~~

***clearInterval***  
~~~
elemento.addEventListener('click', ()=>{
	clearInterval(tiempoIntervalo)
});
~~~

Para volver a iniciar debemos crear una funcion con la variable que contenga el interval
~~~
const start = () => {
	const tiempoIntervalo = setInterval( ()=> {
		console.log('el setInterval se va a ejecutar cada 3 segundos')
	},3000);
	return tiempoIntervalo;
}
~~~

luego ejecutar la funcion, desde el elemento que lo active 
~~~
elemento.addEventListener('click', ()=>{
	start();
});
~~~

# toca hacer el boton detener
***Código final***
~~~
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
~~~
***hice el cronometro de ensayo***

# Ejercicio completo

1. formulario con campos: nombre, apellido, edad
2. boton de enviar: eventos submit
3. mostrar datos en pantalla
4. boton que muestre los datos actuales

Listo!

# Validar formulario con Javascript 

se validan los datos del formulario, que sea el tipo de dato que es, y que no contenga espacios

Listo!

# Operador THIS
el operador this, hace referencia al objeto que se esta accionando en ese momento, y es mas optimo de trabajar

~~~
const boton = document.getElementById('boton');

boton.addEventListener('click', function(){
	
	if(this.style.backgroundColor == 'dodgerblue'){
		this.style.backgroundColor = 'lime';
		this.style.color = 'black';
	} else {
		this.style.backgroundColor = 'dodgerblue';
		this.style.color = 'white';
	}
});
~~~

# Objetos JSON
Javascript Object Notation

practicamente crear objetos de manera muy simple. array asociativo

~~~
const pelicula = {
	title: "Batman y Robin",
	origin: "USA",
	year: 1950
};

console.log(pelicula.title);
~~~
para acceder a las propiedades solo hay que llamar el objeto y punto propiedad asi

podemos crear un array de objetos
~~~
const pelicula = {
	title: "Batman y Robin",
	origin: "USA",
	year: 1950
};

const peliculas = [
	{title:"Ironman",origin:"USE",year:2001},
	{title:"la vida es bella",origin:"alemania",year:2000},
	pelicula,
];

console.log(peliculas);
~~~

recorer el array de objetos

~~~
const pelicula = {
	title: "Batman y Robin",
	origin: "USA",
	year: 1950
};

const peliculas = [
	{title:"Ironman",origin:"USE",year:2001},
	{title:"la vida es bella",origin:"alemania",year:2000},
	pelicula,
];

for (let index in peliculas) {
	console.log(peliculas[index]);
}
~~~

mostrar en pantalla, el resultado de la iteracion del array

~~~
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
~~~

#### me falta, como encontrar un object

___


# LocalStorage
almacenamiento local en el navegador  
esta información persiste durante la navegación  
el una pagina mololitica

#### comprobar si el localstorage esta disponible en el navegador
Disponible
- comprueba que se pueda usar el local storage en el navegador
~~~
if(typeof(Storage) !== 'undefined') {
	console.log("localstorage disponible");
} 
else {
	console.log(("localstorage NO disponible"))
}
~~~
1. hay un local storage disponible por dominio
2. file:// se convierte en nuestro domini
3. el localstorage guarda informacion con un key value
4. se puede comprobar en el devtools del navegador, en la seccion de almacenamiento

#### guardar datos en el localstorage yluego recuperarlos

~~~
// comprobar si esta disponible el localstorage en el navegador
if(typeof(Storage) !== 'undefined') {
	console.log("localstorage disponible");
} 
else {
	console.log(("localstorage NO disponible"))
}
~~~
añadir valores al localstorage
- setItem guarda la key y su valor
~~~
localStorage.setItem("titulo1", "Curso Master Javascript");
localStorage.setItem("titulo2", "Curso Master PHP");
localStorage.setItem("titulo3", "Curso Master NodeJs");
~~~

recuperar elemento
- getItem recupera con la key y muestra su valor
- localStorage.getItem('titulo');
~~~
document.querySelector("#titulo1").innerHTML = localStorage.getItem('titulo1'); 
document.querySelector("#titulo2").innerHTML = localStorage.getItem('titulo2'); 
document.querySelector("#titulo3").innerHTML = localStorage.getItem('titulo3'); 
~~~

# Guardar un objeto JSON en el localstorage
- crear el JSON usuario
- para enviar este objeto y guardarlo en el localstorage, debemos convertirlo a un JSON string
- ya que no se puede enviar JSON puro por http
~~~
// de esta forma seria la opcion de guardar un usuario JSON
const usuario = {
	nombre: "Jared",
	email: "jared@hola.com",
	web: "jaredlatorre.com",
};

localStorage.setItem()
~~~
- como convierto un JSON a string?
- ahi un objeto en javascript que se llama JSON
- accedemos a uno de sus metodos para convertir a string 
- JSON.stringify() con este metodo convertimos a string nuestro JSON
~~~
// almacenar el JSON string con (key , JSON.stringify(usuario)); 
localStorage.setItem("json_stringify", JSON.stringify(usuario));
~~~

Resultado de la conversión

> {"nombre":"Jared","email":"jared@hola.com","web":"jaredlatorre.com"}

Código Final en el ejercicio de localstorage.js

# Recuperar un Objeto JSON string
- recuperar un JSON string a JSON object
- toca pasar el string del key
~~~
localStorage.setItem("json_stringify", JSON.stringify(usuario));
~~~
- asi podemos acceder a la información JSON almacenada en una variable
~~~
let userJson = JSON.parse(localStorage.getItem("json_stringify"));
console.log(userJson);
~~~
- mostrar las propiedades del JSON en el documento html 
~~~
document.querySelector("#json").innerHTML = `<div><strong>Objeto JSON</strong></div>nombre: ${userJson.nombre} <br> 
email: ${userJson.email} <br> web: ${userJson.web} `; 
document.querySelector("#titulo1").innerHTML += `<h4>desde el Object JSON ${userJson.nombre}</h4>`;
~~~

# Borrar la memoria del localstorage
- borrar por item con removeItem(key)
- remover un item, en este caso el key del JSON
~~~
localStorage.removeItem(json_stringify)
~~~

# Limpiar el localStorage
- limpia todo el localStorage del documento
- limpia los value pero no las key (hice la prueba en mozilla)
~~~
localStorage.clear();
~~~

# Ejercicio completo localStorage

- crear un formulario que nos permita 
- añadir peliculas
- eliminar peliculas

Listo!