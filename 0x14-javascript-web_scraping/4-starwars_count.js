#!/usr/bin/node
// script that prints num of movies where char “Wedge Antilles” is present.

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/')
      )
        ? count + 1
        : count;
    }, 0));
  }
}
);
