'use strict'

const amount = parseInt(prompt('Syötä noppien määrä:'));
const valueLookedFor = parseInt(prompt('Syötä haluttu summa:'));
const rollAmount = 10000

let i = 0
let timesRolled = 0

while (i<rollAmount) {
  let sum = 0
  for (let j = 0; j<amount; j++) {
    sum += Math.floor(Math.random()*6+1)
  }
  if (sum === valueLookedFor)
    timesRolled++
  i++
}
console.log(i)
const probability = (timesRolled/rollAmount)*100
document.querySelector("p").innerHTML = `Heittämällä noppaa ${rollAmount} kertaa, laskettiin todennäköisyydeksi saada silmälukujen summaksi ${valueLookedFor} heittämällä ${amount} noppaa: ${probability} %`

