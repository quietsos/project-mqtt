# import paho.mqtt.client as mqtt #import the client
# import time

# def on_connect(client,userdata,flags,rc):
#     if rc == 0:
#         print("Connected ok.",rc)
#     else:
#         print("Bad connection...",rc)

# broker = "192.168.0.104"

# client = mqtt.Client("Room-1") # creating new client instance
# client.on_connect = on_connect #callback function for checking the is stublished or not
# client.connect(broker)  # connect client to the broker
# print("Connecting to the broker: ", broker)


# client.loop_start() # start loop
# client.subscribe("house/light") # subscribe to published topic
# client.publish("house/light","ON") # published topic and message to the broker
# time.sleep(4) #time delay of start loop
# client.loop_stop() # stop loop
# client.disconnect() #disconnect client from the broker connection

# **************2nd script:***********

# import paho.mqtt.client as mqtt
# import time

# def on_connect(client,userdata,flag,rc):
#     if rc == 0:
#         client.connected_flag = True
#         print("Connected Ok")
#     else:
#         print("Bad connection return code is:",rc)

# mqtt.Client.connected_flag = False

# broker = "192.168.0.104"
# client = mqtt.Client("room-2")
# client.on_connect = on_connect
# print("Connecting to broker: ",broker)
# client.connect(broker)

# client.loop_start()


# while not client.connected_flag:
#     print("In wait loop")
#     time.sleep(1)


# print("In main loop")
# client.subscribe("room2/light")
# client.publish("room2/light","ON")

# time.sleep(4)
# client.loop_stop()
# client.disconnect()


# **************3rd script*************

# import paho.mqtt.client as mqtt
# import time

# def on_connect(client, userdata,flag,rc):
#     if rc == 0:
#         client.connected_flag = True
#         print("Connected ok",rc)
#     else:
#         print("Bad connection return code is:",rc)
#         client.loop_stop()

# def on_message(client,userdata, message):
#     print("Published message is: ", str(message.payload.decode()))

# mqtt.Client.connected_flag = False
# broker = "192.168.1.103"
# client = mqtt.Client("room-3")
# client.on_connect = on_connect
# client.on_message = on_message
# print("Connecting to broker: ",broker)

# try:
#     client.connect(broker)
# except:
#     print("Cannot connect to the broker")

# client.loop_start()
# while not client.connected_flag:
#     print("In wait loop")
#     time.sleep(1)
# print("In main loop")
# client.subscribe("room-3/light")
# client.publish("room-3/light","OFF")
# time.sleep(4)
# client.loop_stop()
# client.disconnect()

#***********script-4***********

import paho.mqtt.client as mqtt
import time,sys

def on_log(client, userdata, level, buf):
    print("Log is :", buf)

def on_connect(client,userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("Connected ok")

    else:
        print("Bad connection return code is: ",rc)

def on_disconnect(client, userdata, flags, rc =0):
    print("Disconnecting flags" + " result code"+ str(rc)+"client_id")
    client.disconnect_flag = False


def on_message(client, userdata, message):
    print("Publshed message is: ", str(message.payload.decoode()))

mqtt.Client.connected_flag = False
broker = "192.168.0.104"
port = 1883
client = mqtt.Client("Room-4")
client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
print("Connecting to the broker: ", broker)

client.loop_start()
try:
    client.connect(broker,port)
    while not client.connected_flag:
        print("In wait loop")
        time.sleep(1)
except:
    print("Connection failed.")
    sys.exit("Quitting......")

run_flag = True
count = 1
while run_flag:
    print("In main loop")
    msg = "test message"+ str(count)
    ret = client.publish("house/2","test message",0)
    print("publish",ret)
    count += 1
    time.sleep(4)

client.loop_stop()
client.disconnect()


