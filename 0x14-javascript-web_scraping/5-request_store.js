#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const arg = process.argv;

request(arg[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(arg[3], body, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
