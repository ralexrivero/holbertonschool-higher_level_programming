#!/usr/bin/node

const entry = process.argv;

if (entry[2] === undefined) {
  console.log('No argument');
} else {
  console.log(entry[2]);
}
