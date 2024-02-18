import json

import paho.mqtt.client as mqtt
import requests

from mqtt_app.models import Data

from .mqtt_confg import TTN_BROKER, TTN_PASSWORD, TTN_PORT, TTN_USERNAME

latest_message = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    global latest_message
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        decoded_payload = payload.get("uplink_message", {}).get("decoded_payload", {})
        message = decoded_payload.get("message")
        if message:
            print("Received message:", message)
            latest_message = message
            
            created=Data.objects.update_or_create(
                id=1,
                defaults={
                    'message': latest_message,
                    
                }
            )
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

def send_to_web():
    global latest_message
    return latest_message

client = mqtt.Client()
client.username_pw_set(TTN_USERNAME, password=TTN_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

client.connect(TTN_BROKER, TTN_PORT, 60)

client.loop_start()  
