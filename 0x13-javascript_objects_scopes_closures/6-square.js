#!/usr/bin/node

const SquareBase = require('./5-square');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    super.print(c);
  }
};
