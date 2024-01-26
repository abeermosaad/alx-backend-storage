#!/usr/bin/env python3
"""Redis exercise module"""
import redis
from typing import Union, Optional, Any
import uuid


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """Store method"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    @staticmethod
    def get_int(value):
        """Convert bytes to int"""
        return int(value)

    @staticmethod
    def get_str(value):
        """Convert bytes to str"""
        return str(value)

    def get(self, key: str, fn: Optional[Any] = None) -> Any:
        """Get method"""
        val = self._redis.get(key)
        if fn:
            if fn == int:
                return self.get_int(val)
            elif fn == str:
                return self.get_str(val)
            else:
                return fn(val)
        return val
