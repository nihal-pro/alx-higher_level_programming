#!/usr/bin/node
const Args = process.argv.slice(2);

if (Args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(Args[0]);
}
