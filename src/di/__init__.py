"""
Basic Di Services


This package provides a clean architecture approach:
- Domain: Abstract interfaces and exceptions
- injector: Dependency injector
"""

__version__ = "1.0.0"
__author__ = "BrenDev0"
__description__ = "Di for app"


from injector import Injector

__all__ = [
    "Injector"
]
