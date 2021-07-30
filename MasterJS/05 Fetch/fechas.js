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


