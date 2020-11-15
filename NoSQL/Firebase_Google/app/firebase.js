var axios = require('axios');
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

//delete in Database
function deleteDB() { 
    /**
     * remove an object to database under category "people" and sub-id "person1"
     */
    firebase.database().ref('people/person1').remove();
    console.log("Done removing an item")
}
deleteDB() //call delete function