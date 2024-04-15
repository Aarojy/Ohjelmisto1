'use strict'

let inputNumber = 1;
let numsList = [];

while (inputNumber !== 0) {
  inputNumber = parseInt(prompt("Syötä uusi numero tai lopeta syöttämällä 0."))
  numsList.push(inputNumber)
}

numsList.sort((a,b)=>{return b-a})

for (let i = 0; i < numsList.length-1; i++) {
  console.log(numsList[i])
}
