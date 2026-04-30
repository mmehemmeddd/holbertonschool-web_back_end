#!/usr/bin/env python3
"""
Bu modul verilmiş mövzuya (topic) əsasən məktəbləri
tapıb siyahısını qaytaran funksiyanı ehtiva edir.
"""


def schools_by_topic(mongo_collection, topic):
    """
    'topics' sahəsində axtarılan 'topic' olan
    bütün məktəbləri tapır.
    """
    # MongoDB-də array içində axtarış etmək üçün
    # sadəcə sahənin adını və axtarılan dəyəri vermək bəs edir.
    return list(mongo_collection.find({"topics": topic}))
