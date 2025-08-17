#!/usr/bin/env python3
""" Function that changes all topics of a school document based on the name """
import pymongo

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name (str): the school name to update
        topics (list of str): list of topics to set
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
