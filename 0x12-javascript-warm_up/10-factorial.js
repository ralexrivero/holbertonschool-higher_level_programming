#!/usr/bin/node

const entry = process.argv;
const x = parseInt(entry[2]);

function factorial (x) {
  if (x <= 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

if (isNaN(x)) {
  console.log(1);
} else {
  console.log(factorial(x));
}
