import paho.mqtt.client as mqtt
import time
import random

BROKER_ADDRESS = "hugo-serveur.cloudns.eu"
PORT = 1883

# Liste des pièces de la maison
rooms = ["chambre_1", "chambre_2", "sdb", "salon", "cuisine"]
outdoors = ["terrasse", "jardin"]

# Fonctions pour générer des valeurs réalistes de chaque paramètre mesuré par les capteurs
def generate_temperature(): return f"{round(random.uniform(18, 24), 1)} °C"
def generate_humidity(): return f"{round(random.uniform(40, 60), 1)} %"
def generate_movement(): return "oui" if random.random() < 0.1 else "non"
def generate_air_quality(): return f"{random.randint(0, 100)} AQI"
def generate_light(): return f"{random.randint(1000, 50000)} lux"
def generate_rain(): return f"{round(random.uniform(0, 10), 1)} mm/h"

# Dictionnaire des topics et leurs valeurs
sensors = {}
for room in rooms:
    sensors[f"maison/{room}/temperature"] = (generate_temperature, 0)
    sensors[f"maison/{room}/humidite"] = (generate_humidity, 0)
    sensors[f"maison/{room}/mouvement"] = (generate_movement, 2)
    sensors[f"maison/{room}/qualite-air"] = (generate_air_quality, 1)

for zone in outdoors:
    sensors[f"maison/{zone}/luminosite"] = (generate_light, 0)
    sensors[f"maison/{zone}/humidite"] = (generate_humidity, 0)

sensors["maison/pluie"] = (generate_rain, 1)

# Connexion au broker MQTT
client = mqtt.Client()
client.connect(BROKER_ADDRESS, PORT, 60)
client.loop_start()  # Permet de gérer la communication MQTT en arrière-plan

try:
    while True:
        for topic, (value_function, qos) in sensors.items():
            message = value_function()
            client.publish(topic, payload=message, qos=qos)
            print(f"Publié: {topic} -> {message} (QoS {qos})")
        time.sleep(10)
except KeyboardInterrupt:
    print("Arrêt de la simulation MQTT")
    client.loop_stop()
    client.disconnect()


