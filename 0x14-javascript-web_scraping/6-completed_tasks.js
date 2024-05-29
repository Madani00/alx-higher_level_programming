#!/usr/bin/node

const request = require('request');
const arg = process.argv;

request(arg[2], (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body);

    const result = {};
    data.forEach(item => {
      if (!(item.userId in result) && item.completed) {
        result[item.userId] = 1;
      } else if (item.completed) {
        result[item.userId] += 1;
      }
    });
    console.log(result);
  }
});
