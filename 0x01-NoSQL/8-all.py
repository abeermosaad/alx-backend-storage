#!/usr/bin/env python3
"""list_all function"""


def list_all(mongo_collection):
    """ list all documents in mongo_collection"""
    return mongo_collection.find()
