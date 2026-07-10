# ml/ml_report.py
# Phase 4: Generate visual confusion matrix for presentation

import pandas as pd
import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

df = pd.read_csv("smart_meter_data.csv")
model = joblib.load("energy_theft_model.pkl")

X = df[["actual_consumption_kwh", "billed_kwh", "consumption_gap"]].values
preds = model.predict(X)
detected = (preds == -1).astype(int)

cm = confusion_matrix(df["is_theft"], detected)

fig, ax = plt.subplots(figsize=(5, 4))
ax.imshow(cm, cmap="Blues")
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["Normal", "Theft"])
ax.set_yticklabels(["Normal", "Theft"])
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title("Energy Theft Detection - Confusion Matrix")
for i in range(2):
    for j in range(2):
        ax.text(j, i, str(cm[i, j]), ha="center", va="center", color="black", fontsize=14)
plt.tight_layout()
plt.savefig("energy_theft_confusion_matrix.png")
print("Saved energy_theft_confusion_matrix.png")
