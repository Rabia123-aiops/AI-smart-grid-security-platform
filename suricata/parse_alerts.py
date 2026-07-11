# suricata/parse_alerts.py
# Reads Suricata's eve.json log and summarizes detected alerts

import json

LOG_FILE = "/var/log/suricata/eve.json"

def parse_alerts():
    alert_count = 0
    alert_types = {}
    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                event = json.loads(line)
                if event.get("event_type") == "alert":
                    alert_count += 1
                    msg = event["alert"]["signature"]
                    alert_types[msg] = alert_types.get(msg, 0) + 1
            except (json.JSONDecodeError, KeyError):
                continue

    print("Total alerts detected: " + str(alert_count))
    print("Breakdown by type:")
    for msg, count in alert_types.items():
        print("  - " + msg + ": " + str(count))

if __name__ == "__main__":
    parse_alerts()
