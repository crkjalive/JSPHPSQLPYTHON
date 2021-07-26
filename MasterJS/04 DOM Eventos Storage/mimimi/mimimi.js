'use strict'

const h1_mimimi = document.querySelector('#h1_mimimi');

const div_lista_mimimi = document.querySelector('#lista_mimimi');

const input_mimimi = document.querySelector('#input_mimimi');
input_mimimi.placeholder = "Escribe aquí"

const button_list_mimimi = document.querySelector('#button_list_mimimi');
button_list_mimimi.textContent = 'mis mimimi'

let text_mimimi = '';
const lista_mimimi = [];

input_mimimi.addEventListener('keyup', () => {
  let i_mimimi = String.fromCharCode(event.keyCode);
  
  if (i_mimimi == 'A'){
    text_mimimi+= 'i'
  }
  else if (i_mimimi == 'E'){
    text_mimimi+= 'i'
  }
  else if (i_mimimi == 'I'){
    text_mimimi+= 'i'
  }
  else if (i_mimimi == 'O'){
    text_mimimi+= 'i'
  }
  else if (i_mimimi == 'U'){
    text_mimimi+= 'i'
  } 
  else {
    text_mimimi += String.fromCharCode(event.keyCode).toLowerCase();
  }
  // console.log(text_mimimi);
  h1_mimimi.textContent = text_mimimi;
});


input_mimimi.addEventListener('blur', () => { 
  let fecha = new Date();

  if (input_mimimi.value) {
    lista_mimimi.unshift(input_mimimi.value, fecha);
  }

  input_mimimi.value = ''
  // console.log(lista_mimimi)
});

input_mimimi.addEventListener('focus', () => { 
  h1_mimimi.textContent = 'mimimi'
  text_mimimi = ''
})


button_list_mimimi.addEventListener('click', () => {
  div_lista_mimimi.textContent = '';

  for(let i = 0; i < lista_mimimi.length; i++) {
    div_lista_mimimi.innerHTML += `
    <div class="chat_mimimi">${lista_mimimi[i]}</div>
    `;
    // console.log(i, lista_mimimi[i])
  }
  // console.log(lista_mimimi)

  // console.log("probando el click")
})
