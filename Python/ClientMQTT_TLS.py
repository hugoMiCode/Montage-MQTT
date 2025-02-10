import paho.mqtt.client as mqtt

# Ce script permet de publier un message sur le topic "test/topic" du broker MQTT "hugo-serveur.cloudns.eu" en utilisant le protocole TLS.

client = mqtt.Client()
client.tls_set(ca_certs="Python/mosquitto.crt")
client.connect("hugo-serveur.cloudns.eu", 8883)
client.loop_start()
client.publish("test/topic", "Message sécurisé via TLS", qos=1)
client.loop_stop()
client.disconnect()
