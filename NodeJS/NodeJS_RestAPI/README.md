# Intro To `ReactJS`
Tools we will use:
1. [NodeJS](https://nodejs.org/en/)
2. ReactJS
3. [Visual Studio Code (IDE)](https://code.visualstudio.com/)
4. ***Optional*** - some kind of REST-api testing tool; I used [postman](https://www.postman.com/downloads/)

## Dependencies
```
npm install express
npm install path
npm install body-parser
npm install nodemon -g
```

## Setup
```js
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

//launch server
var server = app.listen(8081, function () {
   var port = server.address().port
   console.log("Example app listening at http://localhost:%s", port)
})
```

<br><br><br>

## GET
- Used to `get` items
- Only use `parameters (params)` not `body`
```js
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

//launch server
var server = app.listen(8081, function () {
   var port = server.address().port
   console.log("Example app listening at http://localhost:%s", port)
})
```
![image](https://user-images.githubusercontent.com/18486562/100029775-d4074780-2da6-11eb-9333-5dc6a56fde3c.png)

![image](https://user-images.githubusercontent.com/18486562/100029920-352f1b00-2da7-11eb-8a5f-a327092bb5a8.png)

<br><br>

## POST
- Used to `get` items
- can use both `parameters (params)` and `body`
```js
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

//POST with body
app.post('/add', function (req, res) {
    database[database.length] = req.body.fruit //add to database array
    res.status(200).send(req.body)
})

//launch server
var server = app.listen(8081, function () {
   var port = server.address().port
   console.log("Example app listening at http://localhost:%s", port)
})
```
![image](https://user-images.githubusercontent.com/18486562/100029920-352f1b00-2da7-11eb-8a5f-a327092bb5a8.png)

![image](https://user-images.githubusercontent.com/18486562/100030083-8e974a00-2da7-11eb-9787-8321dfad8457.png)

<br><br>

## PUT
- Used to `update` items
- can use both `parameters (params)` and `body`
```js
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

//PUT method route
app.put('/put/:index/:item', function (req, res) {
    database[req.params.index] = req.params.item
    res.status(200).send(req.params)
})

//launch server
var server = app.listen(8081, function () {
   var port = server.address().port
   console.log("Example app listening at http://localhost:%s", port)
})
```
![image](https://user-images.githubusercontent.com/18486562/100030215-d6b66c80-2da7-11eb-858d-7b71e058091c.png)

![image](https://user-images.githubusercontent.com/18486562/100030482-7a078180-2da8-11eb-9676-56cf3976c721.png)

<br><br>

## DELETE
- Used to `delete` items
- can use both `parameters (params)` and `body`
```js
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

//launch server
var server = app.listen(8081, function () {
   var port = server.address().port
   console.log("Example app listening at http://localhost:%s", port)
})
```
![image](https://user-images.githubusercontent.com/18486562/100030623-d10d5680-2da8-11eb-8c79-3385677b1f95.png)

![image](https://user-images.githubusercontent.com/18486562/100030723-087c0300-2da9-11eb-86df-bc5293bb904a.png)

![image](https://user-images.githubusercontent.com/18486562/100030762-1d589680-2da9-11eb-8197-761647164c41.png)

<br><br>

## Serving HTML (or anything) files
- Make `.html` files to serve, save them in the same directory
```html
<h1>STATIC HTML WEBSITE</h1>

<p>Served by <a href='https://expressjs.com/'>ExpressJS</a></p>
```

- Used `GET`
```js
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

//GET serve html
app.get('/html', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

//launch server
var server = app.listen(8081, function () {
   var port = server.address().port
   console.log("Example app listening at http://localhost:%s", port)
})
```
![image](https://user-images.githubusercontent.com/18486562/100031462-90164180-2daa-11eb-88af-12d237278bca.png)

<br><br><br>

## We are DONE!
[More routing options!](https://expressjs.com/en/guide/routing.html)