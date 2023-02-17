import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("luok/pong")
    client.message_callback_add("luok/pong", on_message_from_pong)
    payload = 0
    client.publish("luok/ping", f"{payload}")
    
def on_message_from_pong(client, userdata, message):
   print("Custom callback  - payload: "+message.payload.decode())
   payload = int(message.payload.decode())
   print("Received " + str(payload))
   payload += 1
   time.sleep(1)
   client.publish("luok/ping", f"{payload}")
   

   
client = mqtt.Client()
client.on_connect = on_connect
client.connect(host="172.20.10.8", port=1883, keepalive=60)
client.loop_forever()
