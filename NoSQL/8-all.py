#!/usr/bin/env python3
""" Function that lists all documents in a collection """
import pymongo

def list_all(mongo_collection):
    """Return list of all documents in the collection, or empty list if none"""
    return list(mongo_collection.find())
