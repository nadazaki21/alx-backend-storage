#!/usr/bin/env python3
""" Exercise file for mandatory tasks  """

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def replay(self, method: Callable):
    """  function to display the history of calls of a particular function. """
    number_of_calls = self.__redis.get(method.__qualname__)
    print(f"{method.__qualname__}was called {number_of_calls} times")
def call_history(method: Callable) -> Callable:
    """Call history decorator"""

    @wraps(method)
    def inner(self, *args):
        output = self.__redis.rpush(f"{method.__qualname__}:inputs", args)
        self.__redis.lpush(f"{method.__qualname__}:output", str(output))
        return output

    return inner


def count_calls(method: Callable) -> Callable:
    """Count calls in redis decorator"""

    @wraps(method)
    def inner(self, method):
        self.__redis.incr(method.__qualname__)
        return method(self, method)

    return inner


class Cache:
    """Class for cache"""

    def __init__(self) -> None:
        """Initialize cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        random_id = str(uuid.uuid4())
        self.__redis.set(random_id, data)
        return random_id

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get data from redis"""
        data = self._redis.get(key)
        if data:
            return fn(data)
        #return None
        return data

    def get_str(self, data) -> str:
        """Get string from redis"""
        return str(data)

    def get_int(self, data) -> int:
        """Get int from redis"""
        return int(data)
