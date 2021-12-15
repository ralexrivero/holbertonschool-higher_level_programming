#!/usr/bin/env

exports.converter = function (base) {
  return value => value.toString(base);
};
