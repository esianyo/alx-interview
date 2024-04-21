#!/usr/bin/node

const request = require('request-promise');
const movieId = process.argv[2];

if (!movieId || isNaN(parseInt(movieId))) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

async function getCharacters() {
  try {
    const response = await request(apiUrl);
    const film = JSON.parse(response);
    const characters = film.characters;

    for (const characterUrl of characters) {
      const characterResponse = await request(characterUrl);
      const character = JSON.parse(characterResponse);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

getCharacters();
