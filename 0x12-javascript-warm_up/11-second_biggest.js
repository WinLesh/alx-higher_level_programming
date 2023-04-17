#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2).map(Number);
  const sbiggest = list.sort(function (l, s) { return l - s; })[1];
  console.log(sbiggest);
}
