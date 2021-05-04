#!/usr/bin/node
const request = require('request');
request.get({ url: process.argv[2] }, function (error, response, body) {
  if (error) console.log(error);
  const tasklist = JSON.parse(body);
  const output = {};
  for (const task of tasklist) {
    if (task.completed === true) {
      if (!output[task.userId]) {
        output[task.userId] = 1;
      } else {
        output[task.userId] += 1;
      }
    }
  }
  console.log(output);
});
