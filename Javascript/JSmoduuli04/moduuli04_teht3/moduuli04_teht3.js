'use strict';

const form = document.querySelector('form');

async function printMovies() {
  const movieDiv = document.querySelector('#movies');
  movieDiv.innerHTML = '';
  const query = document.querySelector('#query').value;
  const response = await fetch(
      `https://api.tvmaze.com/search/shows?q=${query}`);
  const movies = await response.json();

  for (let movie of movies) {
    const header = document.createElement('h2');
    const link = document.createElement('a');
    const img = document.createElement('img');
    const summary = document.createElement('div');
    const br = document.createElement("br")
    const article = document.createElement('article');
    const elements = [header, link, img, summary, article];
    header.innerText = movie['show']['name'];
    link.href = movie['show']['url'];
    link.innerText = movie['show']['url'];
    link.target = '_blank';
    if (!(movie['show']['image'] === null)) {
      img.src = movie['show']['image']['medium'];}
    img.alt = movie['show']['name'];
    summary.innerHTML = movie['show']['summary'];
    article.appendChild(header);
    article.appendChild(link);
    article.appendChild(br)
    if (!(movie['show']['image'] === null)) {
      article.appendChild(img);}
    article.appendChild(summary);
    movieDiv.appendChild(article)
  }

}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  printMovies();
});