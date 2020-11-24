var express = require('express');
var app = express();
var path = require('path');
var bodyParser = require('body-parser');

//Parsing format
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(bodyParser.raw());

//database
let database = ['apple']

//GET
app.get('/', function (req, res) {
   res.status(200).send(database)
})

//GET with params
//GET cannot have body
app.get('/add/:fruit/', function (req, res) {
    database[database.length] = req.params.fruit //add to database array
    res.status(200).send(database)
})

//POST with body
app.post('/add', function (req, res) {
    database[database.length] = req.body.fruit //add to database array
    res.status(200).send(req.body)
})

//PUT method route
app.put('/put/:index/:item', function (req, res) {
    database[req.params.index] = req.params.item
    res.status(200).send(req.params)
})

//DELETE method route
app.delete('/delete', function (req, res) {
    let index = req.body.index
    if(index < 0){
        res.status(400).send("Nahhh, index has to be bigger than -1")
    }
    else {
        database.splice(index, 1)
        res.status(200).send("removed index: "+ req.body.index)
    }
})

//GET serve html
app.get('/html', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

//launch server
var server = app.listen(8081, function () {
   var port = server.address().port
   console.log("Example app listening at http://localhost:%s", port)
})
