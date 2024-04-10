'use strict'

const year = parseInt(prompt('Syötä vuosi:'));

if (year % 4 === 0) {
  if (year % 100 === 0) {
    if (year % 400 === 0) {
      document.querySelector("p").innerHTML = `Syöttämäsi vuosi: ${year} on karkausvuosi!`
    } else {
      document.querySelector("p").innerHTML = `Syöttämäsi vuosi: ${year} ei ole karkausvuosi!`
    }
  } else {
    document.querySelector("p").innerHTML = `Syöttämäsi vuosi: ${year} on karkausvuosi!`
  }

} else {
  document.querySelector("p").innerHTML = `Syöttämäsi vuosi: ${year} ei ole karkausvuosi!`
}
