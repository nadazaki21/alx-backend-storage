#!/usr/bin/env python3
""" Advanced Task """
import requests
import redis
from typing import Callable
from functools import wraps

redis_obj = redis.Redis()
count = 0


def wrapper_function(f: Callable) -> Callable:
    """wrapper function"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        count = count + 1
        redis_obj.setex(f"count:{args}", 10, count)
        return f(*args, **kwargs)

    return wrapper


@wrapper_function
def get_page(url: str) -> str:
    """uses the requests module to obtain the
    HTML content of a particular URL and returns it."""
    data = requests.get(url)
    return data.text
