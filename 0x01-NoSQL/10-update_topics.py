#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics approached in the school.

    Returns:
        int: The number of updated documents.
    """
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})
    return result.modified_count
