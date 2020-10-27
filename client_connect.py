import paho.mqtt.client as mqtt
import paho.mqtt.client as paho
import time

def on_message(client, userdata, message):
    print("Message received= ",str(message.payload.decode("utf-8")))
    print("Message topic= ",message.topic)
    print("Message qos= ", message.qos)
    


broker = "localhost" #select broker define

client = paho.Client(client_id = "1", clean_session=True)  # connect to the broker

client.on_message = on_message #callback on_message function fo retain message from the broker

# client.connect(broker,1883, 60)

if client.connect(broker,1883,60) == 0: #connecting to the broker
    print("Connected... to:", broker)
else:
    print("Connection problem!")

client.loop_start()     # start the loop
client.subscribe("house/bulb") # subscribe a topic
client.publish("house/bulb", input("Enter publish message: "),1) # pblish a topic with a message
time.sleep(4)  # wait 
client.loop_stop() #stop loop



