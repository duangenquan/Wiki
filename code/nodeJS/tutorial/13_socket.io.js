var express = require('express');
var app = express();
// Create an http server and dispatch the requests to express
var server = require('http').createServer(app);
// Load the socket.io module and allow it to use the http server to listen for requests
var io = require('socket.io')(server);

// Listen for connection events (on socket.io) and define the callback function
io.on('connection', function (client) {
    console.log('Client connected...');
    // Emits the 'messages' event on the clients and sends the object {socket:io}
    client.emit('messages', {socket: 'i.o'})

    client.on('fromClient', function (data) {
        console.log(data);
        console.log('Try to trigger fromServer event');
        // Use broadcast to send a message to all the clients that are connected
        io.sockets.emit("fromServer", {fromServer: 'fromServer'});
    });

})

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/socket.html');
});

server.listen(8080);

console.log('Please check results at http://localhost:8080 --> inspect --> console' );
console.log(`Sample results are: 
client messages: : i.o
fromServer`);
