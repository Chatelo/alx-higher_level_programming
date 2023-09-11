#!/usr/bin/node

const arg = process.argv[2];
const convertedNumber = parseInt(arg);

if (isNaN(convertedNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertedNumber}`);
}
