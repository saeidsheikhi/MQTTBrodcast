import paho.mqtt.client as mqtt
import random
import time

# MQTT Broker configuration
broker_address = ""  # You can use a different broker
port = 1883
topic_heart_rate = "smartwatch/heart_rate2"
topic_blood_pressure = "smartwatch/blood_pressure2"

# Create an MQTT client
client = mqtt.Client("SmartWatchClient")
username = "admin"  # Replace with your actual MQTT username
password = ""  # Replace with your actual MQTT password
client.username_pw_set(username, password)

# Connect to the MQTT broker
client.connect(broker_address, port)

def publish_data():
    while True:
        # Simulate heart rate and blood pressure data
        heart_rate = random.randint(60, 100)
        systolic_bp = random.randint(100, 140)
        diastolic_bp = random.randint(60, 90)

        # Publish heart rate data
        client.publish(topic_heart_rate, f"Heart Rate: {heart_rate} bpm")

        # Publish blood pressure data
        client.publish(topic_blood_pressure, f"Blood Pressure: {systolic_bp}/{diastolic_bp} mmHg")

        print(f"Published: Heart Rate={heart_rate} bpm, Blood Pressure={systolic_bp}/{diastolic_bp} mmHg")

        # Wait for a few seconds before publishing the next data
        time.sleep(5)

if __name__ == "__main__":
    try:
        client.loop_start()
        publish_data()
    except KeyboardInterrupt:
        print("Smartwatch simulation stopped.")
        client.loop_stop()
        client.disconnect()
