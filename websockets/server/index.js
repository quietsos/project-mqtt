// *****************script-1************
// var server = require('ws').Server;
// var s = new server({port:5001});


// *****************script-2************

// var server = require('ws').Server;
// var s = new server({port:5001});

// s.on('connection', function(ws){
//     ws.on('message',function(message){
//         console.log("Received: " +message);
//     });
// });


// *****************script-3************

// var server = require('ws').Server;
// var s = new server({port:5001});

// s.on('connection', function(ws){
//     ws.on('message',function(message){
//         console.log("Received: " +message);

//         if(message == 'hello'){
//             ws.send("hey there from the server.")
//         };
//     });
// });


// // *****************script-4************

// var server = require('ws').Server;
// var s = new server({port:5001});

// s.on('connection', function(ws){
//     ws.on('message',function(message){
//         console.log("Received: " +message);

//         // if(message == 'hello'){
//         //     ws.send("hey there from the server.")
//         // };
//         ws.send(message);
//     });
// });



// *****************script-5************

var server = require('ws').Server;
var s = new server({port:5001});

s.on('connection', function(ws){
    ws.on('message',function(message){
        console.log("Received: " +message);
        ws.send("From server: " +message);


    });

    ws.on('close',function(){
        console.log("I lost a client");
    });

    console.log("One more client connected.");

});