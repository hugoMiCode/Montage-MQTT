import paho.mqtt.client as mqtt

# ce script permet de mettre en evidence la connexion sécurisée avec TLS


client = mqtt.Client()
client.tls_set(ca_certs="C:/Users/Hugo/Repositories/ENS/Montage MQTT/Python/mosquitto.crt")
# client.tls_set(ca_certs="mosquitto.crt")
client.connect("hugo-serveur.cloudns.eu", 8883)
client.loop_start()
client.publish("test/topic", "Message sécurisé via TLS", qos=1)
client.loop_stop()
client.disconnect()
