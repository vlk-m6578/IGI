import matplotlib.colors as mcolors

class ColorValidatorMixin:
    
    def _validate_color(self, color: str) -> str:
        try:
            return mcolors.to_hex(color)
        except ValueError:
            raise ValueError(f"Invalid color: {color}")

class Color(ColorValidatorMixin):
    
    def __init__(self, color: str):
        self._color = self._validate_color(color) 

    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, value: str):
        self._color = self._validate_color(value)

    @color.getter
    def color(self):
        return self._color