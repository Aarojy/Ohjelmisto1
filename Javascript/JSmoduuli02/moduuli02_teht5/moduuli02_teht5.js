'use strict'

let inputNumber = 1;
let numsList = [];

while (!(inputNumber in numsList)) {
  inputNumber = parseInt(prompt("Syötä uusi numero"))
  numsList.push(inputNumber)
}

for (let i = 0; i < numsList.length-1; i++) {
  console.log(numsList[i])
}