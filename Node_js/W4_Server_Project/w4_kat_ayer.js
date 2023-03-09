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
var path = require('path');
var port = process.env.PORT || 23456;

// Start server
http.createServer(app).listen(port);
console.log('Express server listening on port ' + port + '.');
console.log('Visit http://localhost:' + port + ' in a browser to view.');

// Fetch HTML and assign pages
app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, '/public/home.html'));
});

app.get('/about', function (req, res) {
    res.sendFile(path.join(__dirname, '/public/about.html'));
});

app.get('/ethics', function (req, res) {
    res.sendFile(path.join(__dirname, '/public/ethics.html'));
});

app.get('/store', function (req, res) {
    res.sendFile(path.join(__dirname, '/public/shop.html'));
});