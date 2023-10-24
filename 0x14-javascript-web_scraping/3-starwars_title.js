#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the API URL using the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error object
    console.error(error);
  } else {
    // Parse the response body as JSON to access the movie title
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
