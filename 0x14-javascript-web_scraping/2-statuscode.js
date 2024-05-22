#!/usr/bin/node

const arg = process.argv;
const request = require('request');

request(arg[2], (err, res, body) => {
  if (err) {
    console.log('code:', res.statusCode);
  }
  console.log('code:', res.statusCode);
});
