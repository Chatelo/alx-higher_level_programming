#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurred during the request, print the error object
    console.error(error);
  } else {
    // Write the response body to the specified file path in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        // If an error occurred during writing, print the error object
        console.error(err);
      }
    });
  }
});
