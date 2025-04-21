"""
Abstract base classes for geometric shapes.
"""

from abc import ABC, abstractmethod
from math import sqrt

class GeometricShape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate shape's area. Must be overridden."""
        pass

