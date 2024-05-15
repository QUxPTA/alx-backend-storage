#!/usr/bin/env python3
"""
Redis module
"""

import uuid
import redis
from typing import Union


class Cache:
    """
    A simple cache class using Redis as the backend.
    """

    def __init__(self):
        """
        Initialize the cache by creating a Redis client
        and flushing the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache and return a unique key.

        Args:
            data: The data to be stored in the cache.
            Can be a string, bytes, integer, or float.

        Returns:
            A unique string key that can be used to retrieve the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
