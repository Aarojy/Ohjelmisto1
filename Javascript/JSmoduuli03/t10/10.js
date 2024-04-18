'use strict'

const form1 = document.querySelector("#source")
const paragraph = document.querySelector("#target")

form1.addEventListener("submit", submitForm)

function submitForm(event) {
  event.preventDefault()

  const firstName = form1.elements["firstname"].value;
  const lastName = form1.elements["lastname"].value;

  paragraph.innerText = firstName + " " + lastName
}