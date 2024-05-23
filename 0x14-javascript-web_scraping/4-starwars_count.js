#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body).results;
    const dataString = JSON.stringify(data);

    const ver = /people\/18\//g;
    const matche = dataString.match(ver);

    if (matche) {
      console.log(matche.length);
    } else {
      console.log(0);
    }
  }
});
