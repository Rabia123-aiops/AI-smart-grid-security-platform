# opendss/grid_model.py
# Grid Simulation Layer
# This script loads a simulated power grid, reads voltage/current values,
# injects occasional anomalies, and saves everything to a CSV file.

import opendssdirect as dss
import csv
import os
import random
import time
from datetime import datetime

CSV_FILE = "grid_readings.csv"


def load_circuit():
    dss.Text.Command("Clear")
    dss.Text.Command("Compile IEEE13Nodeckt.dss")
    print("Circuit loaded successfully!")


def get_readings():
    dss.Solution.Solve()

    voltages_pu = dss.Circuit.AllBusMagPu()
    avg_voltage = (sum(voltages_pu) / len(voltages_pu) * 230) if voltages_pu else 0

    total_current = 0
    count = 0
    for elem in dss.Circuit.AllElementNames():
        dss.Circuit.SetActiveElement(elem)
        mag_ang = dss.CktElement.CurrentsMagAng()
        mags = mag_ang[0::2]
        if mags:
            total_current += sum(abs(m) for m in mags)
            count += len(mags)
    avg_current = (total_current / count) if count else 0

    avg_voltage += random.uniform(-2, 2)
    avg_current += random.uniform(-3, 3)

    return avg_voltage, avg_current


def inject_anomaly(voltage, current, step):
    is_anomaly = (step % 40) in range(35, 40)
    if is_anomaly:
        voltage += random.uniform(20, 40)
        current += random.uniform(15, 30)
    return voltage, current, is_anomaly


def save_reading(voltage, current, is_anomaly):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "voltage", "current", "is_anomaly"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            round(voltage, 2),
            round(current, 2),
            is_anomaly,
        ])


def main():
    load_circuit()
    step = 0
    print("Starting live grid simulation... Press Ctrl+C to stop.")
    try:
        while True:
            v, c = get_readings()
            v, c, anomaly = inject_anomaly(v, c, step)
            save_reading(v, c, anomaly)
            print("Step " + str(step) + ": Voltage=" + str(round(v,2)) + "V, Current=" + str(round(c,2)) + "A, Anomaly=" + str(anomaly))
            step += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("Simulation stopped. " + str(step) + " readings saved to " + CSV_FILE)


if __name__ == "__main__":
    main()
