#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const getMovieCharacters = (movieId) => {
  return new Promise((resolve, reject) => {
    const options = {
      url: `https://swapi-api.hbtn.io/api/films/${movieId}`,
      method: 'GET'
    };

    request(options, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const characters = JSON.parse(body).characters;
        resolve(characters);
      } else {
        reject(error || response.statusCode);
      }
    });
  });
};

const getCharacterName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const name = JSON.parse(body).name;
        resolve(name);
      } else {
        reject(error || response.statusCode);
      }
    });
  });
};

const printMovieCharacters = async (movieId) => {
  try {
    const characters = await getMovieCharacters(movieId);
    for (const characterUrl of characters) {
      const name = await getCharacterName(characterUrl);
      console.log(name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

printMovieCharacters(movieId);
