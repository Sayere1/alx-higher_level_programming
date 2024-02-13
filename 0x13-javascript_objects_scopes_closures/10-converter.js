#!/usr/bin/node
// func that converts a num from base 10 to another base passed as arg
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
