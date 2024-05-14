#!/usr/bin/env python3
"""
Returns list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.
        topic (str): The topic searched.

    Returns:
        list: A list of school documents that have the specified topic.
    """
    return (mongo_collection.find({"topics": topic}))
