#!/usr/bin/node
const dic = require('./101-data').dict;
const newDic = {};

Object.keys(dic).forEach((key) => {
    let arr = [];
    if(dic[key] === 1) {
        arr.push(key);
    }
    newDic.push(arr);
});

console.log(newDic);
