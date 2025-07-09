#!/usr/bin/env python3
"""
mqtt_waspmote.py
----------------
Listens to a Libelium / Waspmote MQTT topic, saves the latest payload
to `latest_data.json`, and prints the data to the console.

‣ Edit BROKER, PORT, and TOPIC to match your setup.
‣ Run with:  python mqtt_waspmote.py
"""

import json
import os
import sys
import time
import paho.mqtt.client as mqtt

# === CONFIGURATION ==========================================================
BROKER = "mqtt.beia-telemetrie.ro"
PORT = 1883                        # default MQTT port
TOPIC = "training/device/darius-vasile"
OUTFILE = "latest_data.json"         # File read by Telegram bot
# ============================================================================

def on_connect(client, userdata, flags, rc):
    """Callback when the client connects to the broker."""
    if rc == 0:
        print(f"✅ Connected to MQTT broker ({BROKER}:{PORT})")
        client.subscribe(TOPIC)
        print(f"🔔 Subscribed to topic: {TOPIC}")
    else:
        print(f"❌ Connection error. RC = {rc}")
        sys.exit(1)

def on_message(client, userdata, msg):
    """Callback when a PUBLISH message is received from the broker."""
    try:
        payload_str = msg.payload.decode()
        print(f"\n📥 Message received @ {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Topic : {msg.topic}")
        print(f"Payload: {payload_str}")

        # ➕ Added line here:
        print("📦 New message received:", payload_str)

        # Attempt to parse JSON; Libelium’s Meshlium usually sends proper JSON
        data = json.loads(payload_str)

        # OPTIONAL: inject a source tag
        data["source"] = "waspmote"

        # Write to disk atomically
        tmp_file = OUTFILE + ".tmp"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp_file, OUTFILE)
        print(f"💾 Saved to {OUTFILE}")

    except json.JSONDecodeError:
        print("⚠️  Payload is not valid JSON. Ignored.")
    except Exception as e:
        print(f"⚠️  Unexpected error: {e}")

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(BROKER, PORT, 60)
    except Exception as exc:
        print(f"❌ Could not connect to broker: {exc}")
        sys.exit(1)

    # Blocking loop – press Ctrl-C to stop
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")
        client.disconnect()

if __name__ == "__main__":
    main()
