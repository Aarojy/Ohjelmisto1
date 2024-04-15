'use strict'

let listOfNames = []

for (let i = 1; i<=5; i++) {
  listOfNames.push(prompt(`Syötä ${i}. numero:`))
}

for (let i = listOfNames.length-1; i>=0; i--) {
  console.log(listOfNames[i])
}