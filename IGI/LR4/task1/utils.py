"""
Utility functions for Task 1.
"""
from task1.rational import RationalNumber

def input_rational(prompt: str) -> RationalNumber:
    """
    Get valid rational number input from user.
    
    :param prompt: Input prompt message
    :return: RationalNumber instance
    :raises ValueError: For invalid input format
    """
    while True:
        try:
            value = input(prompt)
            parts = value.split('/')
            if(len(parts) != 2):
                raise ValueError("Use a/b format")
            numerator = int(parts[0])
            denominator = int(parts[1])
            return RationalNumber(numerator, denominator)
        except ValueError as e:
            raise ValueError(f"Invalid input: {str(e)}")
        
def validate_input(value: str) -> bool:
    """
    Validate user input for menu choices.
    
    :param value: Input value to validate
    :return: True if valid, False otherwise
    """
    return value.isdigit()
