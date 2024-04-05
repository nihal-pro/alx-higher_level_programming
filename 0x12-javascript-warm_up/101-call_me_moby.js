#!/usr/bin/node
module.exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let i = 1; i <= x; ++i) {
    theFunction();
  }
};
