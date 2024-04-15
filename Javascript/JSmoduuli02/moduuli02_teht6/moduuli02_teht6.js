'use strict'

function diceRoll() {
  return Math.floor(Math.random()*6+1);
}

let roll = 0;
const uList = document.querySelector("ul")
let newElement = ""

while (roll !== 6) {
  roll = diceRoll();
  newElement = document.createElement("li")
  newElement.innerText = roll
  uList.append(newElement)
}