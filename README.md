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

- **Python** – Data simulation & MQTT publishing;  
- **Libelium** – Real sensor data acquisition;  
- **MQTT** – Lightweight communication protocol; 
- **Node-RED** – Data processing & routing;  
- **InfluxDB** – Time-series database;  
- **Grafana** – Alerts & visualization;  
- **Ethereum Blockchain** – Secure data storage;  
- **Telegram Bot** – Data query interface;  
- **Docker** – Containerized service orchestration with Arrowhead;  

---

## IoT Data Simulation
- Used **Python Script** to simulate the communication;
- Imported all the **libraries** for MQTT, JSON;
- Generated data for **temperature, humidity, solar radiation and precipitation** with a random function. Generated the timestamp using the .strftime() function;
  
---

## Node-Red Data Processing
- **Node-Red** is used to take the data from the **MQTT Broker**, process it, save it locally and send it to an InfluxDB Data Base;
- The **MQTT IN** Node gets the data from the Broker using the server and the topic;
- Used 2 **Debug Nodes** to check the data before and after applying a JSON Node;
- The **MQTT OUT** Node sends the data further to Grafana;

---

## Grafana - Data Visualization
- Created a new **Grafana dashboard**;
- Imported the **topic**(in this picture, it’s the temperature parameter, generated with the random values);

---

## Libelium for Data Gathering
- Replaced the random values generated in the Python script with actual data from a **Libelium station**;
- The station, equipped with **sensors**, gathers data and sends it to the **MQTT Broker**;

---

### Wi-Fi configuration for Libelium


## Project Structure

```bash
pre-practica-project/
│
├── code/                    
│   ├── mqtt_random.py
│   ├── mqtt_waspmote.py
│   ├── send_to_blockchain.py
│   └── darius_bot.py
│
├── photos/           
│
├── README.md
├── LICENSE
└── .gitignore
