#!/usr/bin/node
const request = require('request');
const movie = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get({ url: movie }, function (error, response, body) {
  if (error) console.error(error);
  const charList = JSON.parse(body).characters;
  for (const charUrl of charList) {
    request.get({ url: charUrl }, function (error, response, body) {
      if (error) console.error(error);
      console.log(JSON.parse(body).name);
    });
  }
});
