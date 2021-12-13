#!/usr/bin/node

const entry = process.argv;
const a = parseInt(entry[2]);
const b = parseInt(entry[3]);

function add (a, b) {
  console.log(a + b);
}

add(a, b);
