#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  } else if (isNaN(n)) {
    return 1;
  }
  const fact = n * factorial(n - 1);
  return fact;
}

const result = factorial(Number(process.argv[2]));
console.log(result);
