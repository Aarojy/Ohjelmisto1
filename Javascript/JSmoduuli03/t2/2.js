'use strict'

const target = document.querySelector("#target")

const element1 = document.createElement("li")
const element2 = document.createElement("li")
const element3 = document.createElement("li")

element1.innerText = "First item"
element2.innerText = "Second item"
element3.innerText = "Third item"

target.appendChild(element1)
target.appendChild(element2)
target.appendChild(element3)

const items = document.querySelectorAll("li")

items[1].classList.add("my-item")