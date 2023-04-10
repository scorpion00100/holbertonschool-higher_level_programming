#!/usr/bin/node
// script that prints x times

const arg = process.argv[2];

if (!arg) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(arg);

  if (isNaN(x)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
