# 🌱 Pre-Internship IoT Automation Project — BEIA Consult International

This repository documents a pre-internship project developed for **BEIA Consult International**, focused on IoT, data transmission, blockchain storage, service orchestration, and data visualization.

## 🔧 Project Objectives

- Connect an IoT device to an MQTT broker  
- Store data both locally and on the cloud  
- Secure data using blockchain (Ethereum)  
- Orchestrate services via Arrowhead using Docker  
- Visualize data with Grafana  
- Enable data processing with Node-RED  
- Allow queries via chatbot/voicebot  

---

## 📡 Technologies & Tools Used

- **Python** – Data simulation & MQTT publishing  
- **Libelium** – Real sensor data acquisition  
- **MQTT** – Lightweight communication protocol  
- **Node-RED** – Data processing & routing  
- **InfluxDB** – Time-series database  
- **Grafana** – Monitoring & visualization  
- **Ethereum Blockchain** – Secure data storage  
- **Telegram Bot** – Data query interface  
- **Docker** – Containerized service orchestration with Arrowhead  

---

## 🛠 Project Structure

```bash
pre-practica-project/
│
├── scripts/                     # Python scripts for MQTT, blockchain, bots
│   ├── mqtt_random.py
│   ├── mqtt_waspmote.py
│   ├── send_to_blockchain.py
│   └── darius_bot.py
│
├── screenshots/                # Visual documentation (.png files)
│
├── README.md
├── LICENSE
└── .gitignore
