import paho.mqtt.client as mqtt
import time

BROKER_ADDRESS = "hugo-serveur.cloudns.eu"
PORT = 1883
KEEP_ALIVE_INTERVAL = 10


# Callback lors de la connexion au broker
def on_connect(client, userdata, flags, rc):
    print(f"Connecté au broker avec un keep-alive de {KEEP_ALIVE_INTERVAL} secondes")


# Connexion au broker MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER_ADDRESS, PORT, KEEP_ALIVE_INTERVAL)

# client.subscribe("test/topic")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nArrêt de l'écoute des messages.")
    client.disconnect()
