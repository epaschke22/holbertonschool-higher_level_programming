#!/usr/bin/node
const dict = require('./101-data.js').dict;
output = {};
for (const key in dict) {
  if (output[dict[key]] === undefined) {
    output[dict[key]] = [key];
  } else {
    output[dict[key]].push(key);
  }
}
console.log(output);
