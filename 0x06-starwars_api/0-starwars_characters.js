#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId || isNaN(parseInt(movieId))) {
  console.error('Usage: ./0-starwars_characters.js movieId');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error('Invalid response:', response.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
