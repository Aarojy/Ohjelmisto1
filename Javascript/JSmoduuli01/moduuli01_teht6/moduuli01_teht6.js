'use strict'

if (confirm('Haluatko laskea neliöjuuren?')) {
  const num1 = parseInt(prompt('Syötä numero:'));
  document.querySelector("p").innerHTML = `Numeron: ${num1} neliöjuuri on: ${num1*num1}`

} else {
  document.querySelector("p").innerHTML = 'Neliöjuurta ei laskettu'
}