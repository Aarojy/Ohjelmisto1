'use strict'

const num1 = parseInt(prompt('Syötä numero:'));
let isPrime = true

for (let i = 2; i<(num1/2+1); i++) {
  if (num1 % i === 0) {
    document.querySelector("p").innerHTML = `Valitsemasi numero: ${num1} ei ole alkuluku!`
    isPrime = false
    break
  }

}

if (isPrime) {
  document.querySelector("p").innerHTML = `Valitsemasi numero: ${num1} on alkuluku!`
}