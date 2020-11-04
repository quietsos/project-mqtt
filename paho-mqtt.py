# Paho-mqtt client....we will discuss here 
#     1. installing paho-mqtt
#         += The python mqtt client 
#     2. importing client class 
#     3. creating client instance
#     4. connecting to the broker or server
#     5. publishing message
#     6. subscribing message


# paho-mqtt is a python libray for handling mqtt broker like mosquitto and many other's'

1. Installing paho-mqtt client

    # you can install the MQTT-paho client using pip with the command:-

pip install paho-mqtt # you should define pip version if you want to install paho-mqtt globally as pip3/pip3.4

pip --version # to check the version of installed pip in your machine

        # += The python mqtt client:
        #         The core of the client libray is the client class which provides all the functions to publish message and topic message to topics.

Main client methonds are:
    1. connec() and disconnect()
    2. subscribe() and unsubscribe()
    3. publish() 

# Each of these methods is associated with a callback.

2. Importing The client class:

Import paho.mqtt.client as mqtt


3. Creating a client instance:
    #     The client constructor takes 4 optional parameters but only the client_id is necessary and this should be unique.

Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")

client = mqtt.Client(client_name) 

4. Connecting to the Broker or Server:

    # For publishing and subscribing message firstly we need to connect to the broker.
    # To do this  we use the connect method of the python mqtt

connect(host, port=" ", keepalive= 60, bind_address=" ")

# general syntax:

client.connect(host_name)



5. publishing Messages:

# Once you have establish a connection you can start to publish message by following below steps:

publish(topic, payload=None, qos = 0, retain =False)

# Note: topic and payload parameter must supply, here payload is the message which i want to publish.

client.publish("BigHouse/light", "ON")




Demo python script for publishing a message:

import paho.mqtt.client as mqtt
broker = "localhost"
client = mqtt.Client("p1")
client.connect(broker)
client.publish("bighouse/light", "ON")


6. subscribe to a topic:

# To subscribe a topic we use the subscribe method of python paho class object.
    The subscribe method accepts 2 parametes 1.topic client_name
                                             2. QoS(quality of service)
                                                1. QoS - 1
                                                2. QoS - 2
                                                3. QoS - 3
                                            

subscribe("bighouse/light",0)                                            

# Python script of subscribe and publishing message:

import paho.mqtt.client as mqtt
broker = "localhost"
print("Defining the host as: ",broker) 
client = mqtt.Client("p1")
print("Creating client instant.")
client.connect(broker)
print("Connected to the broker.")
client.publish("bighouse/light", "ON")
print("Publishing on topic:","bighouse/light")
client.subscribe("bighouse/light", 0) 
print("Subscribing on topic: ", "bighouse/light")

output:
    Defining the host as:  localhost
    Creating client instant.
    Connected to the broker.
    Publishing on topic: bighouse/light
    Subscribing on topic:  bighouse/light

    # Note: Our published message is missing in this output. 
    # For retain message we need to call a functin #on_message()


To process callback we need:
    # 1. Creating callback functions to process any message
    # 2. Start and stop a loop for checking callback message


on_message callback function define:

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode(uft-8))) # retaining message from broker using callback function
    print("Message topic: ", message.topic) #printing message topic in which our message publish
    print("Message QoS: ", message.qos) #printing quality service of published message
    print("Message retain flag: ", message.retain) # printing the message retain flag of the published message


# Final script of publishing and receiveing message in paho-mqtt:

import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    print("Message qos: ", message.qos)
    print("Message topic: ", message.topic)

broker = "localhost"
client = mqtt.Client("client-1")
print("Creating client instance")

client.connect(broker)
print("Connected to the broker")
client.on_message = on_message

client.loop_start()
client.subscribe("home/bulb")
print("Subscribing topic")
# client.publish("home/bulb","ON")
client.publish("home/bulb", input("Enter publish message: "))
print("Publishing topic message")

time.sleep(4)
client.loop_stop()


# Troubleshoot using looging:

usig log function we cal see the details connection, publish and subscribe message.

def on_log(client, userdata, level, buf):
    print("log: ",buf)


client.on_log = on_log


# python script:

import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    print("Message qos: ", message.qos)
    print("Message topic: ", message.topic)

def on_log(client, userdata, level, buf):
    print("log: ",buf)


broker = "localhost"
client = mqtt.Client("client-1")
print("Creating client instance")

client.connect(broker)
print("Connected to the broker")
client.on_message = on_message
client.on_log = on_log

client.loop_start()
client.subscribe("home/bulb")
print("Subscribing topic")
# client.publish("home/bulb","ON")
client.publish("home/bulb", input("Enter publish message: "))
print("Publishing topic message")

time.sleep(4)
client.loop_stop()



# Paho-mqtt python client objects:

    The main component of the paho python mqtt client library is the #client class
    The client class provide all the necessary function to connect to an mqtt broker, publish  message, subscribe message to topics and receive Messages

# To use you will need to create a new client object from the client class 

Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")

# client object creating:
import paho.mqtt.client as mqtt

broker = "localhost"
sohan = mqtt.Client(client_id="1", clean_session=True, userdata=None, transport="tcp")

sohan.connect(broker)