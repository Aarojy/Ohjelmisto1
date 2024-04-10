'use strict'

const number = parseInt(prompt('Kuinka monta noppaa heitetään?'));
let sum = 0

for (let i = 0; i<number; i++) {
  sum = sum + Math.floor(Math.random()*6+1)
}

document.querySelector("p").innerHTML = `Heitit ${number} noppaa. Noppien silmälukujen summa on: ${sum}`