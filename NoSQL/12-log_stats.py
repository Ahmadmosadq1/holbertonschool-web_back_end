#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def _count(col, filt):
    """Robust counter that works on both PyMongo 3.x and 4.x."""
    try:
        return col.count_documents(filt)
    except Exception:
        # Fallback for very old environments
        try:
            return col.count(filt)
        except Exception:
            return sum(1 for _ in col.find(filt))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total logs
    print("{} logs".format(_count(collection, {})))

    # Methods breakdown (exact order and tab before each line)
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(method, _count(collection, {"method": method})))

    # Status check
    print("{} status check".format(_count(collection, {"method": "GET", "path": "/status"})))
