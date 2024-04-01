#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const New = list.map((x, i) => x * i);
console.log(New);
