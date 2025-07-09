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

### 1. Wi-Fi configuration for Libelium
- Connected to **WaspMote**, selected the right Port and implemented a Wi-Fi configuration code;
- Now, the **Wi-Fi** is **configured** on the station;
  
### 2. Data Gathering
- Uploaded a Data Gathering code, that declares each sensor by its socket;
- Named the Moat ID as: “Darius-Libelium”. This is used to create the topic;
- The data is collected from the station with .get() functions;
- Printed text for user-friendly approach;
- Created a frame that will be sent further to the Broker;

### 3. Node-Red Data Processing
- The data from WaspMote gets to the MQTT IN Node with the name: **meshlium3d4c/Darius-Libelium/#**, where: **meshlium3d4c** is the name of the meshlium, **Darius-Libelium** is the name of the topic, and **#** is used so the data from all the sensors is transmitted.
- The data goes through a **JSON Node**, and then it does into the MQTT OUT Node with the topic **training/device/darius-vasile**;

### 4. Grafana Data Visualization
- Displayed the **Battery Status** and the **Temperature** in a Dashboard;
- Displayed the **Pressure** as a **Gauge**;

### 5. Grafana Alerts
- Set 2 **alerts** for the temperature. An alert will be sent on my personal email if the temperature is **above 25** or **above 29**;
- Received the **alert** on the email;

### 6. Node-Red for Data Processing
- Added a **Function Node** into the architecture, that converts the Temperature from **Celsius to Kelvin**;
- Checked the result with a **Debug Node**;

---

## ChatBot for Data Interrogation
- Created a **ChatBot** using **Telegram**, to get the values generated at random by the **Python Script**;
- get_latest_data() extracts the latest data from the JSON file;
- The start() function displays every command available on the ChatBot;
- The humidity(), temperature(), radiation(), precipitation() functions show the parameters in the ChatBot;
- The all_data() function displays all the parameters extracted;
- Also, created an alert, that sends a message if the temperature is **over 30**;

For the next step, the random data generator script has been replaced with **real sensor data** from a **Libelium station**.
- Generated a **Python Script**( mqtt_waspmote.py) , that gets the data from the **Libelium station**, using the **Broker** and the **Topic**, and creates a **JSON file**, ready to be sent in **Telegram**.










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
