/*
Author: Teh Run Xun
Modified: Loi Chai Lam & Steven Tan 
Date: 18 Jan 2019
This web server will act as the response team and when the response team press the on button, the led light will light up.
The led light will turn off when the off button is pressed.
When the ground staff press the button on the BBB, the web server will received the message of robbery in progress. All good otherwise.
Web Page: http://192.168.7.2:8888/
Reference from https://randomnerdtutorials.com/programming-the-beaglebone-black-with-bonescript/
*/

// Load the required modules
var http = require('http');
var fs = require('fs');
var bs = require('bonescript');

// The pin key of led light
var led = "P8_11";
// The pin key of button
var button = "P8_19";

// Pin the Mode to connect the output
bs.pinMode(led, bs.OUTPUT);
bs.pinMode(button, bs.OUTPUT);

// Initialize the server on port 8888
var server = http.createServer(function (req, res) {
    // requesting files (our html file)
    var file = 'server.html';
    fs.readFile(file, function(error, content){
    res.end(content);
    });
});
server.listen(8888);

// Load socket io module
var io = require('socket.io').listen(server);

// When communication is established
io.on('connection', function (socket) {
    socket.on('led', function(data){
      console.log(data);
      // Turn on the led light
      if (data==1){
        bs.digitalWrite(led,bs.HIGH);
      }
      // Turn off the led light
      else {
        bs.digitalWrite(led,bs.LOW);
      }

      setInterval(check,10);
      function check(){
        bs.digitalRead(button, checkButton);
      }
      // Check if the button on BBB is pressed
      function checkButton(x) {
        // When the button is pressed
        if(x.value == 1){
          socket.emit('warningStatus', "Message from ground staff: Robbery In Progress, HELP!");
        }
        else{
          socket.emit('warningStatus', "Message from ground staff: All Good!");
        }
      }
    });
});

console.log("Server is running");