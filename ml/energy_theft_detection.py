# ml/energy_theft_detection.py
# Phase 4: Synthetic smart-meter data + theft detection model

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import joblib

rng = np.random.default_rng(7)
n_customers = 500

normal_consumption = rng.normal(300, 40, n_customers)
normal_billed = normal_consumption + rng.normal(0, 5, n_customers)

theft_mask = rng.random(n_customers) < 0.08
billed = normal_billed.copy()
billed[theft_mask] = normal_consumption[theft_mask] * rng.uniform(0.3, 0.6, theft_mask.sum())

df = pd.DataFrame({
    "actual_consumption_kwh": normal_consumption,
    "billed_kwh": billed,
    "is_theft": theft_mask.astype(int)
})
df["consumption_gap"] = df["actual_consumption_kwh"] - df["billed_kwh"]
df.to_csv("smart_meter_data.csv", index=False)
print("Generated synthetic smart-meter dataset:", len(df), "customers,", theft_mask.sum(), "theft cases")

X = df[["actual_consumption_kwh", "billed_kwh", "consumption_gap"]].values
model = IsolationForest(contamination=0.08, random_state=42)
model.fit(X)
preds = model.predict(X)
detected_theft = (preds == -1).astype(int)

print("\nDetected", detected_theft.sum(), "potential theft cases")
print(classification_report(df["is_theft"], detected_theft, zero_division=0))

joblib.dump(model, "energy_theft_model.pkl")
print("Model saved: energy_theft_model.pkl")
