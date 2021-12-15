#!/usr/bin/node

exports.esrever = function (list) {
  const newl = [];
  while (list.length) {
    newl.push(list.pop());
  }
  return newl;
};
