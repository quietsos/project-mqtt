# import paho.mqtt.client as mqtt
# import time

# broker = "192.168.1.103"
# port = 1883


# def on_log(client, userdata, levels, buf):
#     print("Log is: ",buf)

# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         client.connected_flag = True
#         print("Connected ok.")
#     else:
#         print("Bad connection return code is: ",rc)
#         client.loop_stop()

# def on_disconnect(client,userdata,rc):
#     print("Client disconnect ok")

# def on_publish(client, userdata, mid):
#     print("In on_pub callback mid is: ",mid)


# mqtt.Client.connected_flag = False
# client = mqtt.Client("Lab")
# client.on_log = on_log
# client.on_connect = on_connect
# client.on_disconnect = on_disconnect
# client.on_publish = on_publish
# try:
#     client.connect(broker,port)
#     print("Connected to the broker.")

# except:
#     print("Invalid connection.!")
#     client.loop_stop()

# client.loop_start()

# while not client.connected_flag:
#     print("In wait loop")
#     time.sleep(1)

# time.sleep(3)
# print("In main loop")
# print("Publishing")

# ret = client.publish("lab/bulb", "Test message 0",0)
# print("Publish return: ", ret)
# time.sleep(3)

# ret = client.publish("lab/bulb", "Test message 1", 1)
# print("Publish return: ", ret)
# time.sleep(3)

# ret = client.publish("lab/bulb", "Test messaage 2", 2)
# print("Publish return: ", ret)
# time.sleep(3)

# time.sleep(3)
# client.loop_start()
# client.disconnect()




# #******************Script-2****************


# import paho.mqtt.client as mqtt
# import time
# import logging


# broker = "192.168.1.103"
# port = 1883

# def on_log(lab,userdata,levels,buf):
#     print("log is : ", buf)
# def on_connect(lab,userdata,flags,rc):
#     if rc == 0:
#         lab.connected_flag = True
#         print("Connection ok...")
#     else:
#         print("Invalid connection..return code is:",rc)

# def on_disconnect(lab,userdata,rc):
#     print("Client disconnected ok....")
        
# def on_publish(lab, userdata, mid):
#     print("Callback mid is: ",mid)





# mqtt.Client.connected_flag = False
# lab = mqtt.Client("Innovative_lab")
# lab.on_log = on_log
# lab.on_connect = on_connect
# lab.on_disconnect = on_disconnect
# lab.on_publish = on_publish

# try:
#     lab.connect(broker,port)
#     print("Connected to the broker.")
# except:
#     print("Invalid connection")

# lab.loop_start()

# while not lab.connected_flag:
#     print("In wait loop")
#     time.sleep(1)
# print("In main loop")
# print("Publishing message....")

# ret = lab.publish("room-1/bulb","ON",0)
# print("publish return: ",ret)
# time.sleep(3)

# ret = lab.publish("room-1/bulb","OFF",1)
# print("publish return: ",ret)
# time.sleep(3)

# ret = lab.publish("room-1/bulb","ON",2)
# print("publish return: ", ret)
# time.sleep(3)

# lab.loop_stop()
# lab.disconnect()



# #******************Script-2****************


# import paho.mqtt.client as mqtt
# import time
# import logging


# broker = "192.168.0.104"
# port = 1883
# logging.basicConfig(level=logging.INFO)

# def on_log(lab,userdata,level,buf):
#     logging.info("log is : " + buf)
# def on_connect(lab,userdata,flags,rc):
#     if rc == 0:
#         lab.connected_flag = True
#         logging.info("Connection ok...")
#     else:
#         logging.info("Invalid connection..return code is:" + str(rc))

# def on_disconnect(lab,userdata,rc):
#     logging.info("Client disconnected ok....")
        
# def on_publish(lab, userdata, mid):
#     logging.info("Callback mid is: " + str(mid))





# mqtt.Client.connected_flag = False
# lab = mqtt.Client("Innovative_lab")
# lab.on_log = on_log
# lab.on_connect = on_connect
# lab.on_disconnect = on_disconnect
# lab.on_publish = on_publish

# try:
#     lab.connect(broker,port)
#     logging.info("Connected to the broker.")
# except:
#     logging.info("Invalid connection")

# lab.loop_start()

# while not lab.connected_flag:
#     logging.info("In wait loop")
#     time.sleep(1)
# logging.info("In main loop")
# logging.info("Publishing message....")

# ret = lab.publish("room-1/bulb","ON",0)
# logging.info("publish return: " + str(ret))
# time.sleep(3)

# ret = lab.publish("room-1/bulb","OFF",1)
# logging.info("publish return: " + str(ret))
# time.sleep(3)

# ret = lab.publish("room-1/bulb","ON",2)
# logging.info("publish return: " + str(ret))
# time.sleep(3)

# lab.loop_stop()
# lab.disconnect()


#******************Script-3****************


import paho.mqtt.client as mqtt
import time
import logging


broker = "192.168.0.104"
port = 1883
logging.basicConfig(level=logging.INFO)

def on_log(lab,userdata,level,buf):
    logging.info("log is : " + buf)
def on_connect(lab,userdata,flags,rc):
    if rc == 0:
        lab.connected_flag = True
        logging.info("Connection ok...")
    else:
        logging.info("Invalid connection..return code is:" + str(rc))

def on_disconnect(lab,userdata,rc):
    logging.info("Client disconnected ok....")
        
def on_publish(lab, userdata, mid):
    logging.info("Callback mid is: " + str(mid))

def on_subscribe(lab,userdata,mid,granted_qos):
    logging.info("Subscribed")

def on_message(lab,userdata,message):
    topic = message.topic
    msg = str(message.payload.decode("utf-8"))
    msg = "Received message: " + msg
    logging.info(str(msg))

def reset():
    ret = lab.publish("room-1/bulb","",0,True)



mqtt.Client.connected_flag = False
lab = mqtt.Client("Innovative_lab")
lab.on_log = on_log
lab.on_connect = on_connect
lab.on_disconnect = on_disconnect
lab.on_publish = on_publish
lab.on_subscribe = on_subscribe
lab.on_message = on_message

try:
    lab.connect(broker,port)
    logging.info("Connected to the broker.")
except:
    logging.info("Invalid connection")

lab.loop_start()

while not lab.connected_flag:
    logging.info("In wait loop")
    time.sleep(1)
logging.info("In main loop")
logging.info("Publishing message....")

ret = lab.publish("room-1/bulb","ON",0)
logging.info("publish return: " + str(ret))
time.sleep(3)

ret = lab.publish("room-1/bulb","OFF",1)
logging.info("publish return: " + str(ret))
time.sleep(3)

ret = lab.publish("room-1/bulb","ON",2)
logging.info("publish return: " + str(ret))
time.sleep(3)

lab.subscribe("room-1/bulb")
time.sleep(10)

reset()
lab.loop_stop()
lab.disconnect()

