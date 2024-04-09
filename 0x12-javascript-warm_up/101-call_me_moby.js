#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  return Array.from({length: x}, () => theFunction());
};
