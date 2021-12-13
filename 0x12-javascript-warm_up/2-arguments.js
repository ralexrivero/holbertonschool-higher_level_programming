#!/usr/bin/node

const entry = process.argv.length;

if (entry < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
