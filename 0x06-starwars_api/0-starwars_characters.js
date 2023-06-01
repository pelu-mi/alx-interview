#!/usr/bin/node
// JS file to use request module to get information from Star Wars API
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
let characters = 'hi'
let json = []

request(url, (error, response, body) => {
  // Print error if error occured
  if (error)
    console.log(error);

  // Store array of character urls into variable
  json = JSON.parse(body);
  characters = json.characters;

  print_characters(characters);
});


const print_characters = function (characters) {
  // Print the name of each character
  for (let c of characters) {
    request(c, (err, res, bdy) => {
      let person = JSON.parse(bdy);
      console.log(person.name);
    });
  }
};
