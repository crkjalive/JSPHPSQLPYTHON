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
		} 
		else {
			setTimeout( ()=> {
				return resolve(profesor_string);
			}, 7000);
		}
	});
}


// lista los usuarios
const listarUsuarios = (usuarios) => {
	usuarios.map((user, i) => {
		let nombre = document.createElement('div');
		let avatarUsers = document.createElement('img');
		avatarUsers.src = user.avatar;
		avatarUsers.style.width = '100px';
		avatarUsers.style.borderRadius = '50%'

		nombre.innerHTML = `${i+1} name:<br><h3>${user.first_name} ${user.last_name}</h3>email:<h4>${user.email}</h4>`;
		listUsuarios.append(avatarUsers,nombre);
		document.querySelector('.cargando').style.display = 'none';
	});
}

// mostrar janet
const mostrarJanet = (user) => {
	let nombre = document.createElement('h4');
	let avatar = document.createElement('img');

	nombre.innerHTML = ` Nombre: ${user.first_name} ${user.last_name} <br> Email: ${user.email}`;
	
	avatar.src = user.avatar;
	avatar.style.width = '130';
	avatar.style.borderRadius = '50%'

	listJanet.append(avatar);
	listJanet.append(nombre);
	document.querySelector('#janet .cargando').style.display = 'none';
}

// peticion fetch usuarios, then es la promesa
getUsuarios()
	.then(data => data.json())
	.then(users => { 
		listarUsuarios(users.data);
		return getJanet();
	})
	.then(data => data.json())
	.then(user => {
		mostrarJanet(user.data);
		return getInfo();
	})
	.then(data => {
		console.log(data);
	})
	.catch(error => {
	console.log(error)
	});
