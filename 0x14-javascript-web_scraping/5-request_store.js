#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request.get({ url: process.argv[2] }, function (error, response, body) {
  if (error) console.log(error);
  const obj = body;
  fs.writeFile(process.argv[3], obj, err => {
    if (err) {
      console.error(err);
    }
  });
});
