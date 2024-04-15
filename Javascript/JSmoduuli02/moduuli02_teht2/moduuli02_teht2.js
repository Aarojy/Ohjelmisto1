'use strict'

const amountOfParticipants=  parseInt(prompt("Kuinka monta osallistujaa?"));
let listOfParticipants = []
const orderedList = document.querySelector("ol");

for (let i = 1; i <= amountOfParticipants; i++) {
  listOfParticipants.push(prompt(`Lisää pelaajan ${i} nimi:`))
}

listOfParticipants.sort()

for (let participant of listOfParticipants) {
  let newItem = document.createElement("li");
  newItem.innerText = participant;
  orderedList.append(newItem)
}