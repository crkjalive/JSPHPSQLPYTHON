'use strict'

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

const footer = document.getElementById('footer');

footer.style.backgroundColor = "tomato";

const nav = document.createElement('nav');
const ul = document.createElement('ul');

const a0 = document.createElement('a');
a0.className = 'logo'
const a1 = document.createElement('a');
const a2 = document.createElement('a');
const a3 = document.createElement('a');
const a4 = document.createElement('a');

const li0 = document.createElement('li');
const li1 = document.createElement('li');
const li2 = document.createElement('li');
const li3 = document.createElement('li');
const li4 = document.createElement('li');

li0.textContent = 'Logo';
li1.textContent = 'Developer';
li2.textContent = 'Backend';
li3.textContent = 'Frontend';
li4.textContent = 'Tools';

ul.style.listStyle = 'none'

a0.append(li0)
a1.append(li1)
a2.append(li2)
a3.append(li3)
a4.append(li4)

ul.append(a0,a1,a2,a3,a4);

nav.append(ul);

footer.append(nav);