'use strict';

const yelp = require('yelp-fusion');
var readline = require('readline');

var rl = readline.createInterface(process.stdin, process.stdout);

var clientID = 'BlvN6HwRcH8UxKR7Bvn_tA'
var clientSecret = 'no5m4BEV8ERl1zDxOrJqsbk0KLF6IpiwArsFyswogvvQ175CJa5v9x3TW2Fl1oi1'


yelp.accessToken(clientID, clientSecret).then(response => {
  const client = yelp.client(response.jsonBody.access_token);

rl.question('Search what term?', (inTerm) =>
 rl.question('Lat?', (lat) => 
 	rl.question('Long?', (long) =>
  client.search({
  	radius: '40000',
  	term: inTerm,
    latitude: lat,
    longitude: long

    //location: lat

  }).then(response => {
  	for(var i = 0; i < 5; i++) {
    	console.log("[" + response.jsonBody.businesses[i].name + ", " + 
    		response.jsonBody.businesses[i].location.address1 + ", " +
    		response.jsonBody.businesses[i].location.city + ", " +
    		response.jsonBody.businesses[i].location.country + ", " +
    		response.jsonBody.businesses[i].phone + "]");
	}
	rl.close();
	
  }))));
}).catch(e => {
  console.log(e);
});