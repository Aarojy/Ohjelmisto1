'use strict'

const button = document.querySelector("#start")
const results = document.querySelector("#result")

button.addEventListener("click", calculate)

function calculate() {
  const userInput = document.querySelector("#calculation").value

  if (userInput.includes("+")) {
    const splitInput = userInput.split("+")
    results.innerHTML = parseInt(splitInput[0]) + parseInt(splitInput[1])
  } else if (userInput.includes("-")) {
    const splitInput = userInput.split("-")
    results.innerHTML = parseInt(splitInput[0]) - parseInt(splitInput[1])
  } else if (userInput.includes("*")) {
    const splitInput = userInput.split("*")
    results.innerHTML = parseInt(splitInput[0]) * parseInt(splitInput[1])
  } else if (userInput.includes("/")) {
    const splitInput = userInput.split("/")
    results.innerHTML = parseInt(splitInput[0]) / parseInt(splitInput[1])
  } else {
    console.log("Ei")
  }

}