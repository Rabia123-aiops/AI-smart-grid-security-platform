# resilience/resilience_engine.py
# Phase 5: Grid Resilience & Automated Recovery (Steps 31-35)
# Reads live grid readings and automatically reacts to problems:
# load shedding, fault isolation, self-healing, predictive maintenance

import pandas as pd
import numpy as np
from datetime import datetime

VOLTAGE_THRESHOLD_HIGH = 250
CURRENT_THRESHOLD_HIGH = 225
LOG_FILE = "resilience_events.log"


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = "[" + timestamp + "] " + message
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


# Step 31: Automated load shedding
def load_shedding_check(voltage, current, step):
    if voltage > VOLTAGE_THRESHOLD_HIGH or current > CURRENT_THRESHOLD_HIGH:
        log_event("Step " + str(step) + ": THRESHOLD EXCEEDED (V=" + str(round(voltage, 2)) +
                   ", I=" + str(round(current, 2)) + ") -> Load shedding triggered, disconnecting non-critical load")
        return True
    return False


# Step 32: Fault detection and isolation
def fault_isolation(voltage, current, step, prev_current):
    spike = abs(current - prev_current)
    if spike > 15:
        log_event("Step " + str(step) + ": FAULT DETECTED - sudden current spike of " +
                   str(round(spike, 2)) + "A -> Isolating affected section")
        return True
    return False


# Step 33: Self-healing (backup feeder activation)
def self_healing(step, isolated):
    if isolated:
        log_event("Step " + str(step) + ": SELF-HEALING - activating backup feeder path to restore power")


# Step 34: Predictive maintenance (trend-based)
def predictive_maintenance(readings, step):
    if len(readings) >= 10:
        recent = readings[-10:]
        trend = np.polyfit(range(len(recent)), recent, 1)[0]
        if abs(trend) > 2.0:
            log_event("Step " + str(step) + ": PREDICTIVE MAINTENANCE ALERT - equipment degradation trend detected (slope=" +
                       str(round(trend, 3)) + ")")


# Step 35: Main loop - processes all readings and logs every event
def main():
    df = pd.read_csv("../opendss/grid_readings.csv")
    print("Loaded " + str(len(df)) + " readings from grid_readings.csv")

    current_history = []
    prev_current = df["current"].iloc[0]

    for step, row in df.iterrows():
        v, c = row["voltage"], row["current"]
        isolated = fault_isolation(v, c, step, prev_current)
        load_shedding_check(v, c, step)
        self_healing(step, isolated)
        current_history.append(c)
        predictive_maintenance(current_history, step)
        prev_current = c

    print("\nSimulation complete. Full history saved in resilience_events.log")


if __name__ == "__main__":
    main()
