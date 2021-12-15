#!/usr/bin/env

exports.converter = function (base) {
  return (number) => {
    return number.toString(base);
  };
};
