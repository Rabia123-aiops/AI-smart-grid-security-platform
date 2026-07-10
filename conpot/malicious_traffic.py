# scada/malicious_traffic.py
# Simulates an attack: rapid unauthorized write attempts to the PLC

from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient('127.0.0.1', port=502, timeout=5)
client.connect()

print("Simulating malicious/attack traffic (rapid unauthorized writes)...")
for i in range(30):
    result = client.write_register(0, 9999, slave=1)
    print("Malicious write attempt " + str(i) + " sent to PLC")
    time.sleep(0.05)

client.close()
print("Attack simulation complete.")
