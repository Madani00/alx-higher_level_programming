#!/usr/bin/node

// a script that prints a message depending of the number of arguments passed:
const { argv } = require('node:process');
if (argv[2]) {
	console.log('Argument found');
} else {
	console.log('No argument');
}
