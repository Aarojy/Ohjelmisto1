'use strict'

const paragraph = document.querySelector("p");
const listOfStrings = ["Matti", "Teppo", "Seppo", "Kalevi"];
let result = "";

for (let string of listOfStrings) {
  result = result + string;
}

paragraph.innerText = result