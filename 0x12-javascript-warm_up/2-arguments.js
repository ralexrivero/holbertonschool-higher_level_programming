#!/usr/bin/node

const entry = process.argv.length;

if (entry < 3) {
  console.log('No argument');
} else if (entry === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
