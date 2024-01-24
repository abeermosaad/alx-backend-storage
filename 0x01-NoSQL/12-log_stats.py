#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('127.0.01', 27017)
    collection = client.logs.nginx

    print(f"{collection.estimated_document_count()} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        query = {'method': method}
        count = collection.count_documents(query)
        print(f"\tmethod {method}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status} status check')
