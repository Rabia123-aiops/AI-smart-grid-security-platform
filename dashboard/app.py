# dashboard/app.py
"""
Live Monitoring Dashboard for the Smart Grid Security Platform.

This application integrates an Isolation Forest model and an LSTM
autoencoder into a browser-based dashboard. A background thread
simulates live grid readings, performs anomaly detection, and updates
the dashboard with measurements and alerts.
"""

import os
import time
import threading
from collections import deque
from datetime import datetime

import joblib
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template_string
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Input, LSTM, RepeatVector, TimeDistributed
from tensorflow.keras.models import Model, load_model


# Limit TensorFlow CPU thread usage.
tf.config.threading.set_intra_op_parallelism_threads(2)
tf.config.threading.set_inter_op_parallelism_threads(2)


SEQUENCE_LENGTH = 10
HISTORY_MAX = 100
UPDATE_INTERVAL = 2
ANOMALY_THRESHOLD_PERCENTILE = 95

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "ml",
    "lstm_autoencoder_model.keras",
)
SCALER_PATH = os.path.join(
    BASE_DIR,
    "lstm_scaler.pkl",
)


app = Flask(__name__)

lock = threading.Lock()
history = deque(maxlen=HISTORY_MAX)
alerts = deque(maxlen=50)
reconstruction_errors_baseline = []
raw_window = deque(maxlen=SEQUENCE_LENGTH)


def build_lstm_autoencoder(seq_len, n_features):
    """Create and compile an LSTM autoencoder model."""

    inputs = Input(shape=(seq_len, n_features))
    encoded = LSTM(32, activation="relu")(inputs)
    repeated = RepeatVector(seq_len)(encoded)
    decoded = LSTM(
        32,
        activation="relu",
        return_sequences=True,
    )(repeated)
    outputs = TimeDistributed(Dense(n_features))(decoded)

    model = Model(inputs, outputs)
    model.compile(
        optimizer="adam",
        loss="mse",
    )

    return model


def train_quick_lstm():
    """Train a small demonstration LSTM model when saved files are unavailable."""

    rng = np.random.default_rng(1)
    sample_count = 1000

    voltage = 230 + rng.normal(0, 2, sample_count)
    current = 10 + rng.normal(0, 0.5, sample_count)

    training_data = np.column_stack([
        voltage,
        current,
    ])

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(training_data)

    sequences = np.array([
        scaled_data[index:index + SEQUENCE_LENGTH]
        for index in range(len(scaled_data) - SEQUENCE_LENGTH)
    ])

    model = build_lstm_autoencoder(
        SEQUENCE_LENGTH,
        2,
    )

    model.fit(
        sequences,
        sequences,
        epochs=8,
        batch_size=16,
        verbose=0,
    )

    return model, scaler


def load_or_train():
    """Load the saved LSTM model and scaler, or train demonstration models."""

    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        print("Loading saved LSTM model...")

        model = load_model(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

    else:
        print("Saved model or scaler not found.")
        print("Training a small demonstration LSTM model...")

        model, scaler = train_quick_lstm()

    return model, scaler


print("Initializing models, please wait...")

lstm_model, lstm_scaler = load_or_train()

iso_forest = IsolationForest(
    contamination=0.05,
    random_state=42,
)

warmup_data = np.column_stack([
    230 + np.random.normal(0, 2, 300),
    10 + np.random.normal(0, 0.5, 300),
])

iso_forest.fit(warmup_data)

print("Models ready. Starting live simulation...")


def generate_reading(step):
    """Generate a simulated voltage and current reading."""

    anomaly_burst = (step % 40) in range(35, 40)

    voltage = 230 + np.random.normal(0, 2)
    current = 10 + np.random.normal(0, 0.5)

    if anomaly_burst:
        voltage += np.random.normal(35, 5)
        current += np.random.normal(12, 3)

    return (
        float(voltage),
        float(current),
        bool(anomaly_burst),
    )


def live_loop():
    """Generate readings continuously and evaluate them using both models."""

    step = 0

    while True:
        voltage, current, injected_anomaly = generate_reading(step)
        timestamp = datetime.now().strftime("%H:%M:%S")

        isolation_prediction = iso_forest.predict([
            [voltage, current]
        ])[0]

        isolation_anomaly = bool(
            int(isolation_prediction) == -1
        )

        raw_window.append([
            voltage,
            current,
        ])

        lstm_anomaly = False
        lstm_error = 0.0

        if len(raw_window) == SEQUENCE_LENGTH:
            window_array = np.asarray(
                raw_window,
                dtype=np.float64,
            )

            scaled_window = lstm_scaler.transform(
                window_array
            )

            sequence = scaled_window.reshape(
                1,
                SEQUENCE_LENGTH,
                2,
            )

            reconstructed = lstm_model.predict(
                sequence,
                verbose=0,
            )

            lstm_error = float(
                np.mean(
                    (sequence - reconstructed) ** 2
                )
            )

            reconstruction_errors_baseline.append(
                float(lstm_error)
            )

            if len(reconstruction_errors_baseline) > 20:
                threshold = float(
                    np.percentile(
                        reconstruction_errors_baseline,
                        ANOMALY_THRESHOLD_PERCENTILE,
                    )
                )

                lstm_anomaly = bool(
                    lstm_error > threshold
                )

        entry = {
            "timestamp": str(timestamp),
            "voltage": float(round(voltage, 2)),
            "current": float(round(current, 2)),
            "if_anomaly": bool(isolation_anomaly),
            "lstm_anomaly": bool(lstm_anomaly),
            "lstm_error": float(round(lstm_error, 6)),
            "injected_anomaly": bool(injected_anomaly),
        }

        with lock:
            history.append(entry)

            if isolation_anomaly or lstm_anomaly:
                detectors = []

                if isolation_anomaly:
                    detectors.append("Isolation Forest")

                if lstm_anomaly:
                    detectors.append("LSTM Autoencoder")

                alert_message = (
                    f"[{timestamp}] ANOMALY - "
                    f"Voltage={entry['voltage']}V, "
                    f"Current={entry['current']}A - "
                    f"Detected by: {', '.join(detectors)}"
                )

                alerts.appendleft(
                    str(alert_message)
                )

        step += 1
        time.sleep(UPDATE_INTERVAL)


simulation_thread = threading.Thread(
    target=live_loop,
    daemon=True,
)

simulation_thread.start()


DASHBOARD_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1"
  >
  <title>Smart Grid Security Platform - Live Dashboard</title>

  <script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>

  <style>
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      margin: 0;
      padding: 20px;
    }

    h1 {
      color: #38bdf8;
      font-size: 22px;
    }

    .grid {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 20px;
    }

    .card {
      background: #1e293b;
      border-radius: 10px;
      padding: 16px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }

    .stat {
      display: flex;
      justify-content: space-between;
      margin: 8px 0;
      font-size: 14px;
    }

    .stat b {
      color: #38bdf8;
    }

    #alerts {
      max-height: 420px;
      overflow-y: auto;
      font-size: 13px;
    }

    .alert-item {
      background: #7f1d1d;
      color: #fecaca;
      padding: 8px;
      border-radius: 6px;
      margin-bottom: 6px;
    }

    .status-dot {
      height: 10px;
      width: 10px;
      border-radius: 50%;
      display: inline-block;
      margin-right: 6px;
    }

    .green {
      background: #22c55e;
    }

    .red {
      background: #ef4444;
    }

    @media (max-width: 850px) {
      .grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>

<body>
  <h1>Smart Grid Security Platform - Live Monitoring</h1>

  <div class="grid">
    <div class="card">
      <canvas id="gridChart" height="110"></canvas>

      <div class="stat">
        <span>
          <span
            class="status-dot green"
            id="ifDot"
          ></span>
          Isolation Forest Status
        </span>

        <b id="ifStatus">Normal</b>
      </div>

      <div class="stat">
        <span>
          <span
            class="status-dot green"
            id="lstmDot"
          ></span>
          LSTM Autoencoder Status
        </span>

        <b id="lstmStatus">Normal</b>
      </div>

      <div class="stat">
        <span>Latest Voltage</span>
        <b id="latestVoltage">--</b>
      </div>

      <div class="stat">
        <span>Latest Current</span>
        <b id="latestCurrent">--</b>
      </div>

      <div class="stat">
        <span>LSTM Reconstruction Error</span>
        <b id="lstmError">--</b>
      </div>
    </div>

    <div class="card">
      <h3 style="margin-top: 0;">Live Alerts</h3>
      <div id="alerts">No alerts yet...</div>
    </div>
  </div>

<script>
const context = document
  .getElementById("gridChart")
  .getContext("2d");

const chart = new Chart(context, {
  type: "line",

  data: {
    labels: [],

    datasets: [
      {
        label: "Voltage (V)",
        data: [],
        borderColor: "#38bdf8",
        tension: 0.3,
        pointRadius: 2
      },
      {
        label: "Current (A)",
        data: [],
        borderColor: "#facc15",
        tension: 0.3,
        pointRadius: 2
      }
    ]
  },

  options: {
    responsive: true,
    animation: false,

    scales: {
      x: {
        ticks: {
          color: "#94a3b8"
        }
      },

      y: {
        ticks: {
          color: "#94a3b8"
        }
      }
    },

    plugins: {
      legend: {
        labels: {
          color: "#e2e8f0"
        }
      }
    }
  }
});


async function refresh() {
  try {
    const response = await fetch("/api/live-data");

    if (!response.ok) {
      throw new Error(
        "Server returned status " + response.status
      );
    }

    const data = await response.json();

    chart.data.labels = data.history.map(
      item => item.timestamp
    );

    chart.data.datasets[0].data = data.history.map(
      item => item.voltage
    );

    chart.data.datasets[1].data = data.history.map(
      item => item.current
    );

    chart.update();

    if (data.history.length > 0) {
      const latest = data.history[
        data.history.length - 1
      ];

      document.getElementById(
        "latestVoltage"
      ).innerText = latest.voltage + " V";

      document.getElementById(
        "latestCurrent"
      ).innerText = latest.current + " A";

      document.getElementById(
        "lstmError"
      ).innerText = latest.lstm_error;

      document.getElementById(
        "ifStatus"
      ).innerText = latest.if_anomaly
        ? "ANOMALY!"
        : "Normal";

      document.getElementById(
        "ifDot"
      ).className = "status-dot " +
        (latest.if_anomaly ? "red" : "green");

      document.getElementById(
        "lstmStatus"
      ).innerText = latest.lstm_anomaly
        ? "ANOMALY!"
        : "Normal";

      document.getElementById(
        "lstmDot"
      ).className = "status-dot " +
        (latest.lstm_anomaly ? "red" : "green");
    }

    const alertsContainer = document.getElementById(
      "alerts"
    );

    if (data.alerts.length === 0) {
      alertsContainer.innerHTML = "No alerts yet...";
    } else {
      alertsContainer.innerHTML = data.alerts
        .map(
          alertText =>
            `<div class="alert-item">${alertText}</div>`
        )
        .join("");
    }

  } catch (error) {
    console.error(
      "Dashboard refresh failed:",
      error
    );
  }
}


setInterval(refresh, 2000);
refresh();
</script>
</body>
</html>
"""


@app.route("/")
def index():
    """Render the live monitoring dashboard."""

    return render_template_string(
        DASHBOARD_HTML
    )


@app.route("/api/live-data")
def live_data():
    """Return JSON-safe monitoring history and alert data."""

    with lock:
        safe_history = [
            {
                "timestamp": str(item["timestamp"]),
                "voltage": float(item["voltage"]),
                "current": float(item["current"]),
                "if_anomaly": bool(item["if_anomaly"]),
                "lstm_anomaly": bool(item["lstm_anomaly"]),
                "lstm_error": float(item["lstm_error"]),
                "injected_anomaly": bool(
                    item.get("injected_anomaly", False)
                ),
            }
            for item in history
        ]

        safe_alerts = [
            str(alert)
            for alert in alerts
        ]

    return jsonify({
        "history": safe_history,
        "alerts": safe_alerts,
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
    )
