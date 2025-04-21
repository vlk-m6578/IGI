"""
Handles user interaction for matrix operations.
"""

import numpy as np
from task5.matrix_processor import MatrixProcessor

class MatrixController:
    """Manages matrix analysis workflow."""
    
    def run(self):
        """Execute full analysis pipeline."""
        while True:
            try:
                n = self._get_int_input("Enter number of rows: ", min_val=1)
                m = self._get_int_input("Enter number of columns: ", min_val=1)
                processor = MatrixProcessor(n, m)
                
                print("\nOriginal matrix:")
                print(processor.matrix)
                
                modified = processor.swap_max_with_diagonal()
                print("\nModified matrix:")
                print(modified)
                
                diagonal = np.diagonal(modified)
                print("\nMain diagonal:", diagonal)
                
                print("\nMedian calculation:")
                print(f"Numpy median: {np.median(diagonal):.2f}")
                print(f"Manual median: {MatrixProcessor.manual_median(diagonal):.2f}")
                
                if input("\nRepeat? (y/n): ").lower() != 'y':
                    break
                    
            except Exception as e:
                print(f"Error: {str(e)}")
    
    def _get_int_input(self, prompt: str, min_val: int = 0) -> int:
        """Get validated integer input."""
        while True:
            try:
                value = int(input(prompt))
                if value < min_val:
                    raise ValueError(f"Value must be >= {min_val}")
                return value
            except ValueError as e:
                print(f"Invalid input: {str(e)}")