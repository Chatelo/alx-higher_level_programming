#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments (process.argv[2])
const url = process.argv[2];

// Create an object to store the count of completed tasks for each user
const myDict = {};

// Make an HTTP GET request to the provided API URL
request(url, function (error, response, body) {
  if (error) {
    // If there's an error in the request, handle it properly
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Unable to fetch data from the API');
    return;
  }

  // Parse the response body (which is in JSON format) into a JavaScript object
  const todos = JSON.parse(body);

  // Iterate over each element (todo) in the response
  for (const todo of todos) {
    // Check if the todo is completed (property 'completed' is true)
    if (todo.completed) {
      // If the user id is not in 'myDict', initialize it to 1.
      // Otherwise, increment the count by 1.
      if (myDict[todo.userId] === undefined) {
        myDict[todo.userId] = 1;
      } else {
        myDict[todo.userId] += 1;
      }
    }
  }

  // Print the 'myDict' object, which contains the count of completed tasks for each user
  console.log(myDict);
});
