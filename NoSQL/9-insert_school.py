#!/usr/bin/env python3
"""
Bu modul MongoDB kolleksiyasına yeni sənəd əlavə edən
funksiyanı ehtiva edir.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Kolleksiyaya kwargs əsasında yeni sənəd əlavə edir
    və yeni yaradılan sənədin _id dəyərini qaytarır.
    """
    # kwargs avtomatik olaraq dictionary (lüğət) kimi davranır
    # insert_one vasitəsilə onu bazaya əlavə edirik
    new_document = mongo_collection.insert_one(kwargs)
    
    # Əlavə olunmuş sənədin ID-sini qaytarırıq
    return new_document.inserted_id
