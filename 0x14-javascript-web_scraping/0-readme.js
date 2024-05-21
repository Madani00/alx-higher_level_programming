#!/usr/bin/node

const arg = process.argv;
const fs = require('fs');

fs.readFile(arg[2], 'utf-8', function (err, data) {
  if (err) throw err;

  console.log(data);
});
