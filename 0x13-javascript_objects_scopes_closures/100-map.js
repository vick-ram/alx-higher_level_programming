#!/usr/bin/node
const { list } = require('./100-data');
console.log(list);
const newList = list.map((index, value) => index * value);
console.log(newList);
