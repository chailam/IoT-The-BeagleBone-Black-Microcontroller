/*
Author: Julian Chong
Date: 20 Jan 2019
A simple web app that will retrive any messages sent from the ground staff and display it on the HTML page.
It can also send any written message back to the database.
*/

var receiveForm = document.getElementById("receiveForm");
var sendForm = document.getElementById("sendForm");
var submitButton = document.getElementById("submitButton")

var messageFromGroundStaff = firebase.database().ref().child("fromGroundStaff");

messageFromGroundStaff.on('value', function(datasnapshot){
    var messages = ""
    datasnapshot.forEach(function(child) {
        messages += child.val();
    })
    if (messages.length > 0) {  // if there are messages from the ground staff
        receiveForm.innerHTML = messages;
    }
    else {
        receiveForm.innerHTML = "No current emergencies.";
    }

});

function submitClick() {
    var firebaseRef = firebase.database().ref(); // get firebase reference
    var messageToSend = sendForm.value;     // get value from receive form
    firebaseRef.child("fromResponseTeam").set(messageToSend); // send to firebase
}
