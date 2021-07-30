'use strict'

window.addEventListener('load', () => {


  const screenData = document.querySelector('#mostrar');
  screenData.textContent = "Data"

  const inputName = document.querySelector('#inp_nombre');
  inputName.value = "Jared";

  const inputLastName = document.querySelector('#inp_apellido');
  inputLastName.value = "Latorre";

  const inputAge = document.querySelector('#inp_edad');
  inputAge.value = 2;

  const btn = document.querySelector('#btn');
  btn.textContent = 'enviar json';

  btn.addEventListener('click', () => {
    const formu = {
      nombre: inputName.value,
      apellido: inputLastName.value,
      edad: inputAge.value,
    };
    localStorage.setItem(formu.nombre, JSON.stringify(formu));
    console.log(formu.nombre);
  })

  screenData.addEventListener('click', () => {
    for(let i = 0; i<localStorage.length; i++){
      console.log(localStorage[i]);

    }
    let parce = JSON.parse(localStorage.getItem(inputName.value));
    screenData.textContent = `${parce.nombre}, ${parce.apellido}, ${parce.edad}`;
  });





});
let js="textContent createElement value appendChild append innerHTML style className getElementsByClassName getElementsByTagName querySelectorAll querySelector document.write backgroundColor padding textAlign border color fontSize textTransform createTextNode window location open url href innerHeight innerWidth screen height width click blur change focus mouseover mouseout onclick keydown keypress keyup String.fromCharCode(event.keyCode) setInterval setTimeout clearInterval"









