import paho.mqtt.client as mqtt
import time

BROKER = "hugo-serveur.cloudns.eu"
PORT = 1883
TOPIC = "test/topic"
QOS = 0  # 0, 1 ou 2
MESSAGE = "Hello, MQTT!"

def on_connect(client, userdata, flags, rc):
    """
    Callback function for when the client receives a CONNACK response from the MQTT broker.

    Parameters:
    client (paho.mqtt.client.Client): The client instance for this callback.
    userdata (any): The private user data as set in Client() or userdata_set().
    flags (dict): Response flags sent by the broker.
    rc (int): The connection result.

    Behavior:
    - If the connection is successful (rc == 0), it prints a success message, subscribes to the specified topic, and prints the subscription details.
    - If the connection fails, it prints an error message with the return code.
    """
    if rc == 0:
        print("----- Connexion réussie au broker MQTT -----")
        client.subscribe(TOPIC, qos=QOS)  # S'abonner au topic
        print(f"----- Abonné au topic : {TOPIC} avec QoS {QOS} -----")
    else:
        print(f"----- Échec de la connexion, code de retour : {rc} -----")



def on_message(client, userdata, message):
    """
    Callback function that is triggered when a message is received from the MQTT broker.

    Args:
        client (paho.mqtt.client.Client): The client instance for this callback.
        userdata (any): The private user data as set in Client() or userdata_set().
        message (paho.mqtt.client.MQTTMessage): An instance of MQTTMessage, which contains the topic, payload, qos, etc.

    Prints:
        The topic, payload, and QoS of the received message.
    """
    print(f"\n----- Nouveau message reçu ! -----")
    print(f"Id : {message.mid}")
    print(f"Topic : {message.topic}")
    print(f"Payload : {message.payload.decode()}")
    print(f"QoS : {message.qos}")



# Créer une instance de client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


# On se connecte au broker
print(f"----- Connexion au broker {BROKER}:{PORT}... -----")
client.connect(BROKER, PORT, 60)
client.loop_start()

time.sleep(2)


# On publie un message sur le topic spécifié
print(f"----- Publication du message : {MESSAGE} -----")
client.publish(TOPIC, MESSAGE, qos=QOS, retain=False, properties=None)


# On écoute les messages reçus pendant 10 secondes
time.sleep(10)


# On se déconnecte du broker
client.loop_stop()
client.disconnect()
print("----- Déconnecté du broker. -----")
