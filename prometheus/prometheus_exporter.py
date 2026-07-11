# prometheus/prometheus_exporter.py
# Exposes live grid readings and anomaly flags in Prometheus format
# so Grafana can visualize them.

from prometheus_client import start_http_server, Gauge
import time
import random

voltage_gauge = Gauge('grid_voltage', 'Current grid voltage reading')
current_gauge = Gauge('grid_current', 'Current grid current reading')
anomaly_gauge = Gauge('grid_anomaly_detected', 'Anomaly detection flag (1=anomaly, 0=normal)')

start_http_server(9100)
print("Prometheus exporter running on port 9100 - metrics at http://localhost:9100/metrics")

step = 0
while True:
    anomaly_burst = (step % 40) in range(35, 40)
    voltage = 230 + random.uniform(-2, 2)
    current = 210 + random.uniform(-3, 3)
    if anomaly_burst:
        voltage += random.uniform(20, 40)
        current += random.uniform(15, 30)

    voltage_gauge.set(voltage)
    current_gauge.set(current)
    anomaly_gauge.set(1 if anomaly_burst else 0)

    print("Step " + str(step) + ": V=" + str(round(voltage, 2)) + " I=" + str(round(current, 2)) + " Anomaly=" + str(anomaly_burst))
    step += 1
    time.sleep(5)
