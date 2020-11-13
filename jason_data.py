import paho.mqtt.client as mqtt
import time
import json

brokers_out = {
    "broker1":"192.168.0.104",
    "broker2":"test.mosquitto.org",
    "broker3":"iot.eclipse.org"
}

print(brokers_out)
print("broker out type is: ", type(brokers_out))
print("broker 1 address is: ", brokers_out["broker1"])

data_out = json.dumps(brokers_out)
print("\n Converting to JSON \n")
print("Converting data type: ",type(data_out))
print("Converiting data out: ", data_out)


print("\n Received Data \n")
data_in = data_out
print("\n Received data type is: ", type(data_in))
print("Received data is: ", data_in)

brokers_in = json.loads(data_in)
print("brokers_in data type: ", type(brokers_in))
print("\n broker 2 address: ", brokers_in["broker2"])

cont = input("Enter to continue: ")

def on_message(client,userdata,message):
    topic = message.topic
    m_decode = str(message.payload.decode("utf-8","ignore"))
    print("Received data type: ",type(m_decode))
    m_in = json.loads(m_decode)
    print("Converting json data type: ",type(m_in))
    print( "Received json message: ",m_in)
    print("topic is: ", topic)
    print("broker 1 address = ", m_in["broker1"])

topic = "test/json_test"

client = mqtt.Client("sohan")
print("Connecting to broker ", brokers_out["broker1"])
client.connect(brokers_out["broker1"])
print("Connection established")
client.on_message = on_message

client.loop_start()
client.subscribe(topic)
time.sleep(3)
print("Sending data")
client.publish(topic,data_out)
time.sleep(5)
client.loop_stop()
client.disconnect()
