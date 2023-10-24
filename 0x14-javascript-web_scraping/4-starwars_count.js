#!/usr/bin/node
// Prints the number of movies where "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2]; // Get the API URL from the command-line arguments

request(url, function (err, res, body) {
  if (err) {
    // If an error occurred during the request, print the error object
    console.log(err);
  } else if (res.statusCode === 200) {
    // If the request was successful (status code 200), proceed

    // Parse the response body as JSON and access the "results" array
    const films = JSON.parse(body).results;

    let count = 0; // Initialize the count to 0

    // Iterate through each movie
    for (let i = 0; i < films.length; i++) {
      // Iterate through each character in the movie
      for (let j = 0; j < films[i].characters.length; j++) {
        // Check if the character includes the ID for "Wedge Antilles" (ID: 18)
        if (films[i].characters[j].includes('/18/')) {
          // If found, increment the count
          count++;
        }
      }
    }
    // Print the final count of movies where "Wedge Antilles" is present
    console.log(count);
  } else {
    // If the request returned an invalid response, print 'Invalid'
    console.log('Invalid');
  }
});
