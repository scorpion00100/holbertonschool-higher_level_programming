#!/usr/bin/node
// script that prints x times

let x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let output = "";
  for (let i = 0; i < x; i++) {
    output += 'C is fun\n';
  }
  console.log(output.trim());
}
