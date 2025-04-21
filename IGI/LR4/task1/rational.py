

class RationalNumber:
    """Class representing a rational number with numerator and denominator."""
    
    def __init__(self, numerator: int, denominator: int):
        """
        Initialize a rational number.
        
        :param numerator: Integer numerator
        :param denominator: Integer denominator (must not be zero)
        :raises ValueError: If denominator is zero
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self) -> int:
        """Get the numerator."""
        return self._numerator
    
    @property
    def denominator(self) -> int:
        """Get the denominator."""
        return self._denominator
    
    def __eq__(self, other: object) -> bool:
        """Check equality using cross-multiplication."""
        if not isinstance(other, RationalNumber):
            return False
        return(self.numerator * other.denominator) == (other.numerator *self.denominator)
    
    def __gt__(self, other: 'RationalNumber') -> bool:
        """Compare two rational numbers."""
        return (self.numerator * other.denominator) > (other.numerator *self.denominator)
    
    def __str__(self) -> str:
        """String representation of the rational number."""
        return f"{self.numerator}/{self.denominator}"
    
    def __lt__(self, other: 'RationalNumber') -> bool:
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)