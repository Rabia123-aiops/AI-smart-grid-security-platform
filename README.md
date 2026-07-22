# 🛡️ AI-Driven Smart Grid Security Platform

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![SCADA](https://img.shields.io/badge/SCADA%2FICS-Security-red.svg)](#)
[![EduQual](https://img.shields.io/badge/EduQual-Level%206-purple.svg)](#)

Built for my **EduQual Level 6 assessment — Diploma in Artificial Intelligence Operations**.

A working prototype of an AI-driven smart-grid security platform covering **SCADA protection, energy theft detection, grid resilience automation, monitoring, DevSecOps, and compliance support** for critical energy infrastructure.

**Author:** Rabia Shehzadi
**Email:** rabiashehzadi878@gmail.com


## 📑 Table of Contents

- [Why This Project](#-why-this-project)
- [What Actually Happens](#-what-actually-happens)
- [Platform Architecture](#-platform-architecture)
- [End-to-End Data Flow](#-end-to-end-data-flow)
- [Prototype OT/IT Convergence](#-prototype-otit-convergence)
- [Technology Stack](#-technology-stack)
- [Repository Layout](#-repository-layout)
- [Installation](#-installation)
- [Running the Prototype](#-running-the-prototype)
- [Local Services](#-local-services)
- [Prototype Execution Workflow](#-prototype-execution-workflow)
- [Results and Implementation Evidence](#-results-and-implementation-evidence)
- [Smart Grid Simulation](#-smart-grid-simulation)
- [SCADA / ICS Honeypot](#-scada--ics-honeypot)
- [Suricata Intrusion Detection](#-suricata-intrusion-detection)
- [Machine Learning Results](#-machine-learning-results)
- [Energy Theft Detection](#-energy-theft-detection)
- [LSTM Autoencoder](#-lstm-autoencoder)
- [Grid Resilience Engine](#-grid-resilience-engine)
- [Prototype Summary](#-prototype-summary)
- [Monitoring and Visualisation](#-monitoring-and-visualisation)
- [DevSecOps Implementation](#-devsecops-implementation)
- [Compliance Support and Audit Evidence](#-compliance-support-and-audit-evidence)
- [Implementation Achievements](#-implementation-achievements)
- [Project Limitations](#-project-limitations)
- [Future Improvements](#-future-improvements)
- [Enterprise Deployment Scenario](#-enterprise-deployment-scenario)
- [Lessons Learned](#-lessons-learned)
- [References](#-references)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)
- [Final Project Summary](#-final-project-summary)


---

## 🎯 Why This Project

Power grids are critical infrastructure, and SCADA/ICS environments are increasingly exposed to cyberattacks, anomalies, electricity theft, and operational failures.

Since testing attacks on a real substation is unsafe, I built a self-contained lab on a single Ubuntu VM (**2 CPU cores, 8 GB RAM**) that reproduces the core parts of a smart-grid security environment:

- a simulated IEEE 13-bus distribution grid
- a Conpot decoy PLC using Modbus
- Suricata intrusion detection
- ML/DL anomaly detection models
- electricity-theft detection
- automated resilience actions
- Prometheus, Grafana, and Flask monitoring
- DevSecOps and compliance evidence

> **Scope:** Educational prototype / proof of concept — not intended for connection to a live grid or substation.

---

## 📖 What Actually Happens

1. `grid_model.py` simulates IEEE 13-bus voltage/current readings into `grid_readings.csv`.
2. Conpot runs as a simulated PLC, listening for Modbus traffic.
3. `malicious_traffic.py` sends unauthorised Modbus write requests to Conpot.
4. Conpot logs the requests.
5. Suricata monitors traffic and logs matching alerts to `eve.json`.
6. Isolation Forest, Random Forest, and an LSTM Autoencoder analyse grid data for anomalies.
7. The energy-theft model flags suspicious consumption in synthetic smart-meter data.
8. The resilience engine simulates load shedding, fault isolation, and self-healing.
9. Prometheus, Grafana, and the Flask dashboard display live status.

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

Demonstrates **prototype-level OT/IT convergence**.

### OT components
- IEEE 13-bus grid simulation
- Conpot simulated PLC
- Modbus traffic
- grid measurements
- simulated faults and attacks

### IT and security components
- Python AI/ML models
- Suricata alert processing
- Prometheus monitoring
- Grafana and Flask dashboards
- GitHub Actions and security scanning

OT and IT are connected by feeding simulated grid measurements, industrial traffic events, alerts, and metrics into IT-based analytics, monitoring, and reporting.

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

Apache Spark was skipped since the prototype runs on a resource-constrained 2-core, 8 GB VM — a lightweight local pipeline fit the project scale better.

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

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

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

Verify containers:

```bash
docker ps
```

Should be running:
- Conpot Honeypot
- Prometheus
- Grafana

---

## Step 2 – Run the Smart Grid Simulation

```bash
cd opendss
python3 grid_model.py
```

Loads the IEEE 13-Bus feeder and continuously generates simulated voltage/current data.

---

## Step 3 – (Optional) Generate Normal SCADA Traffic

```bash
cd conpot
python3 normal_traffic.py
```

Sends legitimate Modbus read requests to the PLC — useful for comparing against malicious traffic.

> **Important:** Ensure Docker containers are running first.

---

## Step 4 – Generate Malicious Modbus Traffic

```bash
cd conpot
python3 malicious_traffic.py
```

Sends rapid unauthorised Modbus write requests to demonstrate attack detection.

---

## Step 5 – Monitor and Parse Suricata Alerts

Start Suricata:

```bash
sudo suricata -c /etc/suricata/suricata.yaml -i lo
```

Parse alerts:

```bash
cd suricata
python3 parse_alerts.py
```

Extracts security events from Suricata logs for reporting and dashboard use.

---

## Step 6 – Execute the AI Models

```bash
cd ml
python3 ml_models.py
python3 energy_theft_detection.py
python3 lstm_anomaly_detection.py
```

Runs:
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

Simulates load shedding, fault isolation, and self-healing. Events logged to:

```text
resilience/resilience_events.log
```

---

## Step 8 – Start the Prometheus Exporter

```bash
cd prometheus
python3 prometheus_exporter.py
```

Publishes simulated smart-grid metrics for Prometheus.

---

## Step 9 – Launch the Flask Dashboard

```bash
cd dashboard
python3 app.py
```

Displays live grid measurements, security alerts, AI detection results, and resilience events.

---

## Step 10 – Run the Compliance Verification

```bash
cd devsecops
python3 compliance_check.py
```

Verifies availability of project artefacts, security reports, and implementation evidence.

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

Evidence generated during prototype testing on the Ubuntu lab environment, showing successful integration of grid simulation, SCADA honeypot, intrusion detection, AI, resilience automation, and monitoring.

---

# ⚡ Smart Grid Simulation

The OpenDSS simulation loads the IEEE 13-Bus feeder and continuously generates simulated voltage/current data. Controlled abnormal conditions are introduced so AI models can identify unusual behaviour without affecting real infrastructure.

### Grid Simulation
![Grid Simulation Terminal](docs/screenshots/grid-simulation-terminal.png)

### Grid Anomaly Detection
![Grid Anomaly Detection](docs/screenshots/grid-anomaly-detection.png)

### Grid Health Monitoring
![Grid Health Graph](docs/screenshots/grid-health-graph.png)

---

# 🏭 SCADA / ICS Honeypot

Conpot simulates an industrial PLC with Modbus TCP services, demonstrating both normal and malicious traffic.

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

Suricata monitors industrial Modbus traffic using the custom rule in `suricata/local.rules`. During attack simulation, alerts were generated, parsed, and summarised.

### Suricata Engine
![Suricata Engine](docs/screenshots/suricata-setup-engine-started.png)

### Alert Detection
![Suricata Alert](docs/screenshots/suricata-alert-detected-full.png)

### Alert Summary
![Suricata Summary](docs/screenshots/suricata-alert-summary.png)

---

# 🤖 Machine Learning Results

The AI module combines unsupervised, supervised, and deep learning to analyse simulated grid data.

## Isolation Forest
- Total simulated samples analysed: **109**
- Anomalies detected: **11**

Detects abnormal behaviour without labelled attack data.

## Random Forest
- Accuracy / Precision / Recall / F1-score = **100%** (on the prototype evaluation dataset — not a guarantee of real-world performance)

![Isolation Forest and Random Forest](docs/screenshots/ml-isolation-random-forest.png)

---

# ⚡ Energy Theft Detection

Synthetic dataset: **500 customer records**, **30 labelled theft cases**.

- **40 potentially suspicious customers identified**
- **Overall classification accuracy: 98%**

Flagged customers would require further investigation before confirming theft.

![Energy Theft Detection](docs/screenshots/ml-energy-theft-detection.png)

Confusion matrix: `ml/energy_theft_confusion_matrix.png`

---

# 🧠 LSTM Autoencoder

Analyses sequential time-series behaviour (unlike Random Forest).

- Total sequences analysed: **99**
- Anomalous sequences detected: **5**

An anomaly is flagged when reconstruction error exceeds the learned threshold.

![LSTM Results](docs/screenshots/ml-lstm-anomaly-results.png)

---

# ⚙️ Grid Resilience Engine

Demonstrates automated response to abnormal grid behaviour: load shedding, fault isolation, backup feeder activation, and event logging. All actions are simulated — no physical substations or breakers are involved.

![Resilience Event Log](docs/screenshots/resilience-event-log.png)

Event log: `resilience/resilience_events.log`

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

Prometheus, Grafana, and a custom Flask dashboard provide real-time visibility into grid behaviour, security events, anomalies, and resilience activity.

## Prometheus Metrics

The custom exporter publishes smart-grid metrics that Prometheus collects.

![Prometheus Query Result](docs/screenshots/prometheus-query-result.png)

## Grafana Monitoring Dashboard

Visualises Prometheus metrics with persistent monitoring panels covering voltage/current, grid health, anomaly visibility, and real-time trends.

### Prometheus Data Source Connected
![Grafana Data Source Connected](docs/screenshots/grafana-datasource-connected.png)

### Grafana Dashboard — Top Section
![Grafana Dashboard Top](docs/screenshots/grafana-dashboard-top.png)

### Grafana Dashboard — Bottom Section
![Grafana Dashboard Bottom](docs/screenshots/grafana-dashboard-bottom.png)

---

## Flask Live Dashboard

A lightweight operational interface showing live voltage/current readings, grid health, anomaly alerts, and resilience events.

![Flask Live Monitoring Dashboard](docs/screenshots/dashboard-live-monitoring.png)

---

## Docker Environment

Docker Compose runs the core infrastructure (Conpot, Prometheus, Grafana) in a repeatable environment.

### All Containers Running
![All Containers Running](docs/screenshots/all-containers-running.png)

### Prometheus and Grafana Containers
![Docker Prometheus and Grafana](docs/screenshots/docker-ps-prometheus-grafana.png)

---

# 🔐 DevSecOps Implementation

Added to support secure development, repeatable validation, and audit evidence:

- Bandit static code analysis
- pip-audit dependency checking
- GitHub Actions security workflow
- automated compliance verification
- version-controlled reports and evidence

## Bandit Static Security Scan

Analyses Python source code for common security weaknesses.

![Bandit Security Scan](docs/screenshots/devsecops-bandit-scan.png)

## pip-audit Dependency Scan

Checks installed dependencies against known vulnerability databases.

![pip-audit Dependency Scan](docs/screenshots/devsecops-pip-audit.png)

## GitHub Actions Workflow

Stored in `.github/workflows/security-check.yml` — supports repeatable security checks via version-controlled automation.

---

# 📋 Compliance Support and Audit Evidence

Demonstrates compliance support through automated checks, logging, monitoring, and preserved evidence.

Script: `devsecops/compliance_check.py`

Reports generated:
```text
devsecops/compliance_report.txt
devsecops/bandit_report.txt
devsecops/pip_audit_report.txt
```

Verifies presence of: security scan reports, Suricata rules, saved AI models, resilience logs, monitoring evidence, documentation, and licensing information.

![DevSecOps Compliance Check](docs/screenshots/devsecops-compliance-check.png)

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

> **Important:** This prototype demonstrates compliance support and audit readiness only — it does not claim formal certification against NERC CIP, IEC 62351, ISA/IEC 62443, or any other industrial standard.

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

Developed as an educational prototype for the EduQual Level 6 Diploma in Artificial Intelligence Operations. Current limitations:

- Runs on a single Ubuntu VM.
- Grid behaviour is simulated via the IEEE 13-Bus OpenDSS model.
- Conpot simulates a PLC rather than real industrial hardware.
- Energy-theft detection uses synthetic smart-meter data.
- AI models are trained on prototype datasets.
- Intended for lab demonstration and research only.

---

# 🚀 Future Improvements

Could be extended with:

- Apache Kafka for real-time event streaming
- Apache Spark for distributed AI analytics
- Kubernetes orchestration
- MQTT integration for IoT smart meters
- IEC 61850 protocol support
- Digital Twin integration
- Real PLC and RTU connectivity
- SIEM integration (e.g., Splunk, Microsoft Sentinel)
- Cloud-native deployment
- High-availability monitoring architecture

---

# 🏢 Enterprise Deployment Scenario

In an enterprise environment, the prototype could be deployed with:

- Multiple substations over secure VPNs
- Redundant SCADA servers
- Central Security Operations Centre (SOC)
- Distributed AI inference services
- Central SIEM platform
- Redundant Prometheus and Grafana servers
- Secure API gateways
- Backup disaster recovery infrastructure

This repository demonstrates the core concepts, not a production-ready implementation.

---

# 📖 Lessons Learned

- AI is more effective combined with traditional intrusion detection.
- Simulated industrial environments allow safe cyber-security experimentation.
- Continuous monitoring significantly improves operational visibility.
- Docker simplifies deployment and reproducibility.
- DevSecOps practices improve project quality and audit readiness.

---

# 📚 References

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

Developed as part of the EduQual Level 6 Diploma in Artificial Intelligence Operations. Thanks to the maintainers of the open-source tools and frameworks that made this prototype possible.

---

# 📄 License

Released under the **MIT License** — see the `LICENSE` file for details.

---

# ⭐ Final Project Summary

An end-to-end AI-driven smart-grid cyber-security prototype integrating smart-grid simulation, SCADA/ICS security, Modbus attack simulation, AI-based anomaly detection, energy-theft detection, grid resilience automation, real-time monitoring, Docker deployment, DevSecOps practices, and compliance-support automation.

Though built as an educational prototype, it demonstrates the integration of multiple technologies commonly used in modern cyber-physical power-system security research.
