#!/usr/bin/node

const entry = process.argv;
const side = parseInt(entry[2]);
let x;

if (isNaN(side)) {
  console.log('Missing size');
} else {
  for (x = 0; x < side; x++) {
    console.log('X'.repeat(side));
  }
}
