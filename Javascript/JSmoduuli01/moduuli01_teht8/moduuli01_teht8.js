'use strict';

let year = parseInt(prompt('Syötä aloitus vuosi:'));
const endYear = parseInt(prompt('Syötä lopetus vuosi:'));

const list = document.querySelector('ul');

while (year <= endYear) {

  if (year % 4 === 0) {
    if (year % 100 === 0) {
      if (year % 400 === 0) {
        let li = document.createElement('li');
        li.innerText = year;
        list.appendChild(li);
      }
    } else {
      let li = document.createElement('li');
      li.innerText = year;
      list.appendChild(li);
    }

  }
  year += 1
}