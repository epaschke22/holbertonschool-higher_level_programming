#!/usr/bin/node
function fact (input) {
  if (input === 1 || isNaN(input)) {
    return 1;
  }
  return input * fact(input - 1);
}
console.log(fact(parseInt(process.argv[2])));
