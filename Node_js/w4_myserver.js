/*
// This application to demo the use of restfull services
// This is the core for any MV* pattern
// let me know if you have any question 
// use express server, it must be in the node_modules
*/

// setup
var express = require("express");
var http = require("http");
var app = express();

// run the server 
http.createServer(app).listen(55555);
console.log('Express server listening on port 55555');

// This is the general route URL - http://localhost:55555
app.get('/', function (req, res) {
    var msg = ""
    msg += '<center><h1> This is the default page. </h1></center>'
    msg += 'use the following: <br />'
    msg += '<ul><li><a href="http://localhost:55555/hello">http://localhost:55555/hello</a></li>'
    msg += '<li><a href="http://localhost:55555/goodbye">http://localhost:55555/goodbye</a></li>'
    msg += '<li><a href="http://localhost:55555/products">http://localhost:55555/products</a></li>'
    msg += '<li><a href="http://localhost:55555/products/2">http://localhost:55555/products/2</a></li></ul>'
    res.send(msg);
});

// This is the Hello URL - http://localhost:55555/hello
app.get("/hello", function(req,res){
    res.send("Hello, ENTD261!");
});

//This is for the /goodbye page
app.get("/goodbye", function (req, res) {
    res.send("Thank you, ENTD261!");
});

// Products URL - http://localhost:55555/products
app.get("/products", function (req, res) {
    res.send(JSON.stringify(products));
});

// Products/2 URL - http://localhost:55555/products/2
app.get("/products/:id", function (req, res) {
    if (req.params.id > (products.length - 1) || req.params.id < 0) {
        res.statusCode = 404;
        res.end("Not Found");
    }
    res.send(JSON.stringify(products[req.params.id]));
});


var products = [
    { id: 0, name: 'watch', description: 'Tell time with this amazing watch', price: 30.00 },
    { id: 1, name: 'sandals', description: 'Walk in comfort with these sandals', price: 10.00 },
    { id: 2, name: 'sunglasses', description: 'Protect your eyes in style', price: 25.00 }
]; 