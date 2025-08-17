#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total logs
    print("{} logs".format(collection.count()))

    # Methods breakdown
    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(m, collection.count({"method": m})))

    # Status check: method=GET and path=/status
    print("{} status check".format(collection.count({"method": "GET", "path": "/status"})))
