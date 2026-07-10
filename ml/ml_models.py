# ml/ml_models.py
# Phase 4: Isolation Forest (unsupervised) + Random Forest (supervised)
# anomaly detection on grid sensor data

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("../opendss/grid_readings.csv")
print("Loaded grid_readings.csv:", len(df), "rows")

X = df[["voltage", "current"]].values
y = df["is_anomaly"].astype(int).values

iso = IsolationForest(contamination=0.1, random_state=42)
iso.fit(X)
preds = iso.predict(X)
iso_anomalies = (preds == -1).astype(int)
print("\nIsolation Forest detected " + str(iso_anomalies.sum()) + " anomalies out of " + str(len(X)))

if y.sum() > 1:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    print("\nRandom Forest classification report:")
    print(classification_report(y_test, y_pred, zero_division=0))
    joblib.dump(rf, "random_forest_model.pkl")
else:
    print("Not enough anomaly examples yet")

joblib.dump(iso, "isolation_forest_model.pkl")
print("\nModels saved: isolation_forest_model.pkl, random_forest_model.pkl")
