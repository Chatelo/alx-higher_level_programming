#!/usr/bin/node

// This script reads and prints the content of a file

// Import the required Node.js modules
const argv = process.argv; // The command-line arguments array
import { readFile } from 'fs'; // File system module to read files

// Read the content of the file asynchronously in utf-8 encoding
readFile(argv[2], 'utf8', function (err, data) {
	if (err) {
		// If an error occurred during reading, print the error object
		console.log(err);
	} else {
		// If successful, print the content of the file
		console.log(data);
	}
});
