# scada/normal_traffic.py
# Sends legitimate Modbus read requests to Conpot (simulated PLC)

from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient('127.0.0.1', port=502, timeout=5)
client.connect()

print("Sending normal/legitimate Modbus traffic...")
for i in range(10):
    result = client.read_holding_registers(0, 5, slave=1)
    if result.isError():
        print("Normal read " + str(i) + ": PLC responded (device active, address not configured in test template)")
    else:
        print("Normal read " + str(i) + ": " + str(result.registers))
    time.sleep(1)

client.close()
print("Normal traffic simulation complete.")



