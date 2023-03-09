/*
    Title:          RESTful Node.js Application
    Author:         Kat Ayer
    Due Date:       March 5, 2025
    Class:          ENTD261
    University:     American Public University
*/

// Setup
var express = require('express');
var http = require('http');
var http = require('http');
var app = express();
var homeRouter = require(".routes/home.js");
var aboutRouter = require(".routes/about.js")
var ethicsRouter = require(".routes/ethics.js")
var shopRouter = require(".routes/shop.js")

// Start server
http.createServer(app).listen(23456);
console.log('Express server listening on port 23456.');
console.log('Visit http://localhost:23456 in a browser to view.');

// Create and assign pages
app.use("/", homeRouter);
app.use("/about", aboutRouter);
app.use("/ethics", ethicsRouter);
app.use("/shop", shopRouter);