#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const map1 = list.map((cV, idx) => cV * idx);
console.log(map1);
