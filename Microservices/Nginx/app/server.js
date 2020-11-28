var express = require('express');

//server1
var app = express();
var port = 8081
app.get('/', function (req, res) {
    res.status(200).send("Server on "+port)
})
app.listen(port, ()=>{console.log(port)})

//server 2
var app2 = express();
var port2 = 8082
app2.get('/', function (req, res) {
    res.status(200).send("Server on "+port2)
})
app2.listen(port2, ()=>{console.log(port2)})

//server 3
var app3 = express();
var port3 = 8083
app3.get('/', function (req, res) {
    res.status(200).send("Server on "+port3)
})
app3.listen(port3, ()=>{console.log(port3)})