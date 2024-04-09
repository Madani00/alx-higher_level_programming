#!/usr/bin/node

// a script that computes and prints a factorial
const { argv } = require('node:process');

function factorial (num) {
  // Base case
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(factorial(parseInt(argv[2])));
}
