# devsecops/compliance_check.py
# Automated compliance checklist inspired by NERC CIP / IEC 62351 requirements

import os
from datetime import datetime

CHECKS = []

def check(name, condition):
    status = "PASS" if condition else "FAIL"
    CHECKS.append((name, status))
    print("[" + status + "] " + name)


def run_checks():
    print("Running compliance checklist...\n")

    check("Suricata rules file exists", os.path.exists("../suricata/local.rules"))
    check(".gitignore exists (prevents secrets from being committed)", os.path.exists("../.gitignore"))
    check("LICENSE file exists", os.path.exists("../LICENSE"))
    check("README documentation exists", os.path.exists("../README.md"))
    check("ML models are saved (audit trail of trained models)", os.path.exists("../ml/isolation_forest_model.pkl"))
    check("Resilience event logging is configured", os.path.exists("../resilience/resilience_engine.py"))
    check("Bandit security scan report exists", os.path.exists("bandit_report.txt"))
    check("Dependency vulnerability report exists", os.path.exists("pip_audit_report.txt"))

    passed = sum(1 for _, s in CHECKS if s == "PASS")
    total = len(CHECKS)
    print("\nCompliance Summary: " + str(passed) + "/" + str(total) + " checks passed")

    with open("compliance_report.txt", "w") as f:
        f.write("Compliance Report - Generated " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("=" * 50 + "\n")
        for name, status in CHECKS:
            f.write("[" + status + "] " + name + "\n")
        f.write("\nSummary: " + str(passed) + "/" + str(total) + " checks passed\n")
    print("Saved compliance_report.txt")


if __name__ == "__main__":
    run_checks()
