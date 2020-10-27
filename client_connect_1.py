import paho.mqtt.client as mqtt
import paho.mqtt.client as paho
import time

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected OK")
	else:
		print("Bad connection  return code = ", rc)
broker = "localhost"

client = mqtt.Client()
client.on_connect = on_connect
print("Connecting to broker")
client.loop_start()
client.publish("house/bulb","ON")
time.sleep(4)
client.loop_stop()
client.disconnect()
