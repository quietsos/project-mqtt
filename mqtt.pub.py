# A simple example for publishing mqtt message using paho to mqttt broker

import paho.mqtt.client as paho  # importing paho mqtt clent from mqtt 
import sys


client = paho.Client()   #create client object as client from paho 

if client.connect("localhost", 1883, 60) != 0:    # connect client to the mqtt broker installed in you local machine using # ip, port,callback
    print("Could not connect to mqtt brokeer")
    sys.exit(-1)


client.publish("test/status", "hello world", 0)  # publish messge using publish function(tile,message,qos)

client.disconnect()  #after publishing message to the broker disconnect the client from broker.
