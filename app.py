from flask import Flask, jsonify
from pyngrok import ngrok
import random
from datetime import datetime

app = Flask(__name__)

ALERT_TYPES = [
    {"type": "High Signal Loss",     "severity": "CRITICAL"},
    {"type": "BTS Down",             "severity": "CRITICAL"},
    {"type": "High Packet Loss",     "severity": "HIGH"},
    {"type": "Microwave Link Fault", "severity": "HIGH"},
    {"type": "Power Issue",          "severity": "MEDIUM"},
    {"type": "High Latency",         "severity": "LOW"},
]

SITES = ["Site-Cairo-01", "Site-Alex-02", "Site-Giza-03", "Site-Aswan-04"]

@app.route('/alert', methods=['GET'])
def get_alert():
    alert = random.choice(ALERT_TYPES)
    site  = random.choice(SITES)
    return jsonify({
        "site":      site,
        "type":      alert["type"],
        "severity":  alert["severity"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "value":     round(random.uniform(60, 100), 2)
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})

if __name__ == '__main__':
    tunnel = ngrok.connect(5000)
    print(f"\n🌍 Public URL: {tunnel.public_url}/alert\n")
    app.run(debug=False, port=5000)