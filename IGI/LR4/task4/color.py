class Color:
    """Handles color property for shapes."""
    
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        """Get color name."""
        return self._color
    
    @color.setter
    def color(self, value: str):
        """Set color name with validation."""
        if not isinstance(value, str):
            raise ValueError("Color must be a string")
        self._color = value