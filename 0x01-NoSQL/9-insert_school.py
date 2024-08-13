#!/usr/bin/env python3
""" Task 9 """


def insert_school(mongo_collection, **kwargs):
    """inserts a new doc and ets its id"""
    return mongo_collection.insert_one(kwargs)
