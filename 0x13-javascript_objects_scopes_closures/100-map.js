#!/usr/bin/node
const map1 = require('./100-data').list;

console.log(map1);
let n = 0;
const myVar = map1.map((x) => x * `${n++}`);
console.log(myVar);
