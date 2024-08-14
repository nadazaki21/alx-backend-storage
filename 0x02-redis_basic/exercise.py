#!/usr/bin/env python3

from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps

""" Exercise file for mandatory tasks  """


class Cache:
    """Class for cache"""

    def __init__(self):
        """Initialize cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        random_id = str(uuid4())
        self.__redis.set(random_id, data)
        return random_id
