#!/usr/bin/env python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
        list: A list of all documents in the collection. An empty list if no documents.
    """
    return (mongo_collection.find())
