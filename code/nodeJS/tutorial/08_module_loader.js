console.log("Check results by running: node 08_module_loader");
console.log("If you see errors, please run: node 01_intro");

console.log("A very simple module example.");
var moduleFunction = require('./07_modules');
moduleFunction();

console.log("An http module example.")
var makeRequest = require('./09_module_http')
makeRequest('http req the first');