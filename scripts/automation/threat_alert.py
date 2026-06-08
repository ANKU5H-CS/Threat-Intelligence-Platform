print("=" * 50)
print("Threat Intelligence Platform")
print("Threat Alert System")
print("=" * 50)

threats = [
    {"name": "Malware", "severity": "High"},
    {"name": "Phishing", "severity": "Medium"},
    {"name": "Ransomware", "severity": "Critical"}
]

for threat in threats:
    if threat["severity"] in ["High", "Critical"]:
        print(f"ALERT: {threat['name']} detected ({threat['severity']})")
