'use strict'

'use strict'

function diceRoll(num) {
  return Math.floor(Math.random()*num+1);
}
const maxRoll = parseInt(prompt("Syötä noppan silmälukujen määrä:"))

let roll = 0;
const uList = document.querySelector("ul")
let newElement = ""

while (roll !== maxRoll) {
  roll = diceRoll(maxRoll);
  newElement = document.createElement("li")
  newElement.innerText = roll
  uList.append(newElement)
}