'use strict';

const button = document.querySelector('#start');
const results = document.querySelector('#result')

button.addEventListener('click', calculate);


function calculate() {
  const num1 = parseInt(document.querySelector('#num1').value);
  const num2 = parseInt(document.querySelector('#num2').value);
  const calcType = document.querySelector('#operation').value;
  switch (calcType) {
    case 'add':
      results.innerHTML = num1 + num2;
      break;
    case 'sub':
      results.innerHTML = num1 - num2;
      break;
    case 'multi':
      results.innerHTML = num1 * num2;
      break;
    case 'div':
      results.innerHTML = num1 / num2;
      break;
  }
}