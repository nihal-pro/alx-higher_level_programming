#!/usr/bin/node
const Args = process.argv.slice(2);
const number1 = parseInt(Args[0]);
const number2 = parseInt(Args[1]);

function add (a, b) {
  console.log(a + b);
}

if (isNaN(number1) || isNaN(number2)) {
  console.log('NaN');
} else {
  add(number1, number2);
}
