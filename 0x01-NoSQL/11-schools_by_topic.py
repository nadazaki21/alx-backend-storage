#!/usr/bin/env python3
""" Task 10 """


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    x = mongo_collection.find({"topics": topic})
    # print(mongo_collection)
    return x
