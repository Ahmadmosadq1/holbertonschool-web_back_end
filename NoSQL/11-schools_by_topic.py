#!/usr/bin/env python3
""" Function that returns the list of schools having a specific topic """
import pymongo

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for
    Returns:
        List of matching school documents
    """
    return list(mongo_collection.find({ "topics": topic }))
