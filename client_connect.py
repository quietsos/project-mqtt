import paho.mqtt.client as mqtt #import the client
import time

def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("Connected ok.",rc)
    else:
        print("Bad connection...",rc)

broker = "192.168.0.104"

client = mqtt.Client("Room-1") # creating new client instance
client.on_connect = on_connect #callback function for checking the is stublished or not
client.connect(broker)  # connect client to the broker
print("Connecting to the broker: ", broker)


client.loop_start() # start loop
client.subscribe("house/light") # subscribe to published topic
client.publish("house/light","ON") # published topic and message to the broker
time.sleep(4) #time delay of start loop
client.loop_stop() # stop loop
client.disconnect() #disconnect client from the broker connection