# 🛡️ AI-Driven Smart Grid Security Platform

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![SCADA](https://img.shields.io/badge/SCADA%2FICS-Security-red.svg)](#)
[![EduQual](https://img.shields.io/badge/EduQual-Level%206-purple.svg)](#)

Built for my **EduQual Level 6 assessment — Diploma in Artificial Intelligence Operations**.

The assessment brief required the design and implementation of an AI-driven smart-grid security platform covering **SCADA protection, energy theft detection, grid resilience automation, monitoring, DevSecOps, and compliance support for critical energy infrastructure**. This repository contains the working prototype developed for that purpose.

**Author:** Rabia Shehzadi  
**Email:** rabiashehzadi878@gmail.com
## 📑 Table of Contents

- [🎯 Why This Project](#-why-this-project)
- [📖 What Actually Happens](#-what-actually-happens)
- [🏗️ Platform Architecture](#️-platform-architecture)
- [🔄 End-to-End Data Flow](#-end-to-end-data-flow)
- [🔐 Prototype OT/IT Convergence](#-prototype-otit-convergence)
- [🛠️ Technology Stack](#️-technology-stack)
- [📁 Repository Layout](#-repository-layout)
- [⚙️ Installation](#️-installation)
- [▶️ Running the Prototype](#️-running-the-prototype)
- [🌐 Local Services](#-local-services)
- [📦 Prototype Execution Workflow](#-prototype-execution-workflow)
- [📸 Results and Implementation Evidence](#-results-and-implementation-evidence)
- [📊 Monitoring and Visualisation](#-monitoring-and-visualisation)
- [🔐 DevSecOps Implementation](#-devsecops-implementation)
- [📋 Compliance Support and Audit Evidence](#-compliance-support-and-audit-evidence)
- [✅ Implementation Achievements](#-implementation-achievements)
- [⚠️ Project Limitations](#️-project-limitations)
- [🚀 Future Improvements](#-future-improvements)
- [🏢 Enterprise Deployment Scenario](#-enterprise-deployment-scenario)
- [📖 Lessons Learned](#-lessons-learned)
- [📚 References](#-references)
- [🙏 Acknowledgements](#-acknowledgements)
- [📄 License](#-license)
- [⭐ Final Project Summary](#-final-project-summary)
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
---

# 📸 Results and Implementation Evidence

The following implementation evidence was generated during prototype testing on the Ubuntu laboratory environment. The screenshots demonstrate the successful integration of the smart-grid simulation, SCADA honeypot, intrusion detection, artificial intelligence, resilience automation, and monitoring components.

---

# ⚡ Smart Grid Simulation

The OpenDSS simulation successfully loads the IEEE 13-Bus feeder and continuously generates simulated voltage and current measurements.

Controlled abnormal operating conditions are introduced into the simulation so that the AI models can identify unusual grid behaviour without affecting any real electrical infrastructure.

### Grid Simulation

![Grid Simulation Terminal](docs/screenshots/grid-simulation-terminal.png)

### Grid Anomaly Detection

![Grid Anomaly Detection](docs/screenshots/grid-anomaly-detection.png)

### Grid Health Monitoring

![Grid Health Graph](docs/screenshots/grid-health-graph.png)

---

# 🏭 SCADA / ICS Honeypot

Conpot simulates an industrial PLC supporting Modbus TCP services.

The project demonstrates both:

- Normal Modbus communication
- Malicious Modbus attack traffic

### Conpot Startup

![Conpot Startup](docs/screenshots/conpot-startup-command.png)

### Conpot Services

![Conpot Running](docs/screenshots/conpot-servers-started.png)

### Attack Received

![Conpot Attack](docs/screenshots/conpot-received-attack.png)

### Malicious Modbus Traffic

![Malicious Traffic](docs/screenshots/scada-malicious-traffic-attack.png)

---

# 🚨 Suricata Intrusion Detection

Suricata continuously monitors industrial Modbus traffic and applies the custom detection rule defined in:

```text
suricata/local.rules
```

During attack simulation, Suricata successfully generated security alerts that were parsed and summarised for further analysis.

### Suricata Engine

![Suricata Engine](docs/screenshots/suricata-setup-engine-started.png)

### Alert Detection

![Suricata Alert](docs/screenshots/suricata-alert-detected-full.png)

### Alert Summary

![Suricata Summary](docs/screenshots/suricata-alert-summary.png)

---

# 🤖 Machine Learning Results

The AI module combines unsupervised learning, supervised learning, and deep learning techniques to analyse simulated smart-grid data.

---

## Isolation Forest

Prototype testing produced:

- Total simulated samples analysed: **109**
- Anomalies detected: **11**

Isolation Forest detects abnormal operating behaviour without requiring labelled attack data.

---

## Random Forest

On the labelled prototype evaluation dataset:

- Accuracy = **100%**
- Precision = **100%**
- Recall = **100%**
- F1-score = **100%**

These results represent performance on the prototype evaluation dataset used in this project and should not be interpreted as guaranteed real-world performance.

![Isolation Forest and Random Forest](docs/screenshots/ml-isolation-random-forest.png)

---

# ⚡ Energy Theft Detection

The synthetic smart-meter dataset contains:

- **500 customer records**
- **30 labelled theft cases**

During prototype evaluation:

- **40 potentially suspicious customers were identified**
- **Overall classification accuracy: 98%**

The identified customers represent records that would require additional investigation before confirming electricity theft.

![Energy Theft Detection](docs/screenshots/ml-energy-theft-detection.png)

The generated confusion matrix is available in:

```text
ml/energy_theft_confusion_matrix.png
```

---

# 🧠 LSTM Autoencoder

Unlike Random Forest, the LSTM Autoencoder analyses sequential time-series behaviour.

Prototype testing produced:

- Total sequences analysed: **99**
- Anomalous sequences detected: **5**

An anomaly is identified whenever the reconstruction error exceeds the learned threshold.

![LSTM Results](docs/screenshots/ml-lstm-anomaly-results.png)

---

# ⚙️ Grid Resilience Engine

The resilience engine demonstrates automated response actions following abnormal grid behaviour.

Implemented resilience actions include:

- Load shedding
- Fault isolation
- Backup feeder activation
- Event logging

All resilience actions are simulated and do not operate physical substations or electrical breakers.

![Resilience Event Log](docs/screenshots/resilience-event-log.png)

Generated event log:

```text
resilience/resilience_events.log
```

---

# ✅ Prototype Summary

| Component | Prototype Result |
|-----------|------------------|
| Smart Grid | IEEE 13-Bus simulation running successfully |
| SCADA | Conpot simulated PLC operational |
| Modbus | Normal and malicious traffic demonstrated |
| Suricata | Industrial attacks successfully detected |
| Isolation Forest | 11 anomalies detected from 109 samples |
| Random Forest | 100% accuracy on prototype evaluation dataset |
| Energy Theft | 98% accuracy using synthetic customer dataset |
| LSTM | 5 anomalous sequences detected from 99 sequences |
| Resilience | Load shedding, fault isolation and backup feeder events logged |
---

# 📊 Monitoring and Visualisation

The prototype uses Prometheus, Grafana, and a custom Flask dashboard to provide real-time visibility into simulated grid behaviour, security events, anomaly detections, and resilience activity.

---

## Prometheus Metrics

The custom exporter publishes smart-grid metrics that Prometheus collects and makes available for monitoring and query analysis.

![Prometheus Query Result](docs/screenshots/prometheus-query-result.png)

---

## Grafana Monitoring Dashboard

Grafana visualises the metrics collected by Prometheus and provides persistent monitoring panels for the prototype.

The dashboard demonstrates:

- voltage and current monitoring
- grid health status
- anomaly visibility
- real-time operational trends

### Prometheus Data Source Connected

![Grafana Data Source Connected](docs/screenshots/grafana-datasource-connected.png)

### Grafana Dashboard — Top Section

![Grafana Dashboard Top](docs/screenshots/grafana-dashboard-top.png)

### Grafana Dashboard — Bottom Section

![Grafana Dashboard Bottom](docs/screenshots/grafana-dashboard-bottom.png)

---

## Flask Live Dashboard

The custom Flask application provides a lightweight operational interface for viewing live smart-grid information.

It displays:

- live voltage and current readings
- grid health information
- anomaly alerts
- resilience-event information

![Flask Live Monitoring Dashboard](docs/screenshots/dashboard-live-monitoring.png)

---

## Docker Environment

Docker Compose is used to run the main infrastructure services in a repeatable environment.

The running services include:

- Conpot
- Prometheus
- Grafana

### All Containers Running

![All Containers Running](docs/screenshots/all-containers-running.png)

### Prometheus and Grafana Containers

![Docker Prometheus and Grafana](docs/screenshots/docker-ps-prometheus-grafana.png)

---

# 🔐 DevSecOps Implementation

DevSecOps practices were added to the project to support secure development, repeatable validation, and audit evidence.

The implementation includes:

- Bandit static code analysis
- pip-audit dependency checking
- GitHub Actions security workflow
- automated compliance verification
- version-controlled reports and evidence

---

## Bandit Static Security Scan

Bandit analyses Python source code for common security weaknesses and unsafe coding patterns.

![Bandit Security Scan](docs/screenshots/devsecops-bandit-scan.png)

---

## pip-audit Dependency Scan

pip-audit checks installed Python dependencies against known vulnerability databases.

![pip-audit Dependency Scan](docs/screenshots/devsecops-pip-audit.png)

---

## GitHub Actions Workflow

The automated security workflow is stored in:

```text
.github/workflows/security-check.yml
```

This workflow supports repeatable security checks through version-controlled automation.

---

# 📋 Compliance Support and Audit Evidence

The project demonstrates compliance support through automated checks, logging, monitoring, and preserved implementation evidence.

The custom script is stored in:

```text
devsecops/compliance_check.py
```

Generated reports include:

```text
devsecops/compliance_report.txt
devsecops/bandit_report.txt
devsecops/pip_audit_report.txt
```

The compliance check verifies the presence of important project artefacts such as:

- security scan reports
- Suricata rules
- saved AI models
- resilience logs
- monitoring evidence
- documentation
- licensing information

![DevSecOps Compliance Check](docs/screenshots/devsecops-compliance-check.png)

---

## Compliance Mapping

| Security and governance area | Prototype implementation |
|---|---|
| Secure coding | Bandit static security analysis |
| Dependency management | pip-audit vulnerability checking |
| Intrusion monitoring | Suricata IDS and alert logs |
| Audit trail | Suricata alerts and resilience-event logs |
| Continuous verification | GitHub Actions workflow |
| Monitoring | Prometheus, Grafana, and Flask |
| Evidence management | Version-controlled reports and screenshots |
| Compliance checking | Custom `compliance_check.py` script |

> **Important:** This prototype demonstrates compliance support and audit readiness. It does not claim formal certification against NERC CIP, IEC 62351, ISA/IEC 62443, or any other industrial standard.

---

# ✅ Implementation Achievements

- [x] IEEE 13-Bus grid simulation
- [x] Conpot SCADA/PLC honeypot
- [x] Normal and malicious Modbus traffic
- [x] Suricata intrusion detection
- [x] Isolation Forest anomaly detection
- [x] Random Forest classification
- [x] Synthetic energy-theft detection
- [x] LSTM Autoencoder anomaly detection
- [x] Grid-resilience automation
- [x] Prometheus metrics collection
- [x] Grafana monitoring dashboard
- [x] Flask live dashboard
- [x] Docker-based infrastructure
- [x] DevSecOps security scans
- [x] Automated compliance evidence checking
---

# ⚠️ Project Limitations

This project was developed as an educational prototype for the EduQual Level 6 Diploma in Artificial Intelligence Operations.

The current implementation has several limitations:

- The platform operates on a single Ubuntu virtual machine.
- Grid behaviour is simulated using the IEEE 13-Bus OpenDSS model.
- Conpot is used as a simulated PLC rather than physical industrial hardware.
- Energy-theft detection is evaluated using synthetic smart-meter data.
- AI models are trained using prototype datasets.
- The project is intended for laboratory demonstration and research purposes only.

---

# 🚀 Future Improvements

The prototype can be extended into a larger research or enterprise platform by introducing:

- Apache Kafka for real-time event streaming
- Apache Spark for distributed AI analytics
- Kubernetes container orchestration
- MQTT integration for IoT smart meters
- IEC 61850 protocol support
- Digital Twin integration
- Real PLC and RTU connectivity
- SIEM integration (e.g., Splunk or Microsoft Sentinel)
- Cloud-native deployment
- High-availability monitoring architecture

---

# 🏢 Enterprise Deployment Scenario

In an enterprise smart-grid environment, the prototype could be deployed using a layered architecture:

- Multiple substations connected through secure VPNs
- Redundant SCADA servers
- Central Security Operations Centre (SOC)
- Distributed AI inference services
- Central SIEM platform
- Redundant Prometheus and Grafana servers
- Secure API gateways
- Backup disaster recovery infrastructure

The current repository demonstrates the core concepts required for such a deployment but does not represent a production-ready implementation.

---

# 📖 Lessons Learned

During the development of this prototype, several practical lessons were learned:

- AI becomes more effective when combined with traditional intrusion detection.
- Simulated industrial environments provide a safe platform for cyber-security experimentation.
- Continuous monitoring significantly improves operational visibility.
- Docker simplifies deployment and improves reproducibility.
- DevSecOps practices improve project quality and audit readiness.

---

# 📚 References

Official documentation used during development:

- OpenDSS
- Conpot
- Suricata IDS
- Prometheus
- Grafana
- Docker
- TensorFlow
- Scikit-learn
- pymodbus
- Python Software Foundation

---

# 🙏 Acknowledgements

This project was developed as part of the EduQual Level 6 Diploma in Artificial Intelligence Operations.

Special thanks to the maintainers of the open-source tools and frameworks that made this prototype possible.

---

# 📄 License

This project is released under the **MIT License**.

See the `LICENSE` file for complete licensing information.

---

# ⭐ Final Project Summary

This repository demonstrates an end-to-end AI-driven smart-grid cyber-security prototype integrating:

- Smart-grid simulation
- SCADA/ICS security
- Modbus attack simulation
- AI-based anomaly detection
- Energy-theft detection
- Grid resilience automation
- Real-time monitoring
- Docker deployment
- DevSecOps practices
- Compliance-support automation

Although developed as an educational prototype, the project demonstrates the integration of multiple technologies commonly used in modern cyber-physical power-system security research.
