// algunas de la funciones matematicas

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