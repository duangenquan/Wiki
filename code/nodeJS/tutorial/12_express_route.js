// http://localhost:8080/images/stone@wizr.com

var express = require('express');
var request = require('request');
var url = require('url');
var crypto = require('crypto');
var app = express();

// Create an end-point with the following syntax
// By using ':', we specify that we will use a dynamic parameter
app.get('/images/:email', function (req, response) {

    // Use the information from the request parameters
    var email = req.params.email;
    // The gravatar API requires a Hash of the 'email' parameter
    var hash = crypto.createHash('md5').update(email).digest('hex');

    // As usual, it is possible to specify the set of options in an object
    var options = {
        protocol: "http",
        host: 'gravatar.com',
        pathname: '/avatar/' + hash,
        query: {size: 80}
    }

    // Make a request with the URL
    var gravatarUrl = url.format(options);

    console.log(gravatarUrl);

    console.log(options);

    // Pipe the request to the response
    request(gravatarUrl).pipe(response);

});

app.listen(8080);

console('Please check results in http://localhost:8080/images/youremail@x.com');
console(`Sample results show an AVATAR image for the given email`);