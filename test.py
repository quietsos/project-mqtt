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