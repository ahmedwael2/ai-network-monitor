import random
import time
import requests
from datetime import datetime

# ── أنواع الـ alerts اللي ممكن تحصل في الشبكة ──
ALERT_TYPES = [
    {"type": "High Signal Loss",      "severity": "CRITICAL"},
    {"type": "BTS Down",              "severity": "CRITICAL"},
    {"type": "High Packet Loss",      "severity": "HIGH"},
    {"type": "Microwave Link Fault",  "severity": "HIGH"},
    {"type": "Power Issue",           "severity": "MEDIUM"},
    {"type": "High Latency",          "severity": "LOW"},
]

SITES = ["Site-Cairo-01", "Site-Alex-02", "Site-Giza-03", "Site-Aswan-04"]

def generate_alert():
    alert = random.choice(ALERT_TYPES)
    site  = random.choice(SITES)
    return {
        "site":      site,
        "type":      alert["type"],
        "severity":  alert["severity"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "value":     round(random.uniform(60, 100), 2)
    }

def send_alert(alert):
    print(f"[{alert['severity']}] {alert['site']} ← {alert['type']} ({alert['value']}%)")

# ── بيعمل simulate لـ alerts كل 5 ثواني ──
print(" Network Monitor Started...")
while True:
    alert = generate_alert()
    send_alert(alert)
    time.sleep(5)
    
