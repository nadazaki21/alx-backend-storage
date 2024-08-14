#!/usr/bin/env python3

from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps

"""
    Writing strings to Redis.
"""


class Cache:
    """
    Cache class.
    """

    def __init__(self):
        """
        Initialize the cache.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache.
        """
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Get data from redis"""
        data = self._redis.get(key)
        if data:
            if fn:
                return fn(data)
        # return None
        return None

    def get_str(self, data: Union[str, bytes, int, float]) -> str:
        """Get string from redis"""
        return data.decode('utf-8')

    def get_int(self, data: Union[str, bytes, int, float]) -> int:
        """Get int from redis"""
        return data.decode('utf-8')
