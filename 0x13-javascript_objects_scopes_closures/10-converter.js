#!/usr/bin/env

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
