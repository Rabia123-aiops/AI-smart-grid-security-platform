# opendss/plot_grid.py
# Visualize grid health
# Reads grid_readings.csv and saves a graph as grid_health_graph.png

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("grid_readings.csv")

fig, axs = plt.subplots(2, 1, figsize=(10, 6))

axs[0].plot(df["voltage"], color="blue", label="Voltage")
axs[0].set_title("Grid Voltage Over Time")
axs[0].set_ylabel("Voltage (V)")

axs[1].plot(df["current"], color="orange", label="Current")
axs[1].set_title("Grid Current Over Time")
axs[1].set_ylabel("Current (A)")
axs[1].set_xlabel("Reading Number")

anomalies = df[df["is_anomaly"] == True]
if not anomalies.empty:
    axs[0].scatter(anomalies.index, anomalies["voltage"], color="red", label="Anomaly", zorder=5)
    axs[1].scatter(anomalies.index, anomalies["current"], color="red", label="Anomaly", zorder=5)

axs[0].legend()
axs[1].legend()
plt.tight_layout()
plt.savefig("grid_health_graph.png")
print("Graph saved as grid_health_graph.png")
