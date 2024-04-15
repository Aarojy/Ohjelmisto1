'use strict'

const originalArray = [1,2,3,4,5,6,7,8,9,10];

function even(array) {
  let newArr = []

  for (let num of array) {
    if (num % 2 === 0) {
      newArr.push(num)
    }
  }
  return newArr
}

const newArray = even(originalArray)

console.log(`Printataan vanha lista: ${originalArray}`)
console.log(`Printataan uusi lista: ${newArray}`)