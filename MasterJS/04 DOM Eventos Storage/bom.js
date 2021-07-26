'use strict'


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
	window.open(url);
}
/* abrirVentana("https://google.com") */
