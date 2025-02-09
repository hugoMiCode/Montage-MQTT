import paho.mqtt.client as mqtt

BROKER_ADDRESS = "hugo-serveur.cloudns.eu"
PORT = 1883
TOPIC = "test/1"  # Définir ici le topic souhaité
QOS = 2
KEEP_ALIVE_INTERVAL = 60
RETAIN = False

# Connexion au broker MQTT
client = mqtt.Client()
client.connect(BROKER_ADDRESS, PORT, KEEP_ALIVE_INTERVAL)

client.loop_start()

print(f"\nEnvoi de messages sur le topic : {TOPIC}")
print("Tapez un message et appuyez sur Entrée pour l'envoyer (Ctrl+C pour quitter)\n")

# Boucle de saisie et d'envoi des messages
try:
    while True:
        message = input("> ")
        client.publish(TOPIC, message, qos=QOS, retain=RETAIN)
        print(f"Message envoyé : {message} (QoS {QOS}) avec retain={RETAIN}")
except KeyboardInterrupt:
    print("\nArrêt de l'éditeur de messages.")

client.disconnect()
