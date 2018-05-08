// Express is a web development framework for nodejs
// npm install --save express

// In order to start the web application, we need to load the library
var express = require('express');

// Create an instance of express
var app = express();

// Define end-points in the following way
// '/' is the root route
app.get('/', function (request, response) {
    //Read a file from the file system and send it back to the response
    response.sendFile(__dirname + "/README.md");
});
// Receive requests at port 8080
app.listen(8080);

console.log("Please check results in http://localhost:8080/");
console.log(`Sample results show the content of README.md`);
