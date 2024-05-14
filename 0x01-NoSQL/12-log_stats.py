#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

# Connect to the database
client = MongoClient()
db = client['logs']
collection = db['nginx']

# Get the total number of logs
total_logs = collection.count_documents({})

# Print the total number of logs
print(f"{total_logs} logs")

# Print the methods stats
print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Print the number of GET requests with path=/status
get_status_count = collection.count_documents(
    {"method": "GET", "path": "/status"})
print(f"{get_status_count} status check")
