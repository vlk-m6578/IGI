"""
Square class for inscribed square calculations.
"""

from task4.shape import GeometricShape
from task4.color import Color
from math import sqrt

class Square(GeometricShape):
    """Represents a square inscribed in a circle."""

    shape_name = "Square"

    def __init__(self, radius: float, color: str):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius
        self._color = Color(color)

    @property
    def radius(self) -> float:
        """Get circle radius."""
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        """Set radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def area(self) -> float:
        """Calculate square area: (2R)^2 / 2 = 2R²"""
        return 2 * self._radius ** 2
    
    @property
    def side_length(self) -> float:
        """Calculate square side: R*sqrt(2)"""
        return self._radius * sqrt(2)
    
    def __str__(self) -> str:
        """String representation using pyformat."""
        return ("{name} (radius: {radius:.2f}, color: {color}, "
                "area: {area:.2f})").format(
            name=self.shape_name,
            radius=self.radius,
            color=self._color.color,
            area=self.area()
        )
