# Fetch y peticiones asincronas

- fetch, nos permite hacer peticiones ajax, 
- son peticiones ajax de un backend, REST API 
- esto nos permite consumir datos de la nube
- esas api por lo general son fake, son datos de prueba
- extension JSON view para ver los JSON formateados

servicio web  
JSONplaceholder  
https://jsonplaceholder.typicode.com/

- fetch hace peticiones ajax, es un sustituto

~~~

'use strict'

// Fetch y peticiones a servicios / apis rest

const listadoUsuarios = document.querySelector('#usuarios') 

// guardamos los usuarios de la api
let usuarios = [];

// hacemos la peticion al servidor, llamada AJAX
fetch('https://reqres.in/api/users') // accede a un servidor remoto api

	// se queda a la espera, recoge los datos y los convirte en json
	.then(data => data.json()) 

	// peticion asyncrona que captura la data de los usuarios (users)
	.then(users => { 
		usuarios = users.data;
		console.log(usuarios);

		// iteramos la data de usuarios
		usuarios.map((user, i) => { 
			let nombre = document.createElement('h4');

			// insertamos info al document
			nombre.innerHTML = ` ${i+1} Nombre: ${user.first_name} 
				${user.last_name} <br> Email: ${user.email}
			`;

			// agregamos el elemento creado al div contenedor
			listadoUsuarios.append(nombre);

			// damos css para ocultar el span de cargando
			document.querySelector('.cargando').style.display = 'none';
		});
	});

~~~
- hasta aqui se termina la primera parte sobre la petición Fetch

# Promesas y fetch
- las promesas son muy utiles ya que previenen el callback hell
- evitando que el codigo se vuelva ilegible e inmantenible
- esto sucede cuando se trabaja con datos asyncronos, api rest, ajax
- esto implica que se deba esperar para obtener los resultados
- que pasa si requerimos pedir informacion de un usuario en especifico.

~~~
'use strict'

// Fetch y promesas a peticiones de servicios / apis rest

const listUsuarios = document.querySelector('#usuarios') 
const listJanet = document.querySelector('#janet') 

// peticion fetch usuarios
const getUsuarios = () => {
	return fetch('https://reqres.in/api/users')
}

// peticion fetch a janet
const getJanet = () => {
	return fetch('https://reqres.in/api/users/2')
}

// lista los usuarios
const listarUsuarios = (usuarios) => {
	usuarios.map((user, i) => {
		let nombre = document.createElement('h4');
		nombre.innerHTML = ` ${i+1} Nombre: ${user.first_name} ${user.last_name} <br> Email: ${user.email}`;
		listUsuarios.append(nombre);
		document.querySelector('.cargando').style.display = 'none';
	});
}

// mostrar janet
const mostrarJanet = (user) => {
	let nombre = document.createElement('h4');
	let avatar = document.createElement('img');

	nombre.innerHTML = ` Nombre: ${user.first_name} ${user.last_name} <br> Email: ${user.email}`;
	
	avatar.src = user.avatar;
	avatar.width = '130';

	listJanet.append(avatar);
	listJanet.append(nombre);
	document.querySelector('#janet .cargando').style.display = 'none';
}

// peticion fetch usuarios then es la promesa
getUsuarios()
	.then(data => data.json())
	.then(users => { 
		listarUsuarios(users.data);
		return getJanet();
	})
	.then(data => data.json())
	.then(user => {
		mostrarJanet(user.data);
	});
~~~

- losthen son las promesas o peticiones que hace al servidor, esperando a que se complete y continue con la siguiente promesa

resumen del codigo.
1. se crean las funciones, que hacen el llamado a la url del usuario.
2. devolviendos en la funcion la url
3. luego estan las funciones que hace el llamado a los datos json del api rest
4. esta logica en el codigo, me mapea los usuarios que ha traido devolviendo el objeto y el indice
5. creamos un elemento donde vamos a insertar la data json
6. con innerHTML le metemos codigo html y data json 
7. por ultimo le agregamos este elemento a nuestro contenedor con append()
8. codigo de las promesas 
~~~
getUsuarios()
	.then(data => data.json())
	.then(users => { 
		listarUsuarios(users.data);
		return getJanet();
	})
	.then(data => data.json())
	.then(user => {
		mostrarJanet(user.data);
	});
~~~

- esta fucion atraves de las promesas, hace las peticiones al servidor con (.then), generando...
1. transforma la data en json
2. lista los usuarios, atraves de la funcion listarUsuarios(), que recibe como parametro users.data, 
3. retornamos tambien como ya estan los datos disponibles, el objeto Janet
4. otro .then me formatea a json
5. otra promesa recibe el user 
6. ejecutamos la funcion para mostrar a janet
7. esta funcion recibe al user.data como parametro directamente

- con esto vemos como llamar a los usuarios o llamar a uno solo enconcreto

# Como crear promesas

~~~
// getInfo
const getInfo = () => {
	let profesor = {
		nombre: "Victor",
		apellidos: "Robles",
		url:"https//victorroblesweb.es",
	};

	// promise chaining, esta es otra promesa para encadenar
	return new Promise((resolve, reject) => {
		let profesor_string = JSON.stringify(profesor);
		if(typeof profesor_string != 'string'){
			return reject('error');
		} else {
			setTimeout( ()=> {
			}, 3000);
				return resolve(profesor_string);
		}
	});
}
~~~
1. creamos una funcion
2. le creamos el objeto prfesor
3. retornamos una new Promise
4. new Promise es la instancia de la promesa nueva
5. capturamos el objeto JSON en un string con stringify que conbierte el JSON a String
6. la new promise, devuleve dos parametros, resolve and reject
7. resolve es el que devuelve la promesa si fue exitosa la validacion
8. reject devuelve un error si no se valido algun dato
9. creamos un setTimeout, para demostrar que hasta que no se cumpla la promesa no continua haciendo nada
10. cuando ya resuelve la promesa, retorna el string

- con esto ya vemos como se maneja la programacion orientada a objetos, de una forma global, ya que no hemos visto POO aun.

# Capturar error en la promesa
1. para capturar los errores se hace con el metodo ***.catch()*** en las posibles promesas
~~~
.catch(error => {
	console.log(error)
	})
~~~
- esto podria ser activado en casos como: que se valla el internet, hacer una llamada a una url que no exista, 

# Capturar errores
1. capturar errores en el codigo
~~~
try{
	// codigo a prueba
}
catch (error) {
	// error
}
~~~
**Código de prueba***
~~~
try {
	let year = 2021;
	alert(yea);

} catch(e) {
	alert("a ocurrido un error: " + e);
}
~~~
- de esta manera confirmamos si un trozo de codigo esta bien
- si no esta bien nos devolvera el error
- todo codigo suceptible a errores podemos validarlo con este metodo try-catch

# Fechas y funciones matematicas
1. objeto ***new Date***
~~~
let fecha = new Date;
console.log(fecha);
~~~
***devuelve***
~~~
Date Wed Jul 28 2021 00:07:56 GMT-0500 (hora estándar de Colombia)

let fecha = new Date;
document.write(`<h3>mostrar toda la fecha del sistema</h3>${fecha}`);
console.log(fecha);

let year = fecha.getFullYear();
document.write(`<h3>mostrar el año </h3>${year}`);
console.log(year);

let mes = fecha.getMonth();
document.write(`<h3>mostrar el mes contando desde cero</h3> mes de Julio ${mes}`);
console.log(mes);

let dia = fecha.getDay();
document.write(`<h3>muestra el dia de la semana</h3>${dia}`);
console.log(dia);

let hora = fecha.getHours();
document.write(`<h3>muestra la hora</h3>${hora}`);
console.log(hora);

let min = fecha.getMinutes();
document.write(`<h3>muestra los minutos</h3>${min}`);
console.log(min);

let sec = fecha.getSeconds();
document.write(`<h3>muestra los segundos</h3>${sec}`);
console.log(sec);

let milSec = fecha.getMilliseconds();
document.write(`<h3>muestra los milisegundos</h3>${milSec}`);
console.log(milSec);

let utcDate = fecha.getUTCDate();
document.write(`<h3>fecha en numero</h3>${utcDate}`);
console.log(utcDate);
~~~

# Funciones matematicas con Math
1. hay muchisimas funciones matematicas, que hay que buscar la que uno necesite
***ejemplos de algunas mas reconocidas***
~~~
let numeroAleatorio = Math.random();
document.write(`<h4>Math.random()<br>numero aleatorio</h4>${numeroAleatorio}`);
console.log(numeroAleatorio);

let numeroAleatorio2 = Math.random()*100;
document.write(`<h4>Math.random()<br>numero aleatorio de 2 cifras</h4>${numeroAleatorio2}`);
console.log(numeroAleatorio2)

let numeroAleatorio3 = Math.random()*1000;
document.write(`<h4>Math.random()<br>numero aleatorio de 3 cifras</h4>${numeroAleatorio3}`);
console.log(numeroAleatorio3)

let numeroAleatorioEntero = Math.ceil(Math.random()*20);
document.write(`<h4>Math.ceil(Math.random())<br>redondea por arriba</h4>${numeroAleatorioEntero}`);
document.write(`<h4>Math.ceil(Math.random())<br>redondea por arriba</h4>${numeroAleatorioEntero}`);
console.log(numeroAleatorioEntero)

let redondear = Math.round(Math.random()*100);
document.write(`<h4>Math.ceil(Math.random())<br>redondea por arriba</h4>${redondear}`);
console.log(redondear)
~~~









