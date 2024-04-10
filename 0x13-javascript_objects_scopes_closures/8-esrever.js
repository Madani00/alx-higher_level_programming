#!/usr/bin/node

exports.esrever = function (list) {
  const reverseArr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    const index = list[i];
    reverseArr.push(index);
  }
  return reverseArr;
};
