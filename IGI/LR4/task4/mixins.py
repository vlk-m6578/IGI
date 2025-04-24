class PositiveValueValidatorMixin:
    
    def _validate_positive(self, value: float, field_name: str) -> None:
        if value <= 0:
            raise ValueError(f"{field_name} must be positive. Got: {value}")