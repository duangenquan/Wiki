// NodeJS is an open-source, cross-platform JavaScript run-time environment that executes JavaScript code server-side.

var http = require('http');

http.createServer(function(request, response){
    response.writeHead(200);
    response.write("Introduction");
    response.end();
}).listen(8080);

console.log('Listening to port 8080');