"""
Abstract base classes for geometric shapes.
"""

from abc import ABC, abstractmethod
from math import sqrt

class GeometricShape(ABC):
    """Abstract base class for geometric shapes."""

    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """Calculate shape's area. Must be overridden."""
        pass

