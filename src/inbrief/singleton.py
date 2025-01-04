from threading import Lock
from typing import Any


# Metaclass for Singleton
class Singleton(type):
    """Thread-safe Singleton metaclass.

    Example:
        >>> class MyClass(metaclass=Singleton):
        >>>    pass

    Note:
        Pydantic models cannot use Singleton metaclass since they use different metaclass.
    """

    _instances: dict[type, Any] = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
