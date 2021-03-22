#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let total = process.argv.length;
  let a = process.argv;
  let temp;
  for (let i = 0; i < total; i++) {
    for (let j = i + 1; j < total; j++) {
      if (parseInt(a[i]) > parseInt(a[j])) {
        temp = a[i];  
        a[i] = a[j];  
        a[j] = temp;
      }
    }
  }
  console.log(a[total-2]);
}
