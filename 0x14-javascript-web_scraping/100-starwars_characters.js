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

      // Recursively fetch character data and print names
      fetchCharacters(characterUrls, 0);
    } else {
      console.log('Error:', error);
    }
  });
}

// Helper function to recursively fetch and print character names
function fetchCharacters (characterUrls, index) {
  if (index >= characterUrls.length) {
    // All characters have been fetched, exit recursion
    return;
  }

  request(characterUrls[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      // Fetch the next character
      fetchCharacters(characterUrls, index + 1);
    } else {
      console.log('Error:', error);
    }
  });
}

// Start the script by fetching characters for the given movie ID
getCharacters(movieId);
