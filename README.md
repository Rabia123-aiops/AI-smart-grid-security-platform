# 🛡️ AI-Driven Smart Grid Security Platform

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![SCADA](https://img.shields.io/badge/SCADA%2FICS-Security-red.svg)](#)
[![EduQual](https://img.shields.io/badge/EduQual-Level%206-purple.svg)](#)

Built for my **EduQual Level 6 assessment — Diploma in Artificial Intelligence Operations**.

The assessment brief required the design and implementation of an AI-driven smart-grid security platform covering **SCADA protection, energy theft detection, grid resilience automation, monitoring, DevSecOps, and compliance support for critical energy infrastructure**. This repository contains the working prototype developed for that purpose.

**Author:** Rabia Shehzadi  
**Email:** rabiashehzadi878@gmail.com

---

## 🎯 Why This Project

Power grids are critical infrastructure, and modern SCADA/ICS environments are increasingly exposed to cyberattacks, equipment anomalies, electricity theft, and operational failures.

Testing attacks against a real substation or production power network would be unsafe and impractical. Therefore, I built a self-contained laboratory on a single Ubuntu virtual machine with **2 CPU cores and 8 GB RAM**.

The prototype safely reproduces the major parts of a smart-grid security environment:

- a simulated IEEE 13-bus distribution grid
- a Conpot decoy PLC using Modbus
- Suricata intrusion detection
- machine-learning and deep-learning models
- electricity-theft detection
- automated resilience actions
- Prometheus, Grafana, and Flask monitoring
- DevSecOps and compliance evidence

> **Project scope:** This is an educational prototype and proof of concept. It is not intended for direct connection to a live power grid or operational substation.

---

## 📖 What Actually Happens

1. `grid_model.py` generates simulated voltage and current readings from the IEEE 13-bus grid and writes them to `grid_readings.csv`.

2. Conpot runs as a simulated PLC and listens for Modbus traffic.

3. `malicious_traffic.py` sends rapid unauthorised Modbus write requests to the Conpot honeypot.

4. Conpot receives and records the requests.

5. Suricata monitors the traffic, applies the custom Modbus detection rule, and records matching alerts in `eve.json`.

6. Isolation Forest, Random Forest, and the LSTM Autoencoder analyse grid data for abnormal behaviour.

7. The energy-theft model analyses synthetic smart-meter records for suspicious consumption patterns.

8. The resilience engine records simulated load shedding, fault isolation, and self-healing actions.

9. Prometheus collects metrics, while Grafana and the Flask dashboard display the live system status.

---

## 🏗️ Platform Architecture

```text
                           AI-DRIVEN SMART GRID SECURITY PLATFORM

     ┌──────────────────────── SMART GRID / OT ENVIRONMENT ────────────────────────┐
     │                                                                             │
     │  IEEE 13-Bus Grid Simulation                 Conpot PLC / Modbus Honeypot    │
     │  grid_model.py                               malicious_traffic.py            │
     │            │                                            │                   │
     │            ▼                                            ▼                   │
     │  Voltage / Current Readings                   Industrial Network Events      │
     └────────────┬────────────────────────────────────────────┬────────────────────┘
                  │                                            │
                  ▼                                            ▼
         grid_readings.csv                           Suricata IDS + eve.json
                  │                                            │
                  ├──────────────────────┬─────────────────────┘
                  ▼                      ▼
        Isolation Forest /        Alert Parsing and
        Random Forest / LSTM      Security Event Summary
                  └──────────────┬───────────────┘
                                 ▼
                    Detection and Decision Logic
                                 │
                                 ▼
                      Grid Resilience Engine
              Load Shedding | Fault Isolation | Self-Healing
                                 │
               ┌─────────────────┼─────────────────┐
               ▼                 ▼                 ▼
          Prometheus       Grafana Dashboard   Flask Dashboard
                                 │
                                 ▼
                      Grid Operator / Analyst

       DevSecOps Support: Bandit | pip-audit | GitHub Actions | Compliance Checks
```

---

## 🔄 End-to-End Data Flow

```text
Grid Simulation
      ↓
Grid Measurements
      ↓
CSV and Metrics
      ↓
Isolation Forest / Random Forest / LSTM
      ↓
Anomaly Detection
      ↓
Resilience Engine
      ↓
Prometheus
      ↓
Grafana and Flask Dashboards
```

```text
Malicious Traffic Script
      ↓
Conpot Simulated PLC
      ↓
Suricata IDS
      ↓
eve.json Alerts
      ↓
Alert Parser
      ↓
Dashboard and Audit Evidence
```

---

## 🔐 Prototype OT/IT Convergence

The project demonstrates **prototype-level OT/IT convergence**.

### OT components

- IEEE 13-bus grid simulation
- Conpot simulated PLC
- Modbus traffic
- grid measurements
- simulated faults and attacks

### IT and security components

- Python AI and ML models
- Suricata alert processing
- Prometheus monitoring
- Grafana and Flask dashboards
- GitHub Actions and security scanning

The connection between OT and IT is created through the transfer of simulated grid measurements, industrial traffic events, alerts, and metrics into IT-based analytics, monitoring, and reporting services.

---

## 🛠️ Technology Stack

| Category | Tools Used |
|---|---|
| Grid simulation | OpenDSS, `opendssdirect.py`, IEEE 13-bus feeder |
| SCADA simulation | Conpot, Modbus, `pymodbus` |
| Intrusion detection | Suricata, custom rules, `eve.json` |
| Machine learning | scikit-learn, Isolation Forest, Random Forest |
| Deep learning | TensorFlow CPU, LSTM Autoencoder |
| Monitoring | Prometheus, Grafana, Flask |
| Containers | Docker, Docker Compose |
| DevSecOps | Bandit, pip-audit, GitHub Actions |
| Platform | Python 3.10, Ubuntu 22.04 |

Apache Spark was deliberately not used because the prototype runs on a resource-constrained 2-core, 8 GB virtual machine. A lightweight local pipeline was more appropriate for this project scale.

---

## 📁 Repository Layout

```text
AI-smart-grid-security-platform/
├── .github/                 # CI and security workflow
├── conpot/                  # SCADA honeypot and attack simulation
├── dashboard/               # Flask monitoring dashboard
├── devsecops/               # security scans and compliance evidence
├── docs/
│   └── screenshots/         # project implementation evidence
├── ml/                      # ML, energy-theft, and LSTM models
├── opendss/                 # grid simulation and IEEE feeder files
├── prometheus/              # metrics exporter and configuration
├── resilience/              # resilience automation
├── suricata/                # IDS rules and alert parser
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└── README.md
```
---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Rabia123-aiops/AI-smart-grid-security-platform.git
cd AI-smart-grid-security-platform
```

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Verify Docker installation:

```bash
docker --version
docker-compose --version
```

---

# ▶️ Running the Prototype

## Step 1 – Start Docker Services

```bash
docker-compose up -d
```

Verify all containers are running:

```bash
docker ps
```

The following services should be running:

- Conpot Honeypot
- Prometheus
- Grafana

---

## Step 2 – Run the Smart Grid Simulation

```bash
cd opendss

python3 grid_model.py
```

This script loads the IEEE 13-Bus feeder and continuously generates simulated voltage and current measurements.

---

## Step 3 – (Optional) Generate Normal SCADA Traffic

```bash
cd conpot

python3 normal_traffic.py
```

This script generates legitimate Modbus read requests to the simulated PLC. It is useful for comparing normal operational behaviour with malicious traffic.

> **Important:** Ensure the Docker containers are running before executing this script.

---

## Step 4 – Generate Malicious Modbus Traffic

```bash
cd conpot

python3 malicious_traffic.py
```

This script sends rapid unauthorised Modbus write requests against the simulated PLC to demonstrate cyberattack detection.

---

## Step 5 – Monitor and Parse Suricata Alerts

Start Suricata:

```bash
sudo suricata -c /etc/suricata/suricata.yaml -i lo
```

Parse detected alerts:

```bash
cd suricata

python3 parse_alerts.py
```

The parser extracts security events from Suricata logs for reporting and dashboard visualisation.

---

## Step 6 – Execute the AI Models

```bash
cd ml

python3 ml_models.py

python3 energy_theft_detection.py

python3 lstm_anomaly_detection.py
```

The AI module performs:

- Isolation Forest anomaly detection
- Random Forest classification
- Synthetic energy theft detection
- LSTM Autoencoder sequence anomaly detection

---

## Step 7 – Execute Grid Resilience Automation

```bash
cd resilience

python3 resilience_engine.py
```

The resilience engine simulates:

- Load shedding
- Fault isolation
- Self-healing

Generated events are recorded in:

```text
resilience/resilience_events.log
```

---

## Step 8 – Start the Prometheus Exporter

```bash
cd prometheus

python3 prometheus_exporter.py
```

The exporter publishes simulated smart-grid metrics for Prometheus.

---

## Step 9 – Launch the Flask Dashboard

```bash
cd dashboard

python3 app.py
```

The Flask dashboard displays:

- Live grid measurements
- Security alerts
- AI detection results
- Grid resilience events

---

## Step 10 – Run the Compliance Verification

```bash
cd devsecops

python3 compliance_check.py
```

The compliance script verifies the availability of project artefacts, security reports, and implementation evidence.

---

# 🌐 Local Services

| Service | URL | Purpose |
|----------|-----|----------|
| Flask Dashboard | http://127.0.0.1:5000 | Live Smart Grid Monitoring |
| Grafana | http://127.0.0.1:3000 | Dashboard Visualisation |
| Prometheus | http://127.0.0.1:9090 | Metrics Collection |
| Conpot (HTTP) | http://127.0.0.1:80 | Simulated PLC Web Interface |
| Conpot (Modbus) | 127.0.0.1:502 | Modbus TCP Service |

---

# 📦 Prototype Execution Workflow

```text
Start Docker Containers
          │
          ▼
Run Grid Simulation
          │
          ▼
(Optional) Generate Normal Traffic
          │
          ▼
Generate Malicious Traffic
          │
          ▼
Suricata Detects Threats
          │
          ▼
Parse Security Alerts
          │
          ▼
Run AI Models
          │
          ▼
Execute Resilience Engine
          │
          ▼
Publish Metrics to Prometheus
          │
          ▼
Grafana & Flask Dashboards
          │
          ▼
Run Compliance Verification
```
