#!/usr/bin/node
const Args = process.argv.slice(2);
const len = Args.length;

if (len <= 1) {
  console.log(0);
} else {
  console.log(Args.sort((a, b) => b - a)[1]);
}
