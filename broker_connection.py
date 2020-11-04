import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flag, rc):
    if rc == 0:
        client.connected_flag = True
        print("Connected Ok",rc)

    else:
        print("Connecting.......")

def on_log(client, userdata,level, buf):
    print("log: ",buf)

def on_message(client, userdata, message):
    print("Received messge:",str(message.payload.decode("utf-8")))

mqtt.Client.connected_flag = False
broker = "localhost"
client = mqtt.Client("room-1")
client.username_pw_set(username='sohan', password='1234')
# client2 = mqtt.Client("room-2")
client.on_connect = on_connect
client.connect(broker,1883)
# try:
#     client2.connect(broker,1883)
# except:
#     print("Connection falied.")
#     exit(1)
client.on_message = on_message
client.on_log = on_log


client.loop_start()
while not client.connected_flag:
    print("In wait loop")
    time.sleep(1)

client.subscribe("room/bulb-1")
print("Subscribed.")
client.publish("room/bulb-1","ON")
print("Published.")
time.sleep(4)
client.loop_stop()
client.disconnect()