# ml/lstm_anomaly_detection.py
# LSTM Autoencoder for time-series anomaly detection

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, RepeatVector, TimeDistributed, Dense

tf.config.threading.set_intra_op_parallelism_threads(2)
tf.config.threading.set_inter_op_parallelism_threads(2)

SEQUENCE_LENGTH = 10
LSTM_UNITS = 32
EPOCHS = 20
BATCH_SIZE = 16
ANOMALY_PERCENTILE = 95


def load_data(csv_path="../opendss/grid_readings.csv"):
    df = pd.read_csv(csv_path)
    print("Loaded " + str(len(df)) + " rows from " + csv_path)
    return df


def create_sequences(data, seq_len):
    sequences = []
    for i in range(len(data) - seq_len):
        sequences.append(data[i:i + seq_len])
    return np.array(sequences)


def build_lstm_autoencoder(seq_len, n_features):
    inputs = Input(shape=(seq_len, n_features))
    encoded = LSTM(LSTM_UNITS, activation="relu")(inputs)
    repeated = RepeatVector(seq_len)(encoded)
    decoded = LSTM(LSTM_UNITS, activation="relu", return_sequences=True)(repeated)
    outputs = TimeDistributed(Dense(n_features))(decoded)
    model = Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mse")
    return model


def main():
    df = load_data()
    features = df[["voltage", "current"]].values
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(features)

    sequences = create_sequences(scaled, SEQUENCE_LENGTH)
    print("Created " + str(sequences.shape[0]) + " sequences")

    split = int(len(sequences) * 0.9)
    train_seqs = sequences[:split]
    test_seqs = sequences

    model = build_lstm_autoencoder(SEQUENCE_LENGTH, features.shape[1])
    print("Training LSTM Autoencoder...")
    model.fit(train_seqs, train_seqs, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=0.1, verbose=1)

    reconstructed = model.predict(test_seqs, verbose=0)
    mse = np.mean(np.mean(np.square(test_seqs - reconstructed), axis=1), axis=1)
    threshold = np.percentile(mse, ANOMALY_PERCENTILE)
    anomalies = mse > threshold

    print("\n===== LSTM ANOMALY DETECTION RESULTS =====")
    print("Threshold: " + str(threshold))
    print("Total sequences: " + str(len(mse)))
    print("Anomalies detected: " + str(anomalies.sum()))

    results_df = pd.DataFrame({
        "sequence_index": np.arange(len(mse)),
        "reconstruction_error": mse,
        "is_anomaly": anomalies,
    })
    results_df.to_csv("lstm_anomaly_results.csv", index=False)

    model.save("lstm_autoencoder_model.keras")
    joblib.dump(scaler, "lstm_scaler.pkl")
    print("Saved model and results.")


if __name__ == "__main__":
    main()
