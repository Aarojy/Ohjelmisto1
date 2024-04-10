'use strict'

const name = prompt('Mikä on nimesi?');

switch (Math.floor(Math.random()*4)+1) {
  case 1:
    document.querySelector("p").innerHTML = `${name} olet Rohkelikko!`
    break
  case 2:
    document.querySelector("p").innerHTML = `${name} olet Luihuinen!`
    break
  case 3:
    document.querySelector("p").innerHTML = `${name} olet Puuskupuh!`
    break
  case 4:
    document.querySelector("p").innerHTML = `${name} olet Korpinkynsi!`
}