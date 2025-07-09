# Pre-Internship IoT Automation Project — BEIA Consult International

This repository documents a pre-internship project developed for **BEIA Consult International**, focused on IoT, data transmission, blockchain storage, service orchestration, and data visualization.

## Project Objectives

- the integration of an IoT device with MQTT communication;
- local and cloud storage;
- blockchain security;
- orchestration of Arrowhead services using Docker;
- data visualization using Grafana;
- data processing using Node-Red;
- Waspmote configuration;
 

---

## Technologies & Tools Used

- **Python** – Data simulation & MQTT publishing  
- **Libelium** – Real sensor data acquisition  
- **MQTT** – Lightweight communication protocol  
- **Node-RED** – Data processing & routing  
- **InfluxDB** – Time-series database  
- **Grafana** – Alerts & visualization  
- **Ethereum Blockchain** – Secure data storage  
- **Telegram Bot** – Data query interface  
- **Docker** – Containerized service orchestration with Arrowhead  

---

## Project Structure

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
