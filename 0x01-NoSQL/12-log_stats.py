#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    school_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(school_collection.estimated_document_count()))
    print("Methods:")
    for i in methods:
        print(f"\tmethod {i}: {school_collection.count_documents({'method': i})}")
    status_number = school_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_number} status check")
