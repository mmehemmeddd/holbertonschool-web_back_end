#!/usr/bin/env python3
"""
Bu modul MongoDB kolleksiyasındakı bütün sənədləri
listələyən funksiyanı ehtiva edir.
"""


def list_all(mongo_collection):
    """
    Kolleksiyadakı bütün sənədləri siyahı şəklində qaytarır.
    Əgər sənəd yoxdursa, boş siyahı ([]) qaytarır.
    """
    if mongo_collection is None:
        return []
    
    # find() funksiyası heç bir şərt olmadan bütün sənədləri gətirir
    # list() onu Python siyahısına çevirir
    return list(mongo_collection.find())	
