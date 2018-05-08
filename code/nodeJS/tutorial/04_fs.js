var fs = require('fs');

var readFile = fs.createReadStream("README.md");
var writeFile = fs.createWriteStream("README_COPY.md");

readFile.pipe(writeFile);

console.log('Please check results by running: node 04_fs');
console.log('The result is to copy README.md as README_COPY.md');