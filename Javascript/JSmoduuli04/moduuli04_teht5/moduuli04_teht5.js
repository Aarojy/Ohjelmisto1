'use strict'

async function chuckNorris() {
  const response = await fetch("https://api.chucknorris.io/jokes/random")
  const responseJSON = await response.json()
  console.log(responseJSON["value"])
}

chuckNorris()