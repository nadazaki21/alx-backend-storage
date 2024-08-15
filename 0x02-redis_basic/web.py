#!/usr/bin/env python3
""" Advanced Task """
import requests
import redis
from typing import Callable
from functools import wraps

redis_obj = redis.Redis()


def wrapper_function(f: Callable) -> Callable:
    """wrapper function"""

    @wraps(f)
    def wrapper(url: str, *args, **kwargs):
        redis_obj.incr(f"count:{url}")
        # the cached data may still have not expired
        cached_data = redis_obj.get(f"cached:{url}")
        if cached_data:
            return cached_data.decode("utf-8")

        response = f(url, *args, **kwargs)
        redis_obj.setex(f"cached:{url}", 10, response)
        return response

    return wrapper


@wrapper_function
def get_page(url: str) -> str:
    """uses the requests module to obtain the
    HTML content of a particular URL and returns it."""
    data = requests.get(url)
    return data.text
