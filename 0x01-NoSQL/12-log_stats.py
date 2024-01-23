#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

client = MongoClient('127.0.01', 27017)
collection = client.logs.nginx

print(f"{collection.estimated_document_count()} logs")
print("Methods:")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    print(f"method {method}: {collection.count_documents({'method': method})}")

print(f'{collection.count_documents({"method": "GET", "path": "/status"})} status check')
