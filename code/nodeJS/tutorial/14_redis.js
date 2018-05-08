console.log(`This is an example for redis, an open source in-memory data structure store.
Please check results by running: node 14_redis
If you see some errors, please run:
    npm install redis --save
    redis-server`);

var redis = require('redis');
var client = redis.createClient();

// Set commands in the database by setting key-value entries
client.set("1", "one");
client.set("2", "two");
client.set("3", "three");

// To retrieve values from the database
client.get("1", function (err, reply) {
    // Commands are non-blocking
    console.log("Sample results are: " + reply);
});

// To retrieve values from the database
client.get("0", function (err, reply) {
    console.log(reply);
});