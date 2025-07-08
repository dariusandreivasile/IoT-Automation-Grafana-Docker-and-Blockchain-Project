import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = "mqtt.beia-telemetrie.ro"
PORT = 1883
TOPIC = "training/device/darius-vasile/data-in"

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.connect(BROKER, PORT, 60)

def generate_data():
    data = {
        "device": "libelium-station-01",
        "temperature": round(random.uniform(20.0, 40.0), 2),      # °C
        "humidity": round(random.uniform(30.0, 80.0), 2),         # %
        "solar_radiation": round(random.uniform(200, 1000), 1),   # W/m2
        "precipitation": round(random.uniform(0, 10), 2),         # mm
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    return data


try:
    while True:
        sensor_data = generate_data()
        payload = json.dumps(sensor_data)
        client.publish(TOPIC, payload)
        print(f"Published to {TOPIC}: {payload}")

        # Salvare locală
        with open("latest_data.json", "w") as f:
            f.write(payload)

        time.sleep(60)

except KeyboardInterrupt:
    print("Stopped by user.")
    client.disconnect()
