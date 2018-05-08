var fs = require('fs');
var http = require('http');
// This example reads from the request and pipes it to a file
http.createServer(function (request, response) {
    var writeFile = fs.createWriteStream("README_UPLOAD.md");

    // Upload file directly
    // request.pipe(writeFile);

    // Upload files with progresses
    var fileBytes = request.headers['content-length'];
    var uploadedBytes = 0;
    request.on('readable', function () {
        var chunk = null;
        while (null !== (chunk = request.read())) {
            // The following code calculates the file upload progress and writes it to the response
            uploadedBytes += chunk.length;
            var progress = (uploadedBytes / fileBytes) * 100;
            response.write("progress: " + parseInt(progress, 10) + "%\n");
        }
    });

    request.on('end', function () {
        response.end('uploaded\n');
    });
}).listen(8080);

console.log('Check results by running the cmd: curl --upload-file README.md http://localhost:8080');
console.log('Or curl -T README.md http://localhost:8080');
console.log(`The result is to upload README.md as README_UPLOAD.md with messages: 
progress: 100%
uploaded`);