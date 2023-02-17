import paho.mqtt.client as mqtt
import time
client = mqtt.Client()
client.connect(host="172.20.10.8", port=1883, keepalive=60)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("luok/ping")
    client.message_callback_add("luok/ping", on_message_from_ping)
    
def on_message_from_ping(client, userdata, message):
   print("Custom callback  - payload: "+message.payload.decode())
   payload = int(message.payload.decode())
   print("Received " + str(payload))
   payload += 1
   time.sleep(1)
   client.publish("luok/pong", f"{payload}")

client.on_connect = on_connect
client.loop_forever()




    
    
