#!/usr/bin/node
exports.converter = function (base) {
  function theConverter (number) {
    return (number.toString(base));
  }
  return (theConverter);
};
