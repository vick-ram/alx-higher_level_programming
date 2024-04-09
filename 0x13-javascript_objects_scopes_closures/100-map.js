#!/usr/bin/node
const arr = require('./100-data').list;
const newList = arr.map((value, index) => value * index);
console.log(arr);
console.log(newList);
