#!/usr/bin/node
// JS file to use request module to get information from Star Wars API
const request = require('request');

// if (process.argv.length <= 2) { exit(0); }

const StarWarsUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(StarWarsUrl, (error, response, body) => {
  // Print error if error occured
  if (error) { console.log(error); }

  // Store array of character urls into variable
  const json = JSON.parse(body);
  const charactersURL = json.characters;
  // console.log(characters);
  const namesURL = charactersURL.map(
    url => new Promise((resolve, reject) => {
      request(url, (err, res, bdy) => {
        if (err) { reject(err); }
        resolve(JSON.parse(bdy).name);
      });
    }));
  // Resolve all the promises
  Promise.all(namesURL).then(names => console.log(names.join('\n')))
    .catch(e => console.log(e));
});
