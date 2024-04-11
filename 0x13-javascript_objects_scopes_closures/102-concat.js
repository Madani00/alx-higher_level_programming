#!/usr/bin/node

const fs = require('fs');

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

fs.readFile(fileAPath, (err, data) => {
  if (err) {
    console.error(err);
  }
  fs.readFile(fileBPath, (err, data1) => {
    if (err) {
      console.error(err);
    }
    fs.writeFile(fileCPath, data + data1, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
