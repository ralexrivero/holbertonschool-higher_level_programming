#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w || h) <= 0 || (w || h) === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print (c) {
    this.c = c;
    if (c === undefined) {
      c = 'X';
    }

    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
