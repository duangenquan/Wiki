// Streams: are like channels, where data flows through, including readable and writable data streams.
var http = require('http');

// request is a readable stream
// response is a writable stream
http.createServer(function(request, response){
    response.writeHead(200);

    // pipe helps us write to a writeable stream as soon as you read from a readable stream
    request.pipe(response);

    /*
    // Or, write stream with chunks
    request.on('readable', function(){
        var chunk = null;
        while (null !== (chunk = request.read())){
            response.write(chunk);
        }
    });

    request.on('end', function(){
        response.end('*** end of request *** \n');
    });
    //*/
    
}).listen(8080);


console.log('Listening on port 8080...');
console.log('Check results by running the cmd: curl -d \'from client\' http://localhost:8080');

console.log(`Sample results are: from client`);

