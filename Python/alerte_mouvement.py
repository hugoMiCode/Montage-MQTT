import paho.mqtt.client as mqtt
import time

BROKER_ADDRESS = "hugo-serveur.cloudns.eu"
PORT = 1883
ALERT_TOPIC = "maison/alerte"  # Topic pour les alertes
MOTION_SENSOR_TOPIC = "maison/+/mouvement"  # Topic pour détecter les mouvements dans toutes les pièces

# Callback lors de la réception d'un message
def on_message(client, userdata, msg):
    # Si un mouvement est détecté
    if msg.payload.decode() == "oui":
        print(f"Mouvement détecté dans {msg.topic.split('/')[1]}!")  # Extraire le nom de la pièce
        send_alert(msg.topic.split('/')[1])  # Appeler la fonction pour envoyer une alerte

# Fonction pour envoyer une alerte
def send_alert(room_name):
    alert_message = f"Alerte : Mouvement détecté dans la pièce {room_name}!"
    client.publish(ALERT_TOPIC, alert_message)  # Publier sur le topic des alertes
    print(f"Alerte envoyée : {alert_message}")

# Callback de connexion
def on_connect(client, userdata, flags, rc):
    print(f"Connecté au broker avec le code de réponse : {rc}")
    # Souscrire au topic de mouvement (toutes les pièces)
    client.subscribe(MOTION_SENSOR_TOPIC)

# Créer un client MQTT
client = mqtt.Client()

# Configurer les callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connexion au broker
client.connect(BROKER_ADDRESS, PORT, 60)

# Démarrer la boucle client
client.loop_forever()
