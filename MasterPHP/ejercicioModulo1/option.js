'use strict'
window.addEventListener('load', () => {

const h1 = document.getElementById('h1');
const optgroup = document.querySelector('optgroup');
const opt1 = document.createElement('option');
opt1.value = "marica";
opt1.textContent = "marica";
optgroup.appendChild(opt1);


select.addEventListener('click', () => {
  h1.textContent = select.value;
});






);
