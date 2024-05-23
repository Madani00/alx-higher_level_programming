#!/usr/bin/node

const arg = process.argv;
const request = require('request');

const filmId = arg[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId.toString();

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
