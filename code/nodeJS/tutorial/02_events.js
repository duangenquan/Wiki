// NodeJS triggers events and handles the callback functions.

// Loading the EventEmitter constructor
var EventEmitter = require('events').EventEmitter;

console.log('Show event examples.');

// logger emits Events by adding a listener
var logger = new EventEmitter(); 

// An example to listen to the error event and  excutethe callback function
logger.on('error', function(message){
    console.log('ERR: '  + message);
});

// Triggers the 'error' event
logger.emit('error', 'This is the first error!');
logger.emit('error', 'This is the second error!');