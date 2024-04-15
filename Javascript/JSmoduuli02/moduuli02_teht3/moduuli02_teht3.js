'use strict'

let dogNames = []
const unorderedList = document.querySelector("ul");

for (let i = 1; i<=6; i++) {
  dogNames.push(prompt(`Syötä koiran ${i}. nimi:`));
}

dogNames.sort().reverse();

for (let name of dogNames) {
  let newItem = document.createElement("li");
  newItem.innerText = name;
  unorderedList.append(newItem)
}