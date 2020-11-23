# Websocket:
#     Websocket is a communication protocol, providing full-duplex-communication
#     channel over a single TCP connection

#    *It's closely associated with http as it used http for the inital connection
#    *The client and server negotiate a connection upgrade to Websockets
#    and the connection switches from http to websockets.

# Why websockets:
    # 1. Websockets allow you to receive MQTT data directly into a web browser.
    # 2. This is impportant as the web browser may become the de-facto interface for displaying MQTT data.
    # 3. MQTT websocket support for web browsers is provided by the javascript.



# MQTT over Websockets vs MQTT:
#  1.In this case of MQTT  over websockets the websockets connection
#  forms an outer pipe for the MQTT protocol.
#  2. The server/broker places the MQTT packet into a websockets packet
#  and sent it to the client/server.
#  3. The client/server unpacks the MQTT packet from the websockets packet
#  and then process it as a normal MQTT packet.

#*****************websocket************

# Websocket javascript MQTT client runs in a web Browser and as part of w web page.



import paho.mqtt.client as mqtt
import paho.mqtt.client as paho
import time

broker = "192.168.0.104"
port = 9001

topic = "lab/room"

def on_connect(sohan,userdata,flag,rc):
    if rc == 0:
        print("Connection ok...")
    else:
        print("Connection problem")

def on_subscribe(sohan,userdata,mid,granted_qos):
    print("Subscribed with qos", granted_qos,"\n")
    pass

def on_publish(sohan,userdata,mid):
    print("Data published mid = ",mid, "\n")
    pass

def on_message(sohan,userdata,message):
    print("Received message :",str(message.payload.decode()))

def on_disconnect(sohan,userdata,rc):
    print("client disconneted ok....")

sohan = paho.Client("Lab", transport="websockets")
sohan.on_connect = on_connect
sohan.on_subscribe = on_subscribe
sohan.on_publish = on_publish
sohan.on_message = on_message
sohan.username_pw_set(username="sohan",password="1234")
sohan.on_disconnect = on_disconnect

print("Connecting to the broker:",broker,"on port:",port)
sohan.connect(broker,port)

for i in range(5):

    sohan.loop_start()
    print("Subscribing to : ",topic)
    sohan.subscribe(topic)
    time.sleep(4)
    print("Publishing to :", topic)
    sohan.publish(topic,"ON",1)
    time.sleep(4)
    sohan.loop_stop()

sohan.disconnect()





