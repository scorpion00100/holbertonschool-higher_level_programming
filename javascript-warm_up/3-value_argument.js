#!/usr/bin/node
//prints the first argument passed to it

const [,, arg] = process.argv;

if (arg) {
  console.log(arg);
} else {
  console.log('Aucun argument');
}
