#!/usr/bin/env python3
""" Exercise file for mandatory tasks  """

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method : Callable )-> Callable:
    @wraps(method)
    def inner(self,method):
        self.__redis.incr(method.__qualname__)
        return method(self,method)
    return inner  
        
    
class Cache:
    """Class for cache"""

    def __init__(self) -> None:
        """Initialize cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        random_id = str(uuid.uuid4())
        self.__redis.set(random_id, data)
        return random_id

    def get(self, key: str, fn: callable = None):
        """Get data from redis"""
        data = self._redis.get(key)
        if data:
            return fn(data)
        return None

    def get_str(self, data) -> str:
        """Get string from redis"""
        return str(data)

    def get_int(self, data) -> int:
        """Get int from redis"""
        return int(data)
