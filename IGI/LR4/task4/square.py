"""
Square class for inscribed square calculations.
"""

from task4.shape import GeometricShape
from task4.color import Color
from task4.mixins import PositiveValueValidatorMixin
from math import sqrt

class Square(GeometricShape, PositiveValueValidatorMixin):
    """Квадрат, вписанный в окружность радиуса R."""
    
    shape_name = "Square"

    def __init__(self, radius: float, color: str):
        super().__init__(color)
        self._validate_positive(radius, "Radius")
        self._radius = radius
        self._color = Color(color)

    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        self._validate_positive(value, "Radius")
        self._radius = value

    def area(self) -> float:
        return 2 * self._radius ** 2
    
    @property
    def side_length(self) -> float:
        return self._radius * sqrt(2)
    
    def __str__(self) -> str:
        return ("{name} (radius: {radius:.2f}, color: {color}, "
                "area: {area:.2f})").format(
            name=self.shape_name,
            radius=self.radius,
            color=self._color.color,
            area=self.area()
        )
