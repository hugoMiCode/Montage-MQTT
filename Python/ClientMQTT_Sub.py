import paho.mqtt.client as mqtt
import time

BROKER_ADDRESS = "hugo-serveur.cloudns.eu"
PORT = 1883
# TOPIC = "maison/+/temperature"
TOPIC = "test/1"
QOS = 2


# Callback lors de la réception d'un message
def on_message(client, userdata, msg):
    print(f"Message reçu : {msg.topic} -> {msg.payload.decode()}")


client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER_ADDRESS, PORT, 60)


# Souscription au topic
print(f"\nSouscription au topic : {TOPIC} avec QoS {QOS}")
client.subscribe(TOPIC, qos=QOS)


# On écoute les messages
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nArrêt de l'écoute des messages.")
    client.disconnect()
