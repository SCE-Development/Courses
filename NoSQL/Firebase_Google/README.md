# Firebase Quick Tutorial by SCE

1. You can use Firebase through plain JS `<script/>` for non-framework projects. Follow this [document](https://firebase.google.com/docs/web/setup).
2. More information for various platforms (Android, IOS, Unity,...) can be found [here](https://firebase.google.com/docs/web/setup).
2. In this tutorial, We will simply play around with their RESTFUL-api calls through NodeJS. Highly compatible with REACTJS or writing your own RESTFUL-api.

## Setup
1. [VSCODE](https://code.visualstudio.com/) or any editor.
2. [NodeJS](https://nodejs.org/en/download/)

<br><br><br>

# Letss gooo
Make a new `firebase.js` (name it anything you want) file somewhere on your computer and open it with your editor.

## Dependencies
In the same directory of that `firebase.js` in your terminal:
```
npm install firebase
```

## Code in firebase.js:
import axios and firebase: 
```js
var firebase = require('firebase');
```

<br><br><br>

## Setting up Firebase on GoogleFirebase:
1. Login - [https://console.firebase.google.com/?pli=1](https://console.firebase.google.com/?pli=1)
2. Add a new project. Follow through the creation steps.

![image](https://user-images.githubusercontent.com/18486562/99196712-05e33300-2743-11eb-8c23-9ae3b5005f60.png)

3. Choose your platform, we will choose `web project - </>`

![image](https://user-images.githubusercontent.com/18486562/99196831-9e79b300-2743-11eb-9e30-109d6cd21d54.png)

4. Save the `FirebaseConfig` keys in `firebase.js`

![image](https://user-images.githubusercontent.com/18486562/99196896-f6b0b500-2743-11eb-86ce-e47940d22dc9.png)

Code:
```js
var firebase = require('firebase');

var firebaseConfig = {
    apiKey: "AIzaSyCJUEHtW8DJiKnX2QBV__Cf5vvoieB0t94",
    authDomain: "sce-test-853a6.firebaseapp.com",
    databaseURL: "https://sce-test-853a6.firebaseio.com",
    projectId: "sce-test-853a6",
    storageBucket: "sce-test-853a6.appspot.com",
    messagingSenderId: "806778682337",
    appId: "1:806778682337:web:2e8b23b928d2f6ccfdf0a0",
    measurementId: "G-HP2VKX8N99"
};
//Init Firebase
firebase.initializeApp(firebaseConfig);
```

5. Navigate to `Realtime Database`

![image](https://user-images.githubusercontent.com/18486562/99196972-4a230300-2744-11eb-9fe0-7edb78545c97.png)

6. Create a database if you don't already have one

![image](https://user-images.githubusercontent.com/18486562/99196999-6a52c200-2744-11eb-8963-55d6599db55f.png)


![image](https://user-images.githubusercontent.com/18486562/99197028-a38b3200-2744-11eb-834b-9c5099b2f88f.png)

You can later change the rules to permanent (basically free access for anyone from the outside - dangerous for serious projects) with:
```json
{
  "rules": {
    ".read": true,  // forever able to read 
    ".write": true,  // forever able to write
  }
}
```

7. Done and Ready

![image](https://user-images.githubusercontent.com/18486562/99197080-10063100-2745-11eb-9d89-8ff5867f382a.png)

You can simply start adding items to your db (but thats lame):

![image](https://user-images.githubusercontent.com/18486562/99197118-52c80900-2745-11eb-82ff-15f668701b1e.png)

<br><br><br>

## Lets write some code!

## Writing to database
```js
var firebase = require('firebase');

var firebaseConfig = {
    apiKey: "AIzaSyCJUEHtW8DJiKnX2QBV__Cf5vvoieB0t94",
    authDomain: "sce-test-853a6.firebaseapp.com",
    databaseURL: "https://sce-test-853a6.firebaseio.com",
    projectId: "sce-test-853a6",
    storageBucket: "sce-test-853a6.appspot.com",
    messagingSenderId: "806778682337",
    appId: "1:806778682337:web:2e8b23b928d2f6ccfdf0a0",
    measurementId: "G-HP2VKX8N99"
};
//Init Firebase
firebase.initializeApp(firebaseConfig);

//Write to Database
function write() { 
    let obj = {
        name: "SCE",
        Age: "31"       //yes we are old :<
    }

    /**
     * Add an object to database under category "people" and sub-id "person1"
     */
    firebase.database().ref('people/person1').set(obj);
    console.log("Done adding an item")
}
write() //call write function
```
![image](https://user-images.githubusercontent.com/18486562/99197361-e4844600-2746-11eb-8484-8fcb7022d3e0.png)

Check firebase:

![image](https://user-images.githubusercontent.com/18486562/99197395-1eede300-2747-11eb-90f0-6a4453b6cf53.png)

<br><br>

## Update Item to database
We can do the same `set` function with a new `obj` and the same id `people/person1`
```js
var firebase = require('firebase');

var firebaseConfig = {
    apiKey: "AIzaSyCJUEHtW8DJiKnX2QBV__Cf5vvoieB0t94",
    authDomain: "sce-test-853a6.firebaseapp.com",
    databaseURL: "https://sce-test-853a6.firebaseio.com",
    projectId: "sce-test-853a6",
    storageBucket: "sce-test-853a6.appspot.com",
    messagingSenderId: "806778682337",
    appId: "1:806778682337:web:2e8b23b928d2f6ccfdf0a0",
    measurementId: "G-HP2VKX8N99"
};
//Init Firebase
firebase.initializeApp(firebaseConfig);

//Write to Database
function write() { 
    let obj = {
        name: "Software and Computer Engineering Society",
        Age: "31",       //yes we are old :<
        Room: "Engr294"
    }

    /**
     * Add an object to database under category "people" and sub-id "person1"
     */
    firebase.database().ref('people/person1').set(obj);
    console.log("Done adding an item")
}
write() //call write function
```
![image](https://user-images.githubusercontent.com/18486562/99197361-e4844600-2746-11eb-8484-8fcb7022d3e0.png)

![image](https://user-images.githubusercontent.com/18486562/99197506-cb2fc980-2747-11eb-99e9-791c421e91ef.png)

<br><br>

## Read in database
```js
var firebase = require('firebase');

var firebaseConfig = {
    apiKey: "AIzaSyCJUEHtW8DJiKnX2QBV__Cf5vvoieB0t94",
    authDomain: "sce-test-853a6.firebaseapp.com",
    databaseURL: "https://sce-test-853a6.firebaseio.com",
    projectId: "sce-test-853a6",
    storageBucket: "sce-test-853a6.appspot.com",
    messagingSenderId: "806778682337",
    appId: "1:806778682337:web:2e8b23b928d2f6ccfdf0a0",
    measurementId: "G-HP2VKX8N99"
};
//Init Firebase
firebase.initializeApp(firebaseConfig);

//Read to Database
async function read() { 
    /**
     * read all objects under category "people"
     */
    var data ;
    await firebase.database().ref('people').once('value').then(function(snapshot) {
        data = snapshot.val();
    });
    console.log(data)
}
read() //call read function
```
![image](https://user-images.githubusercontent.com/18486562/99198373-fcf75f00-274c-11eb-961f-05c6364853ba.png)

<br><br>

## Delete Item to database
We can do the same with `remove` function with the same id `people/person1`
```js
var firebase = require('firebase');

var firebaseConfig = {
    apiKey: "AIzaSyCJUEHtW8DJiKnX2QBV__Cf5vvoieB0t94",
    authDomain: "sce-test-853a6.firebaseapp.com",
    databaseURL: "https://sce-test-853a6.firebaseio.com",
    projectId: "sce-test-853a6",
    storageBucket: "sce-test-853a6.appspot.com",
    messagingSenderId: "806778682337",
    appId: "1:806778682337:web:2e8b23b928d2f6ccfdf0a0",
    measurementId: "G-HP2VKX8N99"
};
//Init Firebase
firebase.initializeApp(firebaseConfig);

//delete in Database
function deleteDB() { 
    /**
     * remove an object to database under category "people" and sub-id "person1"
     */
    firebase.database().ref('people/person1').remove();
    console.log("Done removing an item")
}
deleteDB() //call delete function
```
![image](https://user-images.githubusercontent.com/18486562/99197080-10063100-2745-11eb-9d89-8ff5867f382a.png)

<br><br><br>

# DONE
Congrate you are now firebase.