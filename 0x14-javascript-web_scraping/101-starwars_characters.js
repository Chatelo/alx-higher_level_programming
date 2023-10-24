#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

// Helper function to fetch characters for a movie
function getCharacters (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(apiUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      // Fetch characters data in the correct order
      fetchCharacters(characterUrls, 0, []);
    } else {
      console.log('Error:', error);
    }
  });
}

// Helper function to recursively fetch and store character names in the correct order
function fetchCharacters (characterUrls, index, charactersList) {
  if (index >= characterUrls.length) {
    // All characters have been fetched, print them in the correct order
    printCharacters(charactersList);
    return;
  }

  request(characterUrls[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      charactersList.push(characterData.name);
      // Fetch the next character
      fetchCharacters(characterUrls, index + 1, charactersList);
    } else {
      console.log('Error:', error);
    }
  });
}

// Helper function to print character names in the correct order
function printCharacters (charactersList) {
  charactersList.forEach((characterName) => {
    console.log(characterName);
  });
}

// Start the script by fetching characters for the given movie ID
getCharacters(movieId);
