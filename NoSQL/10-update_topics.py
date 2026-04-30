#!/usr/bin/env python3
"""
Bu modul məktəb adına əsasən mövzuları (topics)
yeniləyən funksiyanı ehtiva edir.
"""


def update_topics(mongo_collection, name, topics):
    """
    Verilmiş ada uyğun gələn məktəbin sənədini tapır və
    onun mövzularını (topics) yeni verilən siyahı ilə əvəz edir.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
