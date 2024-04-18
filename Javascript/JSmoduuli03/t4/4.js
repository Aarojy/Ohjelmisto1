'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const target = document.querySelector("#target")

for (let student of students) {
  const newOption = document.createElement("option")
  newOption.value = student["id"]
  newOption.innerText = student["name"]
  target.appendChild(newOption)
}