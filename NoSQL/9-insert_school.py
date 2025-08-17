#!/usr/bin/env python3
""" Function that inserts a new document in a collection """
import pymongo

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
        **kwargs: fields to include in the new document
    Returns:
        The new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
