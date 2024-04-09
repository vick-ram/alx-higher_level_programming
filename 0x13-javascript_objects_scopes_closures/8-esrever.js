#!/usr/bin/node
exports.esrever = function (list) {
  const last = list.length - 1;
  const reversedList = [];
  for (let i = last; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
