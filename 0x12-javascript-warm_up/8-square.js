#!/usr/bin/node

// a script that prints a square
const { argv } = require('node:process');
const k = parseInt(argv[2]);

if (!isNaN(argv[2])) {
  for (let i = 0; i < k; i++) {
    let row = '';
    for (let j = 0; j < k; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
