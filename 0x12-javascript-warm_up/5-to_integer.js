#!/usr/bin/node

// a script that prints My number: <first argument converted in integer>
const { argv } = require('node:process');

if (argv.length === 2) {
  console.log('Not a number');
} else if (parseInt(argv[2])) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
