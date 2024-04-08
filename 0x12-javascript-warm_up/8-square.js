#!/usr/bin/node

// a script that prints a square
const { argv } = require('node:process');
let myVar;

if (argv.length === 2) {
  console.log('Missing size');
} else if (parseInt(argv[2])) {
  let myVar = '';
  for (let i = 0; i < argv[2]; i++) {
    for (let k = 0; k < argv[2]; i++) {
      myVar += 'X';
    }
    myVar += '\n';
  }
  console.log(myVar);
} else {
  console.log('Missing size');
}
