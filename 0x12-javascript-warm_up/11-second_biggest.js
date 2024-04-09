#!/usr/bin/node

// a script that searches the second biggest integer in the list of arguments.
const { argv } = require('node:process');

if (isNaN(argv[2]) || argv[2] === '1') {
  console.log('0');
} else {
  const arrg = argv.slice(2);
  arrg.sort((x, y) => (parseInt(y) - parseInt(x)));
  console.log(arrg[1]);
}
