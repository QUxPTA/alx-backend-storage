#!/usr/bin/env python3
"""
Redis module
"""

import uuid
from functools import wraps
from typing import Union, Callable, Any
import redis


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Append input arguments to the input list
        self._redis.rpush(input_key, str(args))

        # Execute the wrapped function to retrieve the output
        output = method(self, *args, **kwargs)

        # Append the output value to the output list
        self._redis.rpush(output_key, output)

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable, cache: 'Cache') -> None:
    """
    Display the history of calls for a particular function.

    Args:
        method: The function for which the history of calls will be displayed.
        cache: An instance of the Cache class to access Redis.
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    print(f"History of calls for function {method.__qualname__}:")
    for input_args, output in zip(inputs, outputs):
        print(f"Input: {input_args.decode()}, Output: {output.decode()}")


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

    @call_history
    @count_calls
    def store(self, data: str) -> str:
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

    def get(self, key: str, fn: Callable = None) -> Any:
        """
        Retrieve data from the cache using the provided key.

        Args:
            key: The key used to retrieve the data from the cache.
            fn: An optional callable function to convert the retrieved data.
                If provided, the function will be applied to retrieved data.

        Returns:
            The retrieved data from the cache.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes]:
        """
        Retrieve a string value from the cache using the provided key.

        Args:
            key: The key used to retrieve the data from the cache.

        Returns:
            The retrieved string value from the cache.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, bytes]:
        """
        Retrieve an integer value from the cache using the provided key.

        Args:
            key: The key used to retrieve the data from the cache.

        Returns:
            The retrieved integer value from the cache.
        """
        return self.get(key, fn=int)
