#!/usr/bin/env python3
""" Exercise file for mandatory tasks  """

import redis
import uuid
from typing import Union


class Cache:
    """Class for cache"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_id = str(uuid.uuid4())
        self.__redis.set(random_id, data)
        return random_id

    def get(self, key: str, fn: callable = None):
        data = self._redis.get(key)
        if data:
            return fn(data)
        return None

    def get_str(self, data) -> str:
        return str(data)

    def get_int(self, data) -> int:
        return int(data)
