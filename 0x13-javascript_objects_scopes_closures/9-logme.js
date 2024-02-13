#!/usr/bin/node
// function that prints num of arg already printed and the new arg value
let count = 0;
exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
