from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["threat_intelligence"]

collection = db["threat_feeds"]

data = {
    "ip": "8.8.8.8",
    "threat": "suspicious",
    "source": "VirusTotal"
}

collection.insert_one(data)

print("Data inserted successfully")
