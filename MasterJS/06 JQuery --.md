# JQuery
1. Primeros pasos
2. Selectores
3. Eventos
4. Efectos y animaciones
5. AJAX
6. JQuery UI (manipular)
7. Animaciones
8. Plugins y widgets
9. Proyecto Javascript y JQuery

# Para que es jQuery
1. para hacer de todo

# Integrar jQuery
1. atraves de script cdn
~~~

~~~
2. por npm
~~~
npm install jquery
~~~
3. por script
~~~
<script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
~~~

# Selector ID 

1. comprobamos si esta cargado el jquery
~~~
$(document).ready(()=>{
	console.log("Cargado jQuery");
	});
~~~
- con $ o jquery es lo mismo es un objeto
- .ready ejecuta el metodo que recibe la funcion de callback
- de esta forma se maneja jquery dentro de javascript
- como se seleccionar los ID 
- con .css aplico los estilos que quiera

1. como seleccionamos el ID 
~~~
jquery(document).ready(()=>{

	$("#rojo").css("background","red")
		.css("color","white");

	$("#amarillo").css("background","yellow")
		.css("color","black");

	$("#verde").css("background","green")
		.css("color","white");

	console.log('Cargado jQuery');
});
~~~

# Selector class
- selecciona los elementos en modo array
- asi que para seleccionar un elemento de la clase, hay que ver su indice denrto del array
- concatenando .css() le doy el estilo que quiera

~~~
let mi_clase = $(".zebra").
mi_clase.css("border","5px dashed black");
~~~

# evento
- para agregar eventos
~~~
$(".sin_borde").click(function(){
		console.log("Click a algo");
	$(this).addClass('zebra');
	});
~~~

# Selector etiqueta
- le damos el nombre de la etiqueta
~~~
let parrafos = $("p").css('cursor','pointer');

parrafos.click(()=>{

	let that = $(this);

	if(!that.hasClass('zebra')){
		that.addClass('grande');
	}
	else{
		that.removeClass('grande');
	}
	});
~~~

# Selectores de atributo
~~~
	let parrafos = $('p');
	parrafos.click(()=>{
		parrafos.css('background','blue');
	})
~~~

# Selector por atributo
~~~
$('[title="google"]').css('background','#ccc');
$('[title="facebook"]').css('background','blue');		
~~~

# find y parent
- aplicar a varios elementos la misma clase
~~~
$('p, a').addClass('margen-superior');
~~~
- alcanzar un elemento
~~~
let busqueda = $('#caja .resaltado').eq(0).parent().parent().parent().find(['title="Google"']);
console.log(busqueda);
~~~

# eventos
~~~
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
~~~

# Efectos animaciones




















