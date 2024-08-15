#!/usr/bin/env python3

from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps

"""
    Writing strings to Redis.
"""


def count_calls(method: Callable) -> Callable:
    """
    a system to count how many
    times methods of the Cache class are called.
    :param method:
    :return:
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrap
        :param self:
        :param args:
        :param kwargs:
        :return:
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    """Call history decorator"""

    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])
    @wraps(method)
    def wrapper(self, *args):
        """ inner """
        def wrapper(self, *args, **kwargs):
            """ Wrapp """
            self._redis.rpush(i, str(args))
            res = method(self, *args, **kwargs)
            self._redis.rpush(o, str(res))
            return res

    return wrapper


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

    @count_calls
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

        if fn:
            return fn(data)

        return data

    def get_str(self, data: Union[str, bytes, int, float]) -> str:
        """Get string from redis"""
        return data.decode("utf-8")

    def get_int(self, data: Union[str, bytes, int, float]) -> int:
        """Get int from redis"""
        return data.decode("utf-8")
