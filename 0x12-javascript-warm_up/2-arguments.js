#!/usr/bin/node
const Args = process.argv.slice(2);

if (Args.length > 1) {
  console.log('Arguments found');
} else if (Args.length === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
