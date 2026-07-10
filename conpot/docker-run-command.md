# Conpot SCADA Honeypot Setup

## Run Command

sudo docker run -it -p 502:5020 -p 161:16100/udp -p 80:8800 --name conpot_lab honeynet/conpot

## Purpose

Simulates a real industrial PLC (Modbus/SCADA device) to test attack detection.
