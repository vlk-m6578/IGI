def validate_float(prompt: str) -> float:
    """Get validated float input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive")
            return value
        except ValueError as e:
            print(f"Error: {str(e)}")