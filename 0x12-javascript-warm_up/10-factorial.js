#!/usr/bin/node
const Args = process.argv.slice(2);
const Num = parseInt(Args[0]);

function Factorial (Number) {
  if (Number === 1) {
    return 1;
  }
  return Number * Factorial(Number - 1);
}

if (isNaN(Num)) {
  console.log('1');
} else {
  console.log(Factorial(Num));
}
