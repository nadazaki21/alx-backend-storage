#!/usr/bin/env python3
""" Advanced Task """
import requests
import redis

redis_obj = redis.Redis()
count = 0
def get_page(url: str) -> str:
    """ uses the requests module to obtain the
    HTML content of a particular URL and returns it. """
    data = requests.get(url)
    count = count + 1
    redis_obj.setex(f"count:{url}",10, count)
    
    return data.text