#!/usr/bin/node

// a script that prints x times “C is fun”
const { argv } = require('node:process');

if (argv.length === 2) {
  console.log('Missing number of occurrences');
} else if (parseInt(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
