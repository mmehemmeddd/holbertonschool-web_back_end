#!/usr/bin/env python3
"""
Bu skript MongoDB-dəki 'logs' bazasında olan Nginx
loglarının (qeydlərinin) statistikasını ekrana çıxarır.
"""
from pymongo import MongoClient


def log_stats():
    """Logların statistikasını hesablayır və göstərir"""
    # MongoDB-yə qoşuluruq
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Bütün sənədlərin (logların) ümumi sayını tapırıq
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # 2. Hər bir HTTP metodu üzrə sayları tapırıq
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for
