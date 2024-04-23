'use strict'

const target = document.querySelector("#target")

async function chuckNorris(query) {
  const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${query}`)
  const responseJSON = await response.json()
  for (let joke of responseJSON["result"]) {
    const article = document.createElement("article")
    const pElement = document.createElement("p")
    pElement.innerText = joke["value"]
    article.appendChild(pElement)
    target.appendChild(article)
  }
}

const form = document.querySelector("#submitForm")
form.addEventListener("submit", (event) => {
  event.preventDefault()
  target.innerHTML = ""
  const query = document.querySelector("#query").value
  chuckNorris(query)

})