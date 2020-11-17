import paho.mqtt.client as mqtt
import sys
import time
import logging

broker = "192.168.0.104"
port = 1883
logging.basicConfig(level=logging.INFO)


def on_log(sohan,userdata,level,buf):
    logging.info("Log is: " + str(buf))

def on_connect(sohan,userdata,flags, rc):
    if rc == 0:
        sohan.connected_flag = True
        logging.info("Connected Ok")
    else:
        logging.info("Bad connection return code is: " + str(rc))
        sohan.loop_stop()
        sys.exit()

def on_disconnect(sohan,userdata,rc):
    logging.info("Client disconnection ok....")


def on_publish(sohan, userdata, mid):
    logging.info("Callback mid is: " + str(mid))

def on_subscribe(sohan,userdata, mid, granted_qos):
    logging.info("Subscribed")
    

def on_message(sohan,userdata,message):
    print("Received message is: ",str(message.payload.decode("utf-8")))



mqtt.Client.connected_flag = False

sohan = mqtt.Client("my-office")
sohan.on_log = on_log
sohan.on_connect = on_connect
sohan.on_disconnect = on_disconnect
sohan.on_publish = on_publish
sohan.on_subscribe = on_subscribe
sohan.on_message = on_message
sohan.username_pw_set(username="sohan", password="1234")

topics = [("room/light/bulb1",0), ("room/light/bulb2",1)]

topic_ack = []

print("Connecting to the broker...")

try:
    sohan.connect(broker,port)
    print("Connection established")

except:
    print("Cannot connect...")
    sys.exit(1)

sohan.loop_start()

while not sohan.connected_flag:
    print("In wait loop")
    time.sleep(1)

print("In main loop.")

print("Subscribing : ", str(topics))

for t in topics:
    try:
        r = sohan.subscribe(t)

        if r[0] == 0:
            logging.info("Subscribe to topic: " + str(t[0]) + " & return code: " + str(r))
            topic_ack.append(t[0], r[1],0)
        else:
            logging.info("Error on subscribing: " + str(r))
            sohan.loop_stop()
            sys.exit(1)
    except Exception as e:
        print("out")


print("Waitting for all subscribtion.")
# while not check_subs():
#     time.sleep(1)

msg = "OFF"

print("Publishing topic = ", topics[0][0], "Message is = ", msg)

sohan.publish(topics[0][0],msg)




time.sleep(4)
sohan.loop_stop()
sohan.disconnect()