'use strict'

const candidateAmount = parseInt(prompt("Kuinka monta ehdokasta?"))
let candidateList = []
let candidateNames = []

for (let i = 1; i<=candidateAmount; i++) {
  while (true) {
    let candidate = prompt(`Syötä ehdokkaan nro. ${i} nimi:`)
    if (!candidateNames.includes(candidate)) {
      candidateList.push({'name': candidate, 'votes': 0});
      candidateNames.push(candidate)
      break;
    } else {
      alert("Syöttämäsi ehdokas on jo listalla!")
    }
  }
}

const voterAmount = parseInt(prompt("Kuinka monta äänestäjää?"))

for (let i = 1; i<=voterAmount; i++) {
  let vote = prompt(`Äänestäjä nro. ${i}. Syötä valitsemasi ehdokkaan nimi:`)
  for (let j of candidateList) {
    if (vote === j["name"]) {
      j["votes"]++
    }
  }
}

let winner = ""
let maxVotes = 0

for (let cand of candidateList) {
  if (cand["votes"] > maxVotes) {
    winner = cand["name"]
    maxVotes = cand["votes"]
  }
}

console.log(`Voittaja on ${winner}. Hän sai ${maxVotes} ääntä!`)

for (let cand of candidateList) {
  console.log(`${cand["name"]}: ${cand["votes"]} ääntä`)
}
