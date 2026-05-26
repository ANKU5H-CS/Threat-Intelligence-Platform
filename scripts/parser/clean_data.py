from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["tip_project"]

collection = db["threat_feeds"]

seen = set()

cleaned = []

for data in collection.find():

    ip = data.get("indicator")

    if ip not in seen:
        seen.add(ip)
        cleaned.append(ip)

print("Cleaned Data:\n")

for i in cleaned:
    print(i)
