#!/usr/bin/node

// Import the required Node.js module
const request = require('request');

// Get the URL from the command-line arguments
const url = process.argv[2];

// Send a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    // If an error occurred during the request, print the error object
    console.error(error);
  } else {
    // If successful, print the status code from the response
    console.log(`code: ${response.statusCode}`);
  }
});
