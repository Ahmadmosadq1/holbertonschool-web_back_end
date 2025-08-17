#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total logs
    print("{} logs".format(collection.count()))

    # Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Status check
    status_check = collection.count({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
