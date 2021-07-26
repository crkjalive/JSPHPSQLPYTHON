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