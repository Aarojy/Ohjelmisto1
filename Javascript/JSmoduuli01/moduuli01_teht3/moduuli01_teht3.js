'use strict'


const num1 = parseInt(prompt('Syötä nro. 1:'));
const num2 = parseInt(prompt('Syötä nro. 2:'));
const num3 = parseInt(prompt('Syötä nro. 3:'));


const allParagraphs = document.querySelectorAll("p")

allParagraphs[0].innerHTML = `Syöttämiesi numeroiden summa on: ${num1+num2+num3}`
allParagraphs[1].innerHTML = `Syöttämiesi numeroiden tulo on: ${num1*num2*num3}`
allParagraphs[2].innerHTML = `Syöttämiesi numeroiden keskiarvo on: ${(num1+num2+num3)/3}`