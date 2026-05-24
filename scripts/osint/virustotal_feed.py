import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")

url = "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8"

headers = {
    "x-apikey": API_KEY
}

response = requests.get(url, headers=headers)

print(response.json())

with open("logs/virustotal_log.txt", "w") as file:
    file.write(str(response.json()))
