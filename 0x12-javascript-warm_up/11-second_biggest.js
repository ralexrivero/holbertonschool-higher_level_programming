#!/usr/bin/node

const entry = process.argv;
let nearBig = entry.sort();
nearBig = entry[entry.length - 2];

if (entry.length <= 3) {
  console.log(0);
} else {
  console.log(nearBig);
}
