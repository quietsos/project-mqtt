var myserver = require('ws').Server;
var s = new myserver({port:5001});


s.on('connection', function(ws){
    ws.on('message',function(message){
        
        message = JSON.parse(message);

        if(message.type == 'name'){
            ws.personName = message.data;
            return;
        }

        // console.log("Received: " + message);

        s.clients.forEach(function e(client){
            if(client != ws)
                client.send(JSON.stringify({
                    name : ws.personName,
                    data: message.data
                }));
        });
         
        //  ws.send("Server send: " + message)
    });

    ws.on('close',function(){
        console.log("I lost a client");

    });

    console.log("One more client connected.");
     
});