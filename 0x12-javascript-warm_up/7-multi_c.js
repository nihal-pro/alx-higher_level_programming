#!/usr/bin/node
const Args = process.argv.slice(2);
const number = parseInt(Args[0]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  for (let x = 0; x < number; x++) {
    console.log('C is fun');
  }
}
