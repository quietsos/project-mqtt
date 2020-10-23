# An example for mqtt paho subscriber

import paho.mqtt.client as paho  # imporing paho from mqtt
import sys


def onMessage(client, userdata, msg):
    print(msg.topic + ":" + msg.payload.decode())  # createing a function for calling data from broker and show in display

client = paho.Client()      #creating paho client
client.on_message = onMessage  #calling function for message from brokeer

if client.connect("localhost", 1883, 60) != 0:
    print("Couldnot connect to Mqtt broker")     #connecting to the brokeer
    sys.exit(-1)

client.subscribe("test/status")   #subscribing to the topic

try:
    print("Press CTRL+C to exit......")
    client.loop_forever()
except:
    print("Disconnecting from broker")

client.disconnect()
