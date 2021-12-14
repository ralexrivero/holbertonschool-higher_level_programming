#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  list.forEach(count);
  function count (item) {
    if (item === searchElement) {
      n++;
    }
  }
  return n;
};
