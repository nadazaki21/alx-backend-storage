#!/usr/bin/env python3
""" Exercise file for mandatory tasks  """

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    """Class for cache"""

    def __init__(self) -> None:
        """Initialize cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        random_id = str(uuid4())
        self.__redis.set(random_id, data)
        return random_id
