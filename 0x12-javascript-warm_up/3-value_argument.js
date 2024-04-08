#!/usr/bin/node

// a script that prints the first argument passed to it
const { argv } = require('node:process');
if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
