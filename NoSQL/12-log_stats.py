#!/usr/bin/env python3
"""
Bu skript MongoDB-dəki 'logs' bazasında olan Nginx
loglarının (qeydlərinin) statistikasını ekrana çıxarır.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # MongoDB-yə qoşuluruq
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Bütün sənədlərin (logların) ümumi sayını tapırıq
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # 2. Hər bir HTTP metodu üzrə sayları tapırıq
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # 3. 'method=GET' və 'path=/status' olan sənədlərin sayını tapırıq
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))
