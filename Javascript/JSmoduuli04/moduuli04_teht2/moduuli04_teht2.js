'use strict'

const form = document.querySelector("form");

async function logMovies() {
  const query = document.querySelector("#query").value
  const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
  const movies = await response.json();

  console.log(movies)
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  logMovies()
})