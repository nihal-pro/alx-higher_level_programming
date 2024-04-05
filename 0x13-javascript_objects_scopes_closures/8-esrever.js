#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  for (let i = list.length - 1; i !== -1; --i) {
    revList.push(list[i]);
  }
  return (revList);
};
