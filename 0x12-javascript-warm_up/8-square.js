#!/usr/bin/node

// a script that prints a square
const { argv } = require('node:process');
const k = parseInt(argv[2]);

if (argv.length === 2) {
  console.log('Missing size');
} else if (k) {
  let myVar = '';
  for (let i = 0; i < k; i++) {
    for (let k = 0; k < k; i++) {
      myVar += 'X';
    }
    console.log(myVar);
  }
  
} else {
  console.log('Missing size');
}
