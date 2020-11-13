# import paho.mqtt.client as mqtt
# import time

# def on_message(client, userdata, message):
#     print("Received message: ", str(message.payload.decode("utf-8")))
#     print("Message qos: ", message.qos)
#     print("Message topic: ", message.topic)

# def on_log(client, userdata, level, buf):
#     print("log: ",buf)


# broker = "localhost"
# client = mqtt.Client("client-1")
# print("Creating client instance")

# client.connect(broker)
# print("Connected to the broker")
# client.on_message = on_message
# client.on_log = on_log

# client.loop_start()
# client.subscribe("home/bulb")
# print("Subscribing topic")
# # client.publish("home/bulb","ON")
# client.publish("home/bulb", input("Enter publish message: "))
# print("Publishing topic message")

# time.sleep(4)
# client.loop_stop()

#*****************script -2 *****************


import paho.mqtt.client as mqtt  #import the client1
import time
import logging,sys
keepalive=1200
port=1883
r_messages=[]
logging.basicConfig(level=logging.DEBUG)
#use DEBUG,INFO,WARNING
def on_disconnect(client, userdata, flags, rc=0):
    m="DisConnected flags"+"result code "+str(rc)+"client1_id  "+str(client)
    print(m)

def on_connect(client, userdata, flags, rc):
    m="Connected flags"+str(flags)+"result code "+str(rc)+"client1_id  "+str(client)
    print(m)

def on_message(client1, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    logging.info("message received  " +msg +" topic="+ message.topic)
    r_messages.append(msg)

def pub(client,topic,msg,qos,p_msg):
    logging.info(p_msg + msg+ "  topic= "+topic +" qos="+str(qos))
    client.publish(topic,msg,qos)
def sub(client,topic,qos,s_msg):
    logging.info(s_msg+"  topic= "+topic +" qos="+str(qos))
    client.subscribe(topic,qos)   

qos_s=0
qos_p=0
QOS1=1
QOS2=1


broker="192.168.1.65"
#broker="iot.eclipse.org"
topic1="house/bulbs/bulb1"
topic2="house/bulbs/bulb2"

print("Clear before start")
CLEAN_SESSION=True
client1 = mqtt.Client("Python1",clean_session=CLEAN_SESSION)
client1.connect(broker,port,keepalive)      #connect to broker
client1.disconnect()
print("End Clear before start")
CLEAN_SESSION=True
print ("client1 is used to subscribe and client 2 to publish")
print ("Test1: Test if broker remembers subcription with non clean session ")
print ("Test1: Test that Messages with QOS of 0 are not stored for client ")
client1 = mqtt.Client("Python1",clean_session=CLEAN_SESSION)    #create new instance
client2 = mqtt.Client("Python2")    #create new instance 
client1.on_message=on_message        #attach function to callback
print("Connecting client 1 with clean session set to ",CLEAN_SESSION)
client1.connect(broker,port,keepalive)      #connect to broker
client2.connect(broker,port,keepalive)      #connect to broker
client1.loop_start()
msg1="message0"

sub(client1,topic1,qos_s,"client1 subscribed")

time.sleep(3)

pub(client2,topic1,msg1,qos_p,"published message ")

time.sleep(2)
inp=input("Waiting to continue:")
print("disconnecting client1")
client1.disconnect()
logging.info("client1 disconected ")
print("connecting client1 but not subscribing")
client1.connect(broker,port,keepalive)      #connect to broker
pub(client2,topic1,msg1,qos_p,"published message ")
inp=input("Waiting to continue:")

CLEAN_SESSION=False

print("Connecting client 1 with clean session set to ",CLEAN_SESSION)
client1 = mqtt.Client("Python1",clean_session=CLEAN_SESSION)    #create new instance

client1.on_message=on_message        #attach function to callback
client1.connect(broker,port,keepalive)      #connect to broker
client1.loop_start()
msg1="message1"

sub(client1,topic1,qos_s,"client1 subscribed")

time.sleep(3)

pub(client2,topic1,msg1,qos_p,"published message ")

time.sleep(2)
inp=input("Waiting to continue:")
print("disconnecting client1")
client1.disconnect()
logging.info("client1 disconected ")
msg2="message2"
pub(client2,topic1,msg2,qos_p,"client2 publishing while client1 disconnected ")
client1.loop_stop()
time.sleep(2)
print ("client1 reconnected but not subscribing ")
client1.connect(broker,port,keepalive)   #connect to broker
inp=input("Waiting to continue:")

client1.loop_start()
msg3="message3"
pub(client2,topic1,msg3,qos_p,"published message msg3 ")

time.sleep(2)
print("expecting to receive messages 1 and 3 but not message 2")
count=0
for m in r_messages:
    if m==msg1:
        count+=1
    if m==msg3:
        count+=3
    if m==msg2:
        count -=2
#print ("count= ",count)
if count==4:
    print("Test1 Passed")
inp=input("Waiting to continue:")
print ("Test2: Now test if broker stores messages with qos 1 \
and above for disconnected client first subscribe with qos of \
1 to new topic ",topic2)
inp=input("Waiting to continue:")
qos_s=1
qos_p=1
sub(client1,topic2,qos_s,"Subscribed to")
time.sleep(2)
print("disonnecting client1")
client1.disconnect()
logging.info("client1 disconected")
client1.loop_stop()
r_messages=[] ##clear message store
msg4="message4"
pub(client2,topic2,msg4,qos_p,"publish msg4 while client1 disconnected ")
time.sleep(2)
client1.connect(broker,port,keepalive)   #connect to broker
inp=input("Waiting to continue:")
print ("client1 reconnected but not subscribing to topics")
client1.loop_start()
time.sleep(10)
for m in r_messages:
    if m==msg4:

        
        print("Message Msg4 Received-Test2 Passed")
    else:
        print("Message Msg4 Not Received-Test2 Failed")
        
print("ending")
client1.loop_stop()



