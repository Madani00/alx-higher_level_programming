#!/usr/bin/node

// a script that prints the addition of 2 integers
const { argv } = require('node:process');

if (argv[3]) {
  console.log(add(parseInt(argv[3]), parseInt(argv[2])));
} else {
  console.log(0 / 0);
}

function add (a, b) {
  const result = a + b;
  return result;
}
