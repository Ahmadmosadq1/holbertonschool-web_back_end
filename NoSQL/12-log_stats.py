#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total logs
    total = collection.count_documents({})
    print(f"{total} logs")

    # Methods breakdown
    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        cnt = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {cnt}")

    # Status check: method=GET and path=/status
    status_cnt = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_cnt} status check")
