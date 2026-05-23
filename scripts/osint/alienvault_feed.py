import requests
import json
from datetime import datetime

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("[+] Threat Feed Retrieved Successfully")
        print(json.dumps(data[:5], indent=2))

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        log_file = f"logs/threat_feed_{timestamp}.log"

        with open(log_file, "w") as file:
            file.write(json.dumps(data, indent=2))

        print(f"[+] Log Saved: {log_file}")

    else:
        print(f"[-] Failed with Status Code: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")
