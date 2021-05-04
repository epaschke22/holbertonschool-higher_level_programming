#!/usr/bin/node
const request = require('request');
const swapi = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get({ url: swapi }, function (error, response, body) {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  console.log(obj.title);
});
